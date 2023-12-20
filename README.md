# Reinforcement-Learning-for-Generative-AI-Large-Language-Models

### Group Members Name UNI

- Yi Lu yl5118  (Team Captain)
- Yanni Chen yc479 
- Junyuan Huang jh4608  
- Xiaolin Sima xs2483
- Michelle Sun ms6514

Emails  &lt;UNI&gt; @ columbia.edu

**Accenture mentor & co-mentors:** Satish Banka, Subha Seshagiri

**Instructor/CA:** Prof. Sining Chen, Vivian Zhang

We want to unlock significant insights into the Oil and Gas Industry through the use of generative AI. Company documentations such as annual reports and sustainability reports can range from 50 to 500 pages, and often contain large amount of numeric and textual information. With the help of Large Language Models (LLMs), the process of understanding how the company performs can be really efficient. 

The capstone project aims to test, fine-tune, and improve the performance of the open-source Large Language Model (LLM) - Llama2. Our methodology involved a comprehensive approach to data preparation, including gathering recent annual, sustainability, and quarterly reports from ten leading companies in the Oil and Gas Industry. The project achieved significant advancements, with the fine-tuning process demonstrating a marked improvement in the model's ability to generate optimized prompts and report analysis. The enhanced prompt optimization model achieved higher ROUGE and BLEU scores of 0.251 to o.317 and 0.035 to 0.049, indicating a more significant overlap with the reference good prompt. Additionally, the fine-tuned report analysis model exhibited improved BLEU and Rouge scores of 0.215 to 0.262 and 0.451 to 0.461, confirming its effectiveness in summarizing annual highlights and extracting key performance indicators. This project's success underscores the potential of LLMs in transforming the analysis of industry-specific documentation, paving the way for more efficient and insightful data-driven decision-making.

Our team members contribute to the project equally with a detailed contribution summary under Meetings/Reports/Individual Report + Weekly Report Combine.pptx

**Directory tree**

├── .git\
│   │
│   ├── hooks\
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── push-to-checkout.sample
│   │   └── update.sample
│   │
│   ├── info\
│   │   └── exclude
│   │
│   ├── logs\
│   │   │
│   │   ├── refs\
│   │   │   │
│   │   │   ├── heads\
│   │   │   │   └── main
│   │   │   │
│   │   │   └── remotes\
│   │   │       │
│   │   │       └── origin\
│   │   │           └── HEAD
│   │   │
│   │   │
│   │   │
│   │   └── HEAD
│   │
│   ├── objects\
│   │   │
│   │   ├── info\
│   │   │
│   │   └── pack\
│   │       ├── pack-cb6df940aab638ce80199d0f1099c1fdb1296be3.idx
│   │       └── pack-cb6df940aab638ce80199d0f1099c1fdb1296be3.pack
│   │
│   │
│   ├── refs\
│   │   │
│   │   ├── heads\
│   │   │   └── main
│   │   │
│   │   ├── remotes\
│   │   │   │
│   │   │   └── origin\
│   │   │       └── HEAD
│   │   │
│   │   │
│   │   └── tags\
│   │
│   │
│   ├── FETCH_HEAD
│   ├── HEAD
│   ├── config
│   ├── description
│   ├── index
│   └── packed-refs
│
├── App\
│   │
│   ├── adapters\
│   │   │
│   │   ├── BPO\
│   │   │   ├── README.md
│   │   │   ├── adapter_config.json
│   │   │   └── adapter_model.bin
│   │   │
│   │   └── Llama\
│   │       ├── README.md
│   │       └── adapter_config.json
│   │
│   │
│   ├── .DS_Store
│   ├── app.py
│   ├── models.py
│   └── utils.py
│
├── Assignment\
│   ├── F23_Accenture_ReinforcementLearningLLM_1st_report.docx
│   ├── F23_Accenture_ReinforcementLearningLLM_1st_report.pdf
│   ├── F23_Accenture_ReinforcementLearningLLM_final_report.docx
│   ├── F23_Accenture_ReinforcementLearningLLM_final_report.pdf
│   ├── F23_Accenture_ReinforcementLearningLLM_poster.pptx
│   ├── F23_Accenture_ReinforcementLearningLLM_poster.pptx.pdf
│   ├── Project Presentation.pptx
│   └── capstone_poster.pptx
│
├── Code\
│   ├── .DS_Store
│   ├── Week0_LangChain Q_A Bot.ipynb
│   ├── Week0_image2table.ipynb
│   ├── Week0_llm.ipynb
│   ├── Week10_kpi.ipynb
│   ├── Week1_Q_A_Conversation.ipynb
│   ├── Week2_Conversation.ipynb
│   ├── Week2_Q_A_chunk200.ipynb
│   ├── Week2_Q_A_chunk400_analysis.ipynb
│   ├── Week2_Q_A_prompt_eng(with prompt template).ipynb
│   ├── Week2_Q_A_test.ipynb
│   ├── Week2_Summarization.ipynb
│   ├── Week3_Generate_Q_A_pairs_by_gpt3.5.ipynb
│   ├── Week3_Loader_Splitter_test.ipynb
│   ├── Week3_Summarization.ipynb
│   ├── Week4_Q_A.ipynb
│   ├── Week4_Summarization_General.ipynb
│   ├── Week4_Summarization_KPI.ipynb
│   ├── Week4_Summarization_Q_A.ipynb
│   ├── Week5_Q_A.ipynb
│   ├── Week5_Summarization_10_Companies_Analysis.ipynb
│   ├── Week5_Summarization_Bad_Retriever.ipynb
│   ├── Week5_Summarization_Function.ipynb
│   ├── Week5_Summarization_Models.ipynb
│   ├── Week5_Summarization_Tune.ipynb
│   ├── Week6_fine_tuning_on_custom_dataset.ipynb
│   ├── Week7_Q_A_comparison.ipynb
│   ├── Week7_Summarization_LLama2.ipynb
│   ├── Week7_Summarization_LLama2_Prompt_Optimizer.ipynb
│   ├── Week7_Summarization_Tuned_Prompt_Optimizer.ipynb
│   ├── Week7_fine_tuning.ipynb
│   ├── Week7_fine_tuning_2.ipynb
│   ├── Week7_summarization_fine_tuning.ipynb
│   ├── Week7_summarization_prompt_fine_tuning.ipynb
│   ├── Week8_Summarization_Tuned_Prompt_Optimizer_T5.ipynb
│   ├── Week8_THU_BPO_Optimizer.ipynb
│   ├── Week8_fine_tuning_comp_2020.ipynb
│   ├── Week8_fine_tuning_comp_chevron2018.ipynb
│   ├── Week8_fine_tuning_exp_v1.ipynb
│   ├── Week8_fine_tuning_exp_v2.ipynb
│   ├── Week8_fine_tuning_exp_v3.ipynb
│   ├── Week8_fine_tuning_exp_v4.ipynb
│   ├── Week8_fine_tuning_exp_v5.ipynb
│   ├── Week8_fine_tuning_exp_v6.ipynb
│   ├── Week8_fine_tuning_exp_v7.ipynb
│   ├── Week8_rlhf.ipynb
│   ├── Week8_summarization_prompt_fine_tuning_BPO.ipynb
│   ├── Week8_summarization_prompt_fine_tuning_T5.ipynb
│   ├── Week9_BPO_fine_tuning_v1.ipynb
│   ├── Week9_BPO_fine_tuning_v2.ipynb
│   ├── Week9_BPO_fine_tuning_v3. ipynb
│   ├── Week9_BPO_fine_tuning_v4. ipynb
│   ├── Week9_Summarization_Tuned_Prompt_Optimizer_BPO.ipynb
│   ├── Week9_fine_tune_fin.ipynb
│   ├── week10-KPI.ipynb
│   └── week9_RLHF.ipynb
│
├── Data\
│   │
│   ├── Company Reports\
│   │   │
│   │   ├── BP PLC\
│   │   │   ├── BP PLC_2018.pdf
│   │   │   ├── BP PLC_2018_sus.pdf
│   │   │   ├── BP PLC_2019.pdf
│   │   │   ├── BP PLC_2019_sus.pdf
│   │   │   ├── BP PLC_2020.pdf
│   │   │   ├── BP PLC_2020_sus.pdf
│   │   │   ├── BP PLC_2021.pdf
│   │   │   ├── BP PLC_2021_sus.pdf
│   │   │   └── BP PLC_2022_sus.pdf
│   │   │
│   │   ├── Chevron\
│   │   │   ├── Chevron_2018.pdf
│   │   │   ├── Chevron_2018_sus.pdf
│   │   │   ├── Chevron_2019.pdf
│   │   │   ├── Chevron_2019_sus.pdf
│   │   │   ├── Chevron_2020.pdf
│   │   │   ├── Chevron_2020_q1.pdf
│   │   │   ├── Chevron_2020_q2.pdf
│   │   │   ├── Chevron_2020_q3.pdf
│   │   │   ├── Chevron_2020_q4.pdf
│   │   │   ├── Chevron_2020_sus.pdf
│   │   │   ├── Chevron_2021.pdf
│   │   │   ├── Chevron_2021_q1.pdf
│   │   │   ├── Chevron_2021_q2.pdf
│   │   │   ├── Chevron_2021_q3.pdf
│   │   │   ├── Chevron_2021_q4.pdf
│   │   │   ├── Chevron_2021_sus.pdf
│   │   │   ├── Chevron_2022_q1.pdf
│   │   │   ├── Chevron_2022_q2.pdf
│   │   │   ├── Chevron_2022_q3.pdf
│   │   │   ├── Chevron_2022_q4.pdf
│   │   │   └── Chevron_2022_sus.pdf
│   │   │
│   │   ├── Marathon Petroleum Corporation\
│   │   │   ├── Marathon Petroleum Corporation_2018.pdf
│   │   │   ├── Marathon Petroleum Corporation_2018_sus.pdf
│   │   │   ├── Marathon Petroleum Corporation_2019.pdf
│   │   │   ├── Marathon Petroleum Corporation_2019_sus.pdf
│   │   │   ├── Marathon Petroleum Corporation_2020.pdf
│   │   │   ├── Marathon Petroleum Corporation_2020_sus.pdf
│   │   │   ├── Marathon Petroleum Corporation_2021.pdf
│   │   │   ├── Marathon Petroleum Corporation_2021_q1.pdf
│   │   │   ├── Marathon Petroleum Corporation_2021_q2.pdf
│   │   │   ├── Marathon Petroleum Corporation_2021_q3.pdf
│   │   │   ├── Marathon Petroleum Corporation_2021_sus.pdf
│   │   │   ├── Marathon Petroleum Corporation_2022_q1.pdf
│   │   │   ├── Marathon Petroleum Corporation_2022_q2.pdf
│   │   │   ├── Marathon Petroleum Corporation_2022_q3.pdf
│   │   │   ├── Marathon Petroleum Corporation_2022_sus.pdf
│   │   │   ├── Marathon Petroleum Corporation_2023_q1.pdf
│   │   │   └── Marathon Petroleum Corporation_2023_q2.pdf
│   │   │
│   │   ├── PetroChina\
│   │   │   ├── PetroChina_2018_sus.pdf
│   │   │   ├── PetroChina_2019.pdf
│   │   │   ├── PetroChina_2019_sus.pdf
│   │   │   ├── PetroChina_2020.pdf
│   │   │   ├── PetroChina_2020_q1.pdf
│   │   │   ├── PetroChina_2020_q3.pdf
│   │   │   ├── PetroChina_2020_sus.pdf
│   │   │   ├── PetroChina_2021.pdf
│   │   │   ├── PetroChina_2021_q1.pdf
│   │   │   ├── PetroChina_2021_q2.pdf
│   │   │   ├── PetroChina_2021_q3.pdf
│   │   │   ├── PetroChina_2021_sus.pdf
│   │   │   ├── PetroChina_2022_q1.pdf
│   │   │   ├── PetroChina_2022_q2.pdf
│   │   │   ├── PetroChina_2022_q3.pdf
│   │   │   ├── PetroChina_2022_sus.pdf
│   │   │   ├── PetroChina_2023.pdf
│   │   │   ├── PetroChina_2023_q1.pdf
│   │   │   └── PetroChina_2023_q2.pdf
│   │   │
│   │   ├── Saudi Aramco\
│   │   │   ├── Saudi Aramco_2019.pdf
│   │   │   ├── Saudi Aramco_2020.pdf
│   │   │   ├── Saudi Aramco_2020_q1.pdf
│   │   │   ├── Saudi Aramco_2020_q2.pdf
│   │   │   ├── Saudi Aramco_2020_q3.pdf
│   │   │   ├── Saudi Aramco_2021.pdf
│   │   │   ├── Saudi Aramco_2021_q1.pdf
│   │   │   ├── Saudi Aramco_2021_q2.pdf
│   │   │   ├── Saudi Aramco_2021_q3.pdf
│   │   │   ├── Saudi Aramco_2021_sus.pdf
│   │   │   ├── Saudi Aramco_2022_q1.pdf
│   │   │   ├── Saudi Aramco_2022_q2.pdf
│   │   │   ├── Saudi Aramco_2022_q3.pdf
│   │   │   ├── Saudi Aramco_2022_sus.pdf
│   │   │   ├── Saudi Aramco_2023_q1.pdf
│   │   │   └── Saudi Aramco_2023_q2.pdf
│   │   │
│   │   ├── Shell plc\
│   │   │   ├── Shell plc_2018.pdf
│   │   │   ├── Shell plc_2018_sus.pdf
│   │   │   ├── Shell plc_2019.pdf
│   │   │   ├── Shell plc_2019_sus.pdf
│   │   │   ├── Shell plc_2020.pdf
│   │   │   ├── Shell plc_2020_sus.pdf
│   │   │   ├── Shell plc_2021.pdf
│   │   │   ├── Shell plc_2021_sus.pdf
│   │   │   └── Shell plc_2022_sus.pdf
│   │   │
│   │   ├── Sinopec\
│   │   │   ├── Sinopec_2018_sus.pdf
│   │   │   ├── Sinopec_2019.pdf
│   │   │   ├── Sinopec_2019_sus.pdf
│   │   │   ├── Sinopec_2020.pdf
│   │   │   ├── Sinopec_2020_sus.pdf
│   │   │   ├── Sinopec_2021.pdf
│   │   │   ├── Sinopec_2021_sus.pdf
│   │   │   └── Sinopec_2022_sus.pdf
│   │   │
│   │   ├── TotalEnergies\
│   │   │   ├── TotalEnergies_2018.pdf
│   │   │   ├── TotalEnergies_2019.pdf
│   │   │   ├── TotalEnergies_2020.pdf
│   │   │   ├── TotalEnergies_2020_sus.pdf
│   │   │   ├── TotalEnergies_2021.pdf
│   │   │   ├── TotalEnergies_2021_q1.pdf
│   │   │   ├── TotalEnergies_2021_q2.pdf
│   │   │   ├── TotalEnergies_2021_q3.pdf
│   │   │   ├── TotalEnergies_2021_sus.pdf
│   │   │   ├── TotalEnergies_2022_q1.pdf
│   │   │   ├── TotalEnergies_2022_q2.pdf
│   │   │   ├── TotalEnergies_2022_q3.pdf
│   │   │   ├── TotalEnergies_2022_sus.pdf
│   │   │   ├── TotalEnergies_2023_q1.pdf
│   │   │   ├── TotalEnergies_2023_q2.pdf
│   │   │   └── TotalEnergies_2023_sus.pdf
│   │   │
│   │   └── Valero Energy\
│   │       ├──  Valero Energy_2020_q1.pdf
│   │       ├──  Valero Energy_2020_q2.pdf
│   │       ├──  Valero Energy_2020_q3.pdf
│   │       ├──  Valero Energy_2020_q4.pdf
│   │       ├──  Valero Energy_2021_q1.pdf
│   │       ├──  Valero Energy_2021_q2.pdf
│   │       ├──  Valero Energy_2021_q3.pdf
│   │       ├──  Valero Energy_2021_q4.pdf
│   │       ├──  Valero Energy_2022_q1.pdf
│   │       ├──  Valero Energy_2022_q2.pdf
│   │       ├──  Valero Energy_2022_q3.pdf
│   │       ├──  Valero Energy_2022_q4.pdf
│   │       ├──  Valero Energy_2023_q1.pdf
│   │       ├── Valero Energy_2017.pdf
│   │       ├── Valero Energy_2018.pdf
│   │       ├── Valero Energy_2019.pdf
│   │       ├── Valero Energy_2020.pdf
│   │       ├── Valero Energy_2020_sus.pdf
│   │       ├── Valero Energy_2021.pdf
│   │       ├── Valero Energy_2021_sus.pdf
│   │       ├── Valero Energy_2022_sus.pdf
│   │       └── Valero Energy_2023_q2.pdf
│   │
│   │
│   ├── Company Reports 2022\
│   │   ├── BP PLC_2022.pdf
│   │   ├── Chevron_2022.pdf
│   │   ├── ExxonMobil_2022.pdf.html
│   │   ├── Marathon Petroleum Corporation_2022.pdf
│   │   ├── PetroChina_2022.pdf
│   │   ├── Saudi Aramco_2022.pdf
│   │   ├── Shell plc_2022.pdf
│   │   ├── Sinopec_2022.pdf
│   │   ├── TotalEnergies_2022.pdf
│   │   └── Valero Energy_2022.pdf
│   │
│   ├── QA_Sample\
│   │   │
│   │   ├── samples\
│   │   │   ├── Chevron_2018.csv
│   │   │   ├── ExxonMobil_2018.csv
│   │   │   ├── Valero Energy_2018.csv
│   │   │   └── Valero Energy_2019.csv
│   │   │
│   │   ├── training_samples\
│   │   │   ├── BP PLC_2018.csv
│   │   │   ├── BP PLC_2019.csv
│   │   │   ├── BP PLC_2020.csv
│   │   │   ├── Chevron_2018.csv
│   │   │   ├── Chevron_2019.csv
│   │   │   ├── Chevron_2020.csv
│   │   │   ├── ExxonMobil_2018.csv
│   │   │   ├── ExxonMobil_2020.csv
│   │   │   ├── Marathon Petroleum Corporation_2018.csv
│   │   │   ├── Marathon Petroleum Corporation_2019.csv
│   │   │   ├── Marathon Petroleum Corporation_2020.csv
│   │   │   ├── PetroChina_2019.csv
│   │   │   ├── PetroChina_2020.csv
│   │   │   ├── Saudi Aramco_2019.csv
│   │   │   ├── Saudi Aramco_2020.csv
│   │   │   ├── Sinopec_2019.csv
│   │   │   ├── Sinopec_2020.csv
│   │   │   ├── TotalEnergies_2018.csv
│   │   │   ├── TotalEnergies_2020.csv
│   │   │   ├── Valero Energy_2018.csv
│   │   │   └── Valero Energy_2019.csv
│   │   │
│   │   ├── BP PLC_2018_Q_A.txt
│   │   ├── Chevron_2018.csv
│   │   ├── Chevron_2018.xlsx
│   │   ├── Chevron_2018_Flan_t5.csv
│   │   ├── Chevron_2018_Llama_7B.csv
│   │   ├── Chevron_2018_Llama_7B.xlsx
│   │   ├── Chevron_2018_Llama_7B_new.csv
│   │   ├── Chevron_2018_Llama_7B_new.xlsx
│   │   ├── Chevron_2018_Llama_7B_v2.csv
│   │   ├── Chevron_2018_Llama_7B_v6.csv
│   │   ├── Chevron_2018_Mistral_7B.csv
│   │   ├── ExxonMobil_2018_Q_A.txt
│   │   ├── ls_export_data.csv
│   │   ├── ls_export_data.json
│   │   ├── rm_data.csv
│   │   ├── test.csv
│   │   ├── test_result_llama_ori.csv
│   │   ├── test_result_llama_v6.csv
│   │   └── test_result_llama_v7.csv
│   │
│   ├── Summarization_Sample\
│   │   ├── prompt_sample.csv
│   │   ├── prompt_sample.xlsx
│   │   ├── summary_sample.csv
│   │   └── summary_sample.xlsx
│   │
│   ├── GPT_Optimization_Prompt.docx
│   ├── Generated_Summarization_Tuning.xlsx
│   ├── KPI_ans.xlsx
│   ├── KPI_fin.csv
│   ├── KPI_ori.csv
│   ├── KPI_v7.csv
│   └── KPI_v7.xlsx
│
├── Meetings\
│   │
│   ├── Reports\
│   │   ├── (Template) Weekly Report Form.docx
│   │   ├── (Template) Weekly Report Slides.pptx
│   │   ├── Individual Report + Weekly Report Combine.pptx
│   │   ├── Weekly Report Form 10_13.docx
│   │   ├── Weekly Report Form 10_19.docx
│   │   ├── Weekly Report Form 10_27.docx
│   │   ├── Weekly Report Form 10_5.docx
│   │   ├── Weekly Report Form 11_10.docx
│   │   ├── Weekly Report Form 11_17.docx
│   │   ├── Weekly Report Form 11_3.docx
│   │   ├── Weekly Report Form 9_28.docx
│   │   ├── Weekly Report Slides 10_13.pptx
│   │   ├── Weekly Report Slides 10_19.pptx
│   │   ├── Weekly Report Slides 10_27.pptx
│   │   ├── Weekly Report Slides 10_5.pptx
│   │   ├── Weekly Report Slides 11_10.pptx
│   │   ├── Weekly Report Slides 11_17.pptx
│   │   ├── Weekly Report Slides 11_3.pptx
│   │   └── Weekly Report Slides 12_1.pptx
│   │
│   ├── Slides\
│   │   ├── BPO workflow.pptx
│   │   ├── Capstone_project_Industry_insights_from_KPIs.pptx
│   │   ├── Options for Prompt Optimization.pptx
│   │   ├── Project Progress.pptx
│   │   ├── Summarization Company Analysis.pptx
│   │   └── Summarization Workflow.pptx
│   │
│   └── .DS_Store
│
├── Research\
│   │
│   ├── Code\
│   │   ├── Week0_LangChain Q_A Bot.ipynb
│   │   ├── Week0_image2table.ipynb
│   │   ├── Week0_llm.ipynb
│   │   ├── Week1_Q_A_Conversation.ipynb
│   │   ├── Week2_Conversation.ipynb
│   │   ├── Week2_Q_A_chunk200.ipynb
│   │   ├── Week2_Q_A_chunk400_analysis.ipynb
│   │   ├── Week2_Q_A_prompt_eng(with prompt template).ipynb
│   │   ├── Week2_Q_A_test.ipynb
│   │   ├── Week2_Summarization.ipynb
│   │   ├── Week3_Generate_Q_A_pairs_by_gpt3.5.ipynb
│   │   ├── Week3_Loader_Splitter_test.ipynb
│   │   ├── Week3_Summarization.ipynb
│   │   ├── Week4_Q_A.ipynb
│   │   ├── Week4_Summarization_General.ipynb
│   │   ├── Week4_Summarization_KPI.ipynb
│   │   ├── Week4_Summarization_Q_A.ipynb
│   │   ├── Week5_Q_A.ipynb
│   │   ├── Week5_Summarization_10_Companies_Analysis.ipynb
│   │   ├── Week5_Summarization_Bad_Retriever.ipynb
│   │   ├── Week5_Summarization_Function.ipynb
│   │   ├── Week5_Summarization_Models.ipynb
│   │   ├── Week5_Summarization_Tune.ipynb
│   │   ├── Week6_fine_tuning_on_custom_dataset.ipynb
│   │   ├── Week7_Q_A_comparison.ipynb
│   │   ├── Week7_Summarization_LLama2.ipynb
│   │   ├── Week7_Summarization_LLama2_Prompt_Optimizer.ipynb
│   │   ├── Week7_Summarization_Tuned_Prompt_Optimizer.ipynb
│   │   ├── Week7_fine_tuning.ipynb
│   │   ├── Week7_fine_tuning_2.ipynb
│   │   ├── Week7_summarization_fine_tuning.ipynb
│   │   ├── Week7_summarization_prompt_fine_tuning.ipynb
│   │   ├── Week8_Summarization_Tuned_Prompt_Optimizer_T5.ipynb
│   │   ├── Week8_THU_BPO_Optimizer.ipynb
│   │   ├── Week8_fine_tuning_comp_2020.ipynb
│   │   ├── Week8_fine_tuning_comp_chevron2018.ipynb
│   │   ├── Week8_fine_tuning_exp_v1.ipynb
│   │   ├── Week8_fine_tuning_exp_v2.ipynb
│   │   ├── Week8_fine_tuning_exp_v3.ipynb
│   │   ├── Week8_fine_tuning_exp_v4.ipynb
│   │   ├── Week8_fine_tuning_exp_v5.ipynb
│   │   ├── Week8_fine_tuning_exp_v6.ipynb
│   │   ├── Week8_fine_tuning_exp_v7.ipynb
│   │   ├── Week8_rlhf.ipynb
│   │   ├── Week8_summarization_prompt_fine_tuning_BPO.ipynb
│   │   ├── Week8_summarization_prompt_fine_tuning_T5.ipynb
│   │   ├── Week9_BPO_fine_tuning_v1.ipynb
│   │   ├── Week9_BPO_fine_tuning_v2.ipynb
│   │   ├── Week9_BPO_fine_tuning_v3. ipynb
│   │   ├── Week9_BPO_fine_tuning_v4. ipynb
│   │   ├── Week9_Summarization_Tuned_Prompt_Optimizer_BPO.ipynb
│   │   ├── Week9_fine_tune_fin.ipynb
│   │   └── week9_RLHF.ipynb
│   │
│   ├── HPC.docx
│   ├── LLM Exploration Group Project.docx
│   ├── Oil KPIs.docx
│   ├── Q_A Testing Questions.docx
│   └── Week 1 Required Tasks - Research Result.docx
│
├── .DS_Store
└── README.md
