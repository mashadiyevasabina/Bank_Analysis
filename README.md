

# 🏦 Bank Customer Churn Analytics & AI Prediction Portal



## 🏦 Layihə Haqqında

Bu layihə bank məlumatlarının **End-to-End Data Analytics** yanaşması ilə analiz edilməsinə yönəlmişdir.

Əsas məqsəd müştəri davranışını anlamaq, bankı tərk etmə riskini müəyyənləşdirmək, kredit müraciətlərində itirilən imkanları aşkar etmək və biznes qərarlarını məlumatlar əsasında dəstəkləməkdir.

Layihə çərçivəsində:

- **SQL və Python** ilə məlumatlar təmizlənmiş, birləşdirilmiş və analiz üçün hazırlanmışdır.
- **EDA və statistik analiz** vasitəsilə müştəri tranzaksiyalarına təsir edən faktorlar araşdırılmışdır.
- **Power BI** ilə müştəri itkisi və kredit müraciətləri üzrə interaktiv dashboardlar hazırlanmışdır.
- **Machine Learning** ilə bankı tərk etmə riski olan müştəriləri müəyyənləşdirən proqnoz modeli qurulmuşdur.
- **Streamlit** vasitəsilə analitik nəticələrin interaktiv təqdimatı üçün tətbiq hazırlanmışdır.

**Layihənin əsas hədəfi:** Xam bank məlumatlarını biznes üçün faydalı insight-lara və qərarverməni dəstəkləyən analitik həllərə çevirmək.

## 📌 Biznes Dəyəri

Bank sektorunda yeni müştəri cəlb etmək, mövcud müştərini saxlamaqdan (**Customer Retention**) 5 dəfə daha baha başa gəlir. Müştərilərin bankı tərk etməsi (**Churn**) maliyyə itkilərinə və bazar payının azalmasına birbaşa təsir göstərir.

**Bank Customer Churn Analytics & AI Portal** layihəsi müştərilərin tranzaksiya, balans, kredit və demoqrafik göstəricilərini təhlil edən, Churn riskini öncədən proqnozlaşdıran və **avtomatik biznes qərarları (Retention Plan)** yaradan **End-to-End Analitik Platformadır**.

---

### 📂 Dataset Haqqında

Layihədə **2026-cı ilin yanvar–iyun aylarını** əhatə edən bank məlumatlarından istifadə edilmişdir.

**Əsas datasetlər:**
- **Customers:** 5,000 müştəri — yaş, maaş, balans, kredit skoru və churn məlumatları.
- **Loans:** 4,820 kredit müraciəti — kredit məbləği, növü, statusu və rədd səbəbləri.
- **Transactions:** 77,396 tranzaksiya — tarix, məbləğ, valyuta, kateqoriya və əməliyyat kanalı.

**Əlavə məlumat mənbələri:**
- **Open-Meteo API:** 7 şəhər üzrə hava məlumatları.
- **Frankfurter API:** USD və EUR valyuta məzənnələri.
- **Calendar Reference:** Bayram, həftəsonu və iş günləri haqqında məlumatlar.

Bu məlumatlar SQL bazasında birləşdirilərək təmizləmə, statistik analiz, Power BI və Machine Learning mərhələlərində istifadə edilmişdir.


## 📊 Əsas KPI-lar (Key Performance Indicators)

Layihədə bankın fəaliyyətini və müştəri davranışını qiymətləndirmək üçün aşağıdakı əsas göstəricilər müəyyən edilmişdir:

| İstiqamət | KPI-lar |
|---|---|
| **Kredit proqnozu (ML & Streamlit)** | Gələn ay üçün proqnozlaşdırılan kredit sayı, filiallar üzrə gözlənilən kredit tələbi |
| **Müştəri itkisi (Power BI)** | Churn Rate (%), risk altında olan müştəri sayı, Retention Rate (%) |
| **Kredit müraciətləri (Power BI)** | Approval Rate (%), Rejection Rate (%), Conversion Rate (%) |
| **Müştəri davranışı (Statistik analiz)** | Gündəlik tranzaksiya sayı, gündəlik tranzaksiya məbləği (AZN), Average Ticket (AZN), bayram və maaş dövrü üzrə aktivlik fərqi (%) |

**Məqsəd:** Kredit tələbatını proqnozlaşdırmaq, müştəri itkisini izləmək, kredit satışındakı problemləri müəyyən etmək və tranzaksiya davranışını qiymətləndirmək.


- **Machine Learning:** Random Forest modeli riskli müştərilərin 78.5%-ni müəyyən edə bilir.

**Biznes məqsədi:** Müştəri itkisini azaltmaq, kredit satışındakı itirilmiş imkanları müəyyən etmək və bankın qərarvermə prosesini data əsaslı analizlə dəstəkləmək.

## 📊 Məlumat Analitikası Layihəsinin İş Axını

Layihə akademik tələblərə uyğun olaraq aşağıdakı mərhələlər üzrə qurulmuşdur:
![End-to-End Data Analytics Workflow](İmages/project_workflow.png)


### 🧹 Data Cleaning (Silver Layer)

Bronze mərhələsində birləşdirilmiş kredit, müştəri və tranzaksiya məlumatları **Python (Pandas)** vasitəsilə təmizlənərək analiz üçün hazırlanmışdır.

- **Data tipləri:** Tarix və rəqəmsal sütunlar uyğun formatlara çevrilmişdir.
- **Standartlaşdırma:** Mətnlər kiçik hərflərə çevrilmiş, artıq boşluqlar təmizlənmişdir.
- **Dublikatlar:** Kredit məlumatlarında 15 təkrarlanan sətir silinmişdir.
- **Boş dəyərlər:** Kredit statusuna uyğun boş dəyərlər araşdırılmış, çatışmayan faiz dərəcələri məhsul növünə görə medianla doldurulmuşdur.
- **Valyuta məzənnələri:** AZN əməliyyatları üçün boş məzənnələr `1` ilə əvəz edilmişdir.
- **Nəticə:** Təmizlənmiş məlumatlar SQL Server-in `silver` sxeminə və CSV fayllarına yazılmışdır.



1. **📊 Statistik Analiz & EDA:** Müştəri davranışlarındakı anomaliyaları, makro-iqtisadi təsirləri və statistik hipotezləri yoxlamaq.
2. **📈 Power BI Dashboard:** Filiallar, kredit müraciətləri və tranzaksiya dinamikasını biznes vizualları ilə təqdim etmək.
3. **🤖 Machine Learning & AI Portal:** Random Forest modeli ilə Churn ehtimalını proqnozlaşdırmaq və **AI Risk Konsultant** mühərriki vasitəsilə avtomatik tövsiyələr generatorunu işə salmaq.

---

## 📊 Statistik Analiz Və Hipotez Testləri (Statistical Analysis)

Bank müştərilərinin tranzaksiya davranışının bayram günləri, ehtimal olunan maaş dövrü, valyuta məzənnələri (USD/EUR) və hava temperaturu ilə əlaqəsi dərindən araşdırılmışdır.

> 📉 **Təhlil Məlumat Dəsti:** **77,396 tranzaksiya və 181 günlük dinamik məlumat** əsasında aparılmışdır.
> 🛠️ **İstifadə Olunan Statistik Metodlar:** Exploratory Data Analysis (EDA), Shapiro–Wilk Normallıq Testi, Welch t-test, Spearman Correlation və Multiple Linear Regression.

### 🔍 Əsas Statistik Nəticələr (Key Findings):

* 🎈 **Bayram Günləri Təsiri:** İş günlərinə nisbətən bayram günlərində tranzaksiya sayı **8.4%**, ümumi məbləğ isə **33% aşağıdır**. Lakin tranzaksiya sayındakı fərq statistik əhəmiyyətlilik həddinə çatmamışdır ($p > 0.05$).
* 💰 **Maaş Dövrü Təsiri:** Ehtimal olunan maaş günlərində (digər günlərlə müqayisədə) tranzaksiya sayı **28.4%**, tranzaksiya məbləği isə **25.4% yüksəkdir**. Hər iki fərq statistik olaraq tam əhəmiyyətlidir ($p < 0.01$).
* 💱 **Valyuta Məzənnəsi (USD / EUR):** USD kursu ilə tranzaksiya göstəriciləri arasında xətti əlaqə tapılmamışdır. EUR kursu artdıqda isə tranzaksiya sayı və məbləği arasında **zəif mənfi korrelyasiya** müşahidə edilmişdir.
* 🌡️ **Hava Temperaturu Təsiri:** İlkin təhlildə temperatur yüksəldikcə tranzaksiya həcminin azalmağa meyilli olduğu görünürdü. Lakin aylar və gün tipləri (regressiya modelinə) nəzərə alındıqda, temperaturun birbaşa əlaqəsi statistik əhəmiyyətini itirmişdir.

> 🖼️ *Statistik Analiz Qrafikləri:* `notebooks/3_Gold/06_Statistics_EDA.ipynb` daxilində tam parametrik vizuallarla sənədləşdirilmişdir.

---

## 🏗️ Data Architecture (Bronze — Silver — Gold)

Məlumatların emalı modern data mühəndisliyi prinsiplərinə uyğun olaraq 3 qatlı (**Medallion Architecture**) SQL/Data çərçivəsində həyata keçirilmişdir:

| Qat (Layer) | Təsvir Və Məzmun |
| --- | --- |
| 🥉 **Bronze Layer** | Bank sistemindən gələn ilkin, işlənməmiş ham (raw) müştəri tranzaksiya və kredit dataları. |
| 🥈 **Silver Layer** | Təmizlənmiş, deduplikasiya olunmuş, tipləri düzəldilmiş və kənar qiymətlərdən (outliers) təmizlənmiş data. |
| 🥇 **Gold Layer** | Statistik analitikaya, Power BI dashboard-larına və ML təliminə hazır aqreqasiya olunmuş cədvəllər (`gold_churn_predictions.csv`). |

---

## 🛠️ İstifadə Olunan Texnologiya Steki

| Kateqoriya | Texnologiyalar |
| --- | --- |
| **Dillər & Mühit** | Python 3.14, Jupyter Notebook, GitHub Codespaces |
| **Data Manipulyasiyası** | Pandas, NumPy, Scikit-Learn (Pipeline, ColumnTransformer) |
| **Statistika & Math** | SciPy, Statsmodels, Descriptive & Inferential Statistics |
| **Machine Learning** | Random Forest Classifier, Class Weight Balancing, Threshold Tuning |
| **Vizuallaşdırma & BI** | Power BI Desktop, Matplotlib, Seaborn |
| **Veb İnterfeys (App)** | Streamlit (Dark Theme, Progress Bar, Metrics, Interactive Tabs) |
| **Model Serialization** | Joblib (`.pkl` artefaktları) |

---

## 🔮 Machine Learning & Biznes Həddinin (Threshold) Optimallaşdırılması

* **Əsas Alqoritm:** Random Forest Classifier (200 Trees)
* **Data Leakage-Free:** Bütün transformasiyalar (StandardScaler, OneHotEncoder) yalnız `Train` dəstinə fit olunaraq data sızmasının qarşısı 100% alınmışdır.
* **Optimal Biznes Həddi (Threshold = 0.35):** Standart `0.50` həddi bank üçün riskli müştəriləri qaçırdığı üçün, ROC-PR əyrisi üzərindən hədd `0.35`-ə endirilmiş və gedə biləcək müştəriləri tutma nisbəti (**Recall**) **78.5%**-ə yüksəldilmişdir.

| Metrika | Qiymət | Biznes Mənası |
| --- | --- | --- |
| **ROC-AUC** | `0.8410` | Modelin riski fərqləndirmə qabiliyyəti yüksəkdir. |
| **Recall (Gedənləri Tutma)** | `78.5%` | Riskli müştərilərin böyük əksəriyyəti öncədən təyin edilir. |
| **Precision** | `52.3%` | Hədəflənən retention kampaniyalarının dəqiqliyi. |

---

## 🤖 Special Feature: AI Risk Consultant Engine

Streamlit tətbiqinə inteqrasiya edilmiş **AI Risk Konsultant** mühərriki daxil edilən müştəri parametrlərini (balans, rədd edilən kreditlər, tranzaksiya sayı, aktivlik) anlıq təhlil edərək avtomatik şərh və retention strategiyası generasiya edir:
### 💡 Əsas Biznes Insight-ları

- **Müştəri itkisi:** Müştərilərin 20.16%-i bankı tərk edib. Qeyri-aktiv müştərilərdə bu göstərici daha yüksəkdir.
- **Kredit müraciətləri:** Müraciətlərin 38%-i rədd edilir. Əsas rədd səbəbləri arasında yüksək borc yükü və aşağı kredit skoru yer alır.
- **Statistik analiz:** Maaş dövründə tranzaksiya aktivliyi artır, bayram günlərində isə iş günlərinə nisbətən ümumi tranzaksiya məbləği azalır.

> 💡 **Nümunə AI Çıxarışı:**
> * 📉 **Aşağı Balans Riski:** Hesab balansı kritik həddən aşağıdır $\rightarrow$ *Tövsiyə: +0.5% dərəcəli depozit təklif edin.*
> * ⚠️ **Kredit Narazılığı:** 1 rədd edilmiş müraciət var $\rightarrow$ *Tövsiyə: İstehlak kreditinə güzəştli şərtlərlə yenidən baxın.*
> 
> 

---

## 🚀 Live Demo

Try the Bank Customer Churn Risk Predictor application live:

📌 **Canlı Veb Portala Keçid:** [https://bank--churn-analysis.streamlit.app/](https://bank--churn-analysis.streamlit.app/)

---



---

## 🚀 Proyekti Yerli Mühitdə İşə Salmaq

Tətbiqi lokal mühitdə başlatmaq üçün terminalda aşağıdakı əmrləri icra edin:

```bash
# 1. Repozitoriyanı klonlayın
git clone https://github.com/sabina-DataCube2026/Bank_Analysis.git
cd Bank_Analysis

# 2. Lazımi kitabxanaları quraşdırın
pip install -r app/requirements.txt

# 3. Streamlit tətbiqini işə salın
python -m streamlit run app/main.py
