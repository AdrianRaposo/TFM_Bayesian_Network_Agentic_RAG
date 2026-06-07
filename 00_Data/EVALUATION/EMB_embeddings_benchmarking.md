| # | Model                 | Hit Rate@1 | Hit Rate@5 | Hit Rate@10 | Hit Rate@20 | MRR@1      | MRR@5      | MRR@10     | MRR@20     |
| - | --------------------- | ---------- | ---------- | ----------- | ----------- | ---------- | ---------- | ---------- | ---------- |
| a | intfloat/e5-base-v2   | **0.771ᵇ** | **0.875**  | **0.917ᵇᶜ** | **0.922ᵇᶜ** | **0.771ᵇ** | **0.813ᵇ** | **0.819ᵇ** | **0.819ᵇ** |
| b | all-minilm-l6-v2      | 0.714      | 0.839      | 0.859       | 0.859       | 0.714      | 0.758      | 0.761      | 0.761      |
| c | BAAI/bge-base-en-v1.5 | 0.753      | 0.857      | 0.867       | 0.870       | 0.753      | 0.793ᵇ     | 0.795ᵇ     | 0.795ᵇ     |



| Comparison (A vs B)                          | Wins | Ties | Losses | p-value |
| -------------------------------------------- | ---- | ---- | ------ | ------- |
| intfloat/e5-base-v2 vs all-minilm-l6-v2      | 69   | 280  | 35     | < 0.001 |
| intfloat/e5-base-v2 vs BAAI/bge-base-en-v1.5 | 57   | 290  | 37     | 0.1210  |
| all-minilm-l6-v2 vs BAAI/bge-base-en-v1.5    | 36   | 297  | 51     | 0.0410  |



| Comparison (A vs B)                          | Wins | Ties | Losses | p-value |
| -------------------------------------------- | ---- | ---- | ------ | ------- |
| intfloat/e5-base-v2 vs all-minilm-l6-v2      | 32   | 342  | 10     | < 0.001 |
| intfloat/e5-base-v2 vs BAAI/bge-base-en-v1.5 | 28   | 347  | 9      | 0.0050  |
| all-minilm-l6-v2 vs BAAI/bge-base-en-v1.5    | 14   | 353  | 17     | 0.7220  |

