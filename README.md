# Ollama-AI-Sniff

这是一个基于Ollama的论文工具。

通过调用Ollama的api接口，使用所兼容的不同LLM来分析传入的论文是否有AI参与进行辅助研究。

运行analyze_papers_tdmq，输入论文所在dir（支持批处理）。默认使用gemma2模型进行分析。结果将被返回到脚本所在的dir命名为analysis_result.txt。

论文中如果提到其中AI参与了研究，其txt文档名将被标记为+记录在analysis_result.txt。

如果没有提到AI，文档名被标记为-记录在analysis_result.txt。

