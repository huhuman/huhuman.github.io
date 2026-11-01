# 網站內容複核清單

更新日期：2026-10-31。這份文件是編輯工作底稿，須排除於 Jekyll 建置、站內搜尋和 sitemap；不是公開作品集文案。本檔會隨原始碼推送至公開 repository，仍可被讀取，因此請勿在此填寫公司機密、未公開資料或個人敏感資訊。

本輪以指定履歷 `Shun_Hsiang_Hsu_Resume_2026.pdf`、已核准的網站 audit、現有 bibliography，以及下列作者／出版社／學術機構頁面為依據。履歷以 PyMuPDF 抽取兩頁文字。公開頁面保留有依據的成果，尚未取得的指標定義、實驗表與個人分工細節集中列於本檔，沒有加入網站中的 TODO 或虛構結果。

## 優先確認

- [ ] 確認預計 2027 畢業資訊。首頁已移除求職及到職年份宣告；學位維持 Construction Engineering and Management Ph.D. 與 UIUC Master of Computer Science。
- [ ] 複核首頁專案摘要、Experience 時間軸、網頁 CV 與 PDF 的公司、職稱、日期、成果數字是否一致。
- [ ] 確認公司經歷中沿用履歷的數字與文字仍適合公開；補資料時只使用可公開的範圍。
- [ ] 確認專案摘要與時間軸敘述符合實際分工。論文詳細分工不足的舊研究目前只標示 First author，沒有推論模型實作、資料標註或實驗皆由本人獨立完成。
- [ ] 正式發佈前再次檢查論文狀態、公共連結及資料釋出範圍。
- [ ] 確認履歷 PDF 內的電話／email 仍打算公開；網站沿用既有插畫頭像，可依求職定位換成正式照片或維持現狀。

網站已提供靜態 HTML、清楚的職務關鍵詞與結構化個人資料，讓可存取頁面的搜尋或 AI 工具較容易辨識內容。這不代表每個 ATS 都會讀取作品集網址，也不保證通過篩選；投遞用 PDF 仍需依實際職缺調整並與網站保持一致。

## 合成資料：資料版本與量測定義

公開位置：`_data/selected_work.yml` 的合成資料摘要、`assets/json/resume.json` 的 Selected Research。獨立 case study 頁面已移除。

目前數字 **72K**、**三個公開真實影像 benchmark**、**3.7–13.6 IoU points** 來自指定履歷。這次查到 Beyond Cracks 專案頁的資料表另列 SynthCrack-72k 為 71,860 張，並分列 SynthCrack-42k、SynthCrack-ONE 與其他 bridge defect datasets；因此保留履歷的 72K 約數，不把它改寫成多缺陷資料的總量。

- [ ] 補三個 benchmark 名稱、版本、來源、資料切分及每個 benchmark 的結果。
- [ ] 確認 3.7–13.6 是哪一個 baseline 與哪些 realism-enhancement 設定的差值，是否採同一模型、訓練資源與評估條件。
- [ ] 說明「zero-shot」的操作定義，包括真實影像是否參與訓練、外觀轉換、參數選擇或其他程序。
- [ ] 確認 IoU 的平均方式、類別、閾值，以及是否有多次實驗或不確定性估計。單位維持 **IoU points**，不可改成百分比成長。
- [ ] 確認 72K 與 SynthCrack-72k 71,860 張的對應版本，以及既有 `synth-crack40k` 命名與後續版本的關係。
- [ ] 為圖表加上精確的資料版本與實驗範圍，避免把舊 crack 圖當作 Beyond Cracks 全部成果的證據。
- [ ] 確認 CAD-referenced asset recognition 目前仍為 ongoing；目前沒有替它套用 crack segmentation 的結果。

## Google：兩種量測與設計範圍

團隊資訊由本人於內容 review 補充：Google → Google Cloud → Gemini Cloud Assist。首頁時間軸、Selected Work 與 CV 已同步呈現，JSON 使用 `division`／`team` 分開保存。

公開位置：`_data/selected_work.yml` 的 LLM 摘要、`assets/json/resume.json` 的 Google 工作與工程專案。

目前兩個 **over 90%** 直接沿用指定履歷，並分別標成 repeated-evaluation score consistency 與 alignment with human ratings。公開來源無法獨立重現這兩個內部實驗結果。

- [ ] 在可公開範圍內確認 consistency 的定義：完全相同分數、容許誤差內一致，或其他規則；重複次數與分母為何。
- [ ] 確認 human alignment 的定義、人工評分者數量、判斷標準、樣本數與分母；不要把它寫成一般模型 accuracy。
- [ ] 補評估的 troubleshooting 任務範圍與資料選樣方式，避免暗示跨任務泛化或整個產品的指標。
- [ ] 確認 rubric／prompt iteration 與最終評估資料的關係，以及可公開的 disagreement analysis 例子。
- [ ] Skill graph 目前寫為 **designed**。若要改成實作、部署或效果提升，需補相應事實。
- [ ] Autorater 與 skill graph 保持兩項工作；2025 inspection-reporting 論文為獨立學術研究，不能作為 Google 指標的實驗出處。

## Reconstruct：個人所有權與工程結果

公開位置：`assets/json/resume.json` 的 Reconstruct 工作與工程專案；首頁顯示時間軸摘要。

- [ ] 如有可公開數據，補 image matching／3D reconstruction 的成功率、失敗案例、成本或效率；目前只保留履歷中的方法比較與選型用途。
- [ ] 如有可公開數據，補 FiLM + Swin 的 baseline、orientation encoding、top/bottom confusion 與各類 segmentation 指標；目前沒有宣稱已量測到某個改善幅度。
- [ ] 確認新增 inspection-specific object classes 的可公開描述。
- [ ] Active-learning pipeline 明確為公司的**既有系統**；個人貢獻是使用它進行標註迭代、訓練與類別擴充，沒有寫成自行建立整個平台。
- [ ] 若添加示意圖，僅呈現可公開的方法層次，避免內部產品架構、資料樣本或未公開客戶資訊。

## TryTech：prototype、pilot 與評估證據

公開位置：`_data/selected_work.yml` 的 Applied AI 摘要、`assets/json/resume.json` 的 TryTech 工作與工程專案。

- [ ] 確認 customer-support prototype 的實際使用範圍；目前沒有寫成已大規模上線或 production serving。
- [ ] 如有量測，補 task success、retrieval quality、tool failure、human handoff、成本與延遲，並附資料來源與定義；目前沒有編造數字或測試流程。
- [ ] 可用匿名且可公開的例子補充 transaction workflow 與 human escalation 的觸發情境。
- [ ] 確認 embedding classifier 的標籤來源、資料切分、分類效果，以及 automated counts 如何供人員參考；目前沒有宣稱它能客觀衡量整體服務品質。
- [ ] AWS SAM／Lambda 部署來自 inspection／post-disaster assessment pilots，與客服 prototype 分開敘述，不合併成同一架構。
- [ ] 如要加入 demo、code 或客戶 logo，先核對實際可公開的 artifact 與使用範圍。

## Skills：已整合至實際工作，待補充工具對應

首頁已移除獨立 Skills 區塊，改在 Selected Work 與 Experience 各項下方放 2–3 個精簡技能標籤。專案標籤放在 `_data/selected_work.yml` 的 `skills`；經驗標籤放在 `assets/json/resume.json` 各筆 `work.skills`。僅使用履歷已明確對應的方法與工具，例如 Reconstruct 的 Swin／FiLM、TryTech 的 AWS SAM／Lambda。尚未確認用途的 Python、PyTorch、CUDA 等工具不任意套用到特定專案。CV 保留頂層 `skills` 的完整分類，沒有推論熟練度。

- [ ] 提供每個想強調的 skill 對應到哪個專案／工作，以及實際做了什麼。
- [ ] 若有可公開的 code、paper、demo 或 project link，一併提供。
- [ ] 區分直接實作、使用既有系統與合作參與；再將確認過的對應加入網站。

## 論文、連結與書目核對紀錄

| 項目                                    | 本輪處理與依據                                                                                                                                                                                                                                                                                                                | 後續確認                                                                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Beyond Cracks                           | 保留 Under review；保留已可讀取的[作者專案頁](https://huhuman.github.io/rhino-defect-synth/)。                                                                                                                                                                                                                                | 確認是否已有狀態更新。該頁 Paper 按鈕目前仍指向同一專案頁；Code 指向的 GitHub repository 本輪回傳 404，所以未新增 Paper／Code 連結。資料下載頁尚未逐一驗證，未新增直接下載連結。 |
| Self-Evaluation, 2025                   | 新增 [IAARC PDF](https://www.iaarc.org/publications/fulltext/CSCE_CRC_2025_FinalPaper-PDF_165.pdf)。PDF 首頁以 † 註明 Hsu 與 Jung equal contribution，已補 note。                                                                                                                                                             | 確認個人分工的最終用字；摘要不套用 Google 的兩個 >90% 數字。                                                                                                                     |
| VisualSiteDiary, 2024                   | 新增 DOI `10.1016/j.autcon.2024.105483`，由 [Elsevier](https://www.sciencedirect.com/science/article/pii/S092658052400219X) 核對；保留既有三位 equal contribution。                                                                                                                                                           | 如有作者自存稿、code、data 或 demo，可再補可公開且可讀取的正式連結。                                                                                                             |
| VL-Con, 2024                            | 新增 [IAARC PDF](https://www.iaarc.org/publications/fulltext/145_ISARC_2024_Paper_243.pdf)、[作者 repository](https://github.com/huhuman/VL-Con)；DOI `10.22260/ISARC2024/0146` 由 [Illinois Experts](https://experts.illinois.edu/en/publications/vl-con-vision-language-dataset-for-deep-learning-based-constructi/) 核對。 | 履歷提到的 few-shot prompting framework 與已出版版本的對應範圍可再釐清；論文簡介僅依公開文章寫資料集與 domain gap。                                                              |
| Parametric Design, 2024                 | 新增 DOI `10.1061/9780784485262.045` 與 [Illinois Experts 紀錄](https://experts.illinois.edu/en/publications/requirements-for-parametric-design-of-physics-based-synthetic-dat/)。DOI 直接讀取收到 403，但學術機構紀錄明確列出 DOI 與書目。                                                                                   | 如有合法公開的全文版本可再加入；不把這篇早期研究自動視為 72K／IoU 區間的出處。                                                                                                   |
| Indoor defect inspection, 2023          | 新增 DOI `10.1007/s11803-023-2152-5`，由 [Springer](https://link.springer.com/article/10.1007/s11803-023-2152-5) 核對。                                                                                                                                                                                                       | 詳細個人分工待補；目前只標示 First author。                                                                                                                                      |
| Steel fatigue crack label quality, 2022 | 保留既有 DOI；新增可讀取的 [Techno-Press 文章頁](https://www.techno-press.com/papers/19719)。                                                                                                                                                                                                                                 | 詳細個人分工待補；目前只標示 First author。                                                                                                                                      |
| Concrete surface crack segmentation     | [Springer 章節頁](https://link.springer.com/chapter/10.1007/978-3-030-64908-1_3) 列 First Online: 9 January 2021 與建議 citation 年份 2021；已將 year 從 2020 修正為 2021，保留 citation key `hsu2020concrete`，並新增 DOI。                                                                                                  | 會議系列名稱仍為 EWSHM 2020。確認其他個人資料是否也需要區分會議年與出版年。                                                                                                      |

## 發佈前內容驗收

- [ ] 專案摘要與時間軸能清楚呈現工作重點、個人貢獻及實際範圍。
- [ ] 公開頁面沒有 TODO、未確認數字、未公開客戶資訊或機密系統圖。
- [ ] 網頁 CV 的 Selected Research 與 Projects 已顯示，專案與首頁錨點連結可用。
- [ ] 論文摘要與貢獻欄位正常顯示；under-review 與 equal-contribution 標示可見。
- [ ] `docs/content-review.md` 不出現在 `_site`、sitemap 或搜尋索引。
- [x] 本人已授權完成最後安全調查後推送發布；上述清單保留供後續文案補充與複核。
