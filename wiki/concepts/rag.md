# RAG (Retrieval-Augmented Generation)

Giving an LLM external knowledge at query time. The vault shows two contrasting approaches:

- **Vector RAG** — chunk → embed → store in a vector DB (e.g. [[pinecone]]) → retrieve by similarity. Made turnkey by [[gemini-embeddings-2]] + [[claude-code]], including **multimodal** (image/video/text) search. Src: [[google-rag-gemini-embeddings-2]].
- **[[llm-wiki-pattern|LLM Wiki]]** — interlinked human-readable markdown maintained by an LLM (this vault). See [[llm-wiki-vs-rag]] for the comparison ([[andrej-karpathy-llm-wiki-obsidian]]).

Feeding RAG: [[firecrawl]] turns any site into LLM-ready data ([[turn-any-website-llm-ready-firecrawl]]). Also a chapter in [[build-sell-claude-code-course]].
