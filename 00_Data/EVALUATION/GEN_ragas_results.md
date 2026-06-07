| Model              | Faithfulness | Answer Relevancy | Answer Correctness |
| ------------------ | ------------ | ---------------- | ------------------ |
| OPENAI             | **0.9787**   | 0.7797           | 0.5102             |
| GEMINI             | 0.9654       | 0.7818           | 0.6043             |
| OLLAMA_DEEPSEEK_R1 | 0.9197       | 0.8260           | **0.6053**         |
| OLLAMA_LLAMA3_1    | 0.8911       | **0.8409**       | 0.5655             |
| OLLAMA_QWEN3_5     | 0.9648       | 0.4137           | 0.3247             |


| Comparison (A vs B)                   | Result                     | p-value |
| ------------------------------------- | -------------------------- | ------- |
| OPENAI vs GEMINI                      | No Significant Difference  | 0.2178  |
| OPENAI vs OLLAMA_DEEPSEEK_R1          | **Winner: OPENAI**         | 0.0003  |
| OPENAI vs OLLAMA_LLAMA3_1             | **Winner: OPENAI**         | 0.0000  |
| OPENAI vs OLLAMA_QWEN3_5              | No Significant Difference  | 0.0992  |
| GEMINI vs OLLAMA_DEEPSEEK_R1          | **Winner: GEMINI**         | 0.0096  |
| GEMINI vs OLLAMA_LLAMA3_1             | **Winner: GEMINI**         | 0.0009  |
| GEMINI vs OLLAMA_QWEN3_5              | No Significant Difference  | 0.9951  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_LLAMA3_1 | No Significant Difference  | 0.2089  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_QWEN3_5  | **Winner: OLLAMA_QWEN3_5** | 0.0282  |
| OLLAMA_LLAMA3_1 vs OLLAMA_QWEN3_5     | **Winner: OLLAMA_QWEN3_5** | 0.0016  |


| Comparison (A vs B)                   | Result                         | p-value |
| ------------------------------------- | ------------------------------ | ------- |
| OPENAI vs GEMINI                      | No Significant Difference      | 0.8980  |
| OPENAI vs OLLAMA_DEEPSEEK_R1          | **Winner: OLLAMA_DEEPSEEK_R1** | 0.0128  |
| OPENAI vs OLLAMA_LLAMA3_1             | **Winner: OLLAMA_LLAMA3_1**    | 0.0047  |
| OPENAI vs OLLAMA_QWEN3_5              | **Winner: OPENAI**             | 0.0000  |
| GEMINI vs OLLAMA_DEEPSEEK_R1          | **Winner: OLLAMA_DEEPSEEK_R1** | 0.0134  |
| GEMINI vs OLLAMA_LLAMA3_1             | **Winner: OLLAMA_LLAMA3_1**    | 0.0008  |
| GEMINI vs OLLAMA_QWEN3_5              | **Winner: GEMINI**             | 0.0000  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_LLAMA3_1 | No Significant Difference      | 0.3865  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_QWEN3_5  | **Winner: OLLAMA_DEEPSEEK_R1** | 0.0000  |
| OLLAMA_LLAMA3_1 vs OLLAMA_QWEN3_5     | **Winner: OLLAMA_LLAMA3_1**    | 0.0000  |



| Comparison (A vs B)                   | Result                         | p-value |
| ------------------------------------- | ------------------------------ | ------- |
| OPENAI vs GEMINI                      | **Winner: GEMINI**             | 0.0000  |
| OPENAI vs OLLAMA_DEEPSEEK_R1          | **Winner: OLLAMA_DEEPSEEK_R1** | 0.0002  |
| OPENAI vs OLLAMA_LLAMA3_1             | **Winner: OLLAMA_LLAMA3_1**    | 0.0115  |
| OPENAI vs OLLAMA_QWEN3_5              | **Winner: OPENAI**             | 0.0000  |
| GEMINI vs OLLAMA_DEEPSEEK_R1          | No Significant Difference      | 0.8131  |
| GEMINI vs OLLAMA_LLAMA3_1             | No Significant Difference      | 0.0909  |
| GEMINI vs OLLAMA_QWEN3_5              | **Winner: GEMINI**             | 0.0000  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_LLAMA3_1 | No Significant Difference      | 0.1511  |
| OLLAMA_DEEPSEEK_R1 vs OLLAMA_QWEN3_5  | **Winner: OLLAMA_DEEPSEEK_R1** | 0.0000  |
| OLLAMA_LLAMA3_1 vs OLLAMA_QWEN3_5     | **Winner: OLLAMA_LLAMA3_1**    | 0.0000  |



| Model              | Faithfulness Wins | Relevancy Wins | Correctness Wins | TOTAL WINS |
| ------------------ | ----------------- | -------------- | ---------------- | ---------- |
| GEMINI             | 2                 | 1              | 2                | **5**      |
| OLLAMA_LLAMA3_1    | 0                 | 3              | 2                | **5**      |
| OLLAMA_DEEPSEEK_R1 | 0                 | 3              | 2                | **5**      |
| OPENAI             | 2                 | 1              | 1                | 4          |
| OLLAMA_QWEN3_5     | 2                 | 0              | 0                | 2          |



| Model              | Faithfulness Wins | Relevancy Wins | PRAGMATIC WINS |
| ------------------ | ----------------- | -------------- | -------------- |
| OPENAI             | 2                 | 1              | **3**          |
| GEMINI             | 2                 | 1              | **3**          |
| OLLAMA_DEEPSEEK_R1 | 0                 | 3              | **3**          |
| OLLAMA_LLAMA3_1    | 0                 | 3              | **3**          |
| OLLAMA_QWEN3_5     | 2                 | 0              | 2              |
