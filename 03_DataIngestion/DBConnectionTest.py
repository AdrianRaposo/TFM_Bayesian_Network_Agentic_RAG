import os
import psycopg

from psycopg.rows import dict_row
from LoggerSetUp import setup_logger
from config import(
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_SCHEMA,
    REQUIRED_EXTENSIONS,
    REQUIRED_TABLES,
    LOGS_BASE_PATH,
    LOG_LEVEL
)

# Configure logger
logger = setup_logger(
    name=__name__,
    logs_base_path=LOGS_BASE_PATH,
    general_log_filename='DBConnectionTest.log',
    error_log_filename='DBConnectionTest_error.log',
    general_level=LOG_LEVEL,
    error_level='ERROR',
    general_mode='w',
    error_mode='w'
)



def ok(msg): logger.info(f"{msg}")
def warn(msg): logger.warning(f"{msg}")
def err(msg): logger.error(f"{msg}")

def connect_db() -> psycopg.Connection:
    """Establish a connection to the PostgreSQL database."""
    return psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        row_factory=dict_row
    )

def check_extension(cur) -> bool:
    """Check if required extensions are installed in the database."""
    test_passed = True
    cur.execute("SELECT extname FROM pg_extension;")
    installed_extensions = {row['extname'] for row in cur.fetchall()}
    for ext in REQUIRED_EXTENSIONS:
        if ext in installed_extensions:
            ok(f"Extension '{ext}' is installed.")
        else:
            warn(f"Extension '{ext}' is NOT installed.")
            test_passed = False
    return test_passed

def check_tables(cur) -> bool:
    """Check if required tables exist in the database schema."""
    test_passed = True
    cur.execute("""
        SELECT tablename FROM pg_tables
        WHERE schemaname = %s;
    """, (DB_SCHEMA,))
    existing_tables = {row['tablename'] for row in cur.fetchall()}
    for table in REQUIRED_TABLES:
        if table in existing_tables:
            ok(f"Table '{table}' exists.")
        else:
            warn(f"Table '{table}' does NOT exist.")
            test_passed = False
    return test_passed 

def check_column_embedding(cur) -> bool:
    """Check if 'chunk.embedding' column exists and its dimension."""
    test_passed = True
    embedding_dim = None
    has_embedding_col = False
    cur.execute(f"""
        SELECT atttypid::regtype::text AS typ
            FROM pg_attribute
            WHERE attrelid = to_regclass('"BNAR_Chunk_Simp_v1".chunk')
            AND attname = 'embedding'
            AND NOT attisdropped
    """)
    embedding_info = cur.fetchone()
    if embedding_info:
        embedding_dim = embedding_info['typ']
        has_embedding_col = True
    if has_embedding_col:
        ok(f"Column 'embedding' exists in 'chunk' table with dimension {embedding_dim}.")
    else:
        warn("Column 'embedding' does NOT exist in 'chunk' table.")
        test_passed = False
    return test_passed

def check_vector_index(cur) -> bool:
    """Check if a vector index exists on the 'chunk' table."""
    test_passed = True
    cur.execute(f"""
        SELECT indexname, indexdef
        FROM pg_indexes
        WHERE schemaname = '{DB_SCHEMA}'
        AND tablename  = 'chunk';
    """)
    idxs = cur.fetchall()
    vec_indexes = [i for i in idxs if "USING ivfflat" in i['indexdef'] or "USING hnsw" in i['indexdef']]
    if vec_indexes:
        for vec_idx in vec_indexes:
            ok(f"Vector index '{vec_idx['indexname']}' exists on 'chunk' table with definition: {vec_idx['indexdef']}.")
    else:
        warn("No vector index exists on 'chunk' table.")
        test_passed = False
    return test_passed

def smoke_test_query(cur) -> bool:
    """Perform a smoke test query to count records in key tables."""
    test_passed = True
    counts = {}
    for t in ["doc", "chunk", "doc_reference", "doc_table"]:
        try:
            cur.execute(f"SELECT COUNT(*) AS c FROM \"{DB_SCHEMA}\".\"{t}\"")
            counts[t] = cur.fetchone()['c']
        except Exception as e:
            counts[t] = f"error: {e}"
            warn(f"Failed to count records in table '{t}': {e}")
            test_passed = False
    ok("Quick counts:")
    for t, c in counts.items():
        print(f"   • {t}: {str(c)}")
        if isinstance(c, int) and c >= 0:
            ok(f"Table '{t}' has {c} records.")
        else:
            warn(f"Table '{t}' has no records or could not be counted.")
            test_passed = False
    return test_passed


def main():
    """Main function to test database connection and required extensions/tables."""
    try:
        # Connect to the PostgreSQL database
        conn = connect_db()
        if conn:
            logger.info("TEST[1/6] Successfully connected to the database.")

        with conn.cursor() as cur:

            # Check for required extensions

            passed = check_extension(cur)
            if passed: 
                logger.info(f"TEST[2/6] Successfully checked installed extensions")
            else:
                logger.warning(f"TEST[2/6] Some required extensions are missing")

            # Check for required tables
            passed = check_tables(cur)
            if passed:
                logger.info(f"TEST[3/6] Successfully checked required tables")
            else:
                logger.warning(f"TEST[3/6] Some required tables are missing")

            # Check column 'chunk.embedding' and its dimension
            passed = check_column_embedding(cur)
            if passed:
                logger.info(f"TEST[4/6] Successfully checked 'chunk.embedding' column")
            else:
                logger.warning(f"TEST[4/6] 'chunk.embedding' column is missing or incorrect")
            # Check vectorial index
            passed = check_vector_index(cur)
            if passed:
                logger.info(f"TEST[5/6] Successfully checked vector indexes on 'chunk' table")
            else:
                logger.warning(f"TEST[5/6] No vector indexes found on 'chunk' table")

            # Check smoke test query
            passed = smoke_test_query(cur)
            if passed:
                logger.info(f"TEST[6/6] Successfully executed smoke test queries")
            else:
                logger.warning(f"TEST[6/6] Smoke test queries found issues")
        logger.info("All tests completed.")

    except Exception as e:
        err(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            ok("Database connection closed.")

if __name__ == "__main__":
    main()
