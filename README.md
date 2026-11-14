<p align="center">
  <img src="images/Banner.jpg" alt="Bank Customer Churn Analytics & AI Portal Banner" width="100%" />
</p>

# 🏦 End-to-End Banking Data Analytics
Customer Churn | Loan Analytics | Transaction Behavior | Predictive Modeling

---
## Project Overview

This end-to-end Banking Data Analytics project focuses on analyzing customer behavior, loan applications, financial transactions, and customer churn.

The project aims to integrate banking datasets with external weather, exchange rate, and calendar data to support data-driven business decisions through statistical analysis, interactive Power BI dashboards, and predictive modeling.



## Project Objectives

- Analyze customer churn, retention patterns, and loan application outcomes.
- Investigate how calendar events, exchange rates, and weather conditions relate to customer transaction behavior.
- Develop predictive models to support banking decisions and risk assessment.
- Deliver actionable insights through interactive Power BI dashboards and a Streamlit application.



## Business Questions

The project addresses four key business questions:

1. **Loan Sales Forecasting:** How much loan sales volume is expected across bank branches next month, and how should branches prepare?

2. **Customer Churn & Retention:** Which customers are at risk of leaving the bank, and is retaining them financially worthwhile?

3. **Loan Application Analysis:** Where are potential loan sales opportunities being lost during the loan application process?

4. **Customer Behavior Analysis:** How do holidays, salary days, exchange rates, and weather conditions influence customer transaction behavior?




## End-to-End Project Workflow

<p align="center">
  <img src="images/project_workflow.png" alt="End-to-End Data Analytics Workflow" width="100%" />
</p>



## Technologies & Tools

| Technology | Purpose |
|---|---|
| **Python (3.14)** | Data processing, analysis, pipeline architecture, and predictive modeling |
| **Pandas & NumPy** | Data manipulation, currency conversions, aggregation, and data cleaning |
| **SQL Server** | Data storage and management using Medallion Architecture (Bronze–Silver–Gold) |
| **Jupyter Notebook** | Documentation of Exploratory Data Analysis (EDA) and statistical analyses |
| **SciPy & Statsmodels** | Statistical hypothesis testing (Welch's t-test, Shapiro–Wilk test, Spearman correlation, and linear regression) |
| **Scikit-Learn** | Machine learning model development, ColumnTransformer, Pipeline, and threshold optimization |
| **Power BI Desktop** | Interactive data visualizations and business dashboards for management decision-making |
| **Streamlit** | Development of an interactive web application and deployment of the AI Risk Consultant |
| **Joblib** | Serialization of trained ML models and optimized decision thresholds (`.pkl` files) |
| **Git & GitHub** | Version control, collaborative development, and automated deployment through Streamlit Cloud |



## Dataset Overview

The project uses synthetic banking datasets covering January–June 2026, enriched with calendar information and external API data.

| Dataset | Records | Key Attributes |
|---|---:|---|
| **Customers** | 5,000 | Customer ID, age, gender, city, branch, tenure, credit score, account balance, salary, number of products, card ownership, activity status, and churn status |
| **Transactions** | 77,396 | Transaction ID, customer ID, date, time, amount, currency (AZN, USD, EUR), transaction category, and channel |
| **Loans** | 4,820 | Loan ID, customer ID, application date, loan type, amount, term, interest rate, approval/rejection status, rejection reason, and default indicator |
| **Calendar** | 181 | Date, holiday status and name, weekend, working-day, and pre-holiday indicators |
| **External APIs** | — | Weather temperature, precipitation, wind indicators, and USD/EUR exchange rates |


### External Data Sources

- **[Open-Meteo Historical Weather API](https://archive-api.open-meteo.com/v1/archive):** Historical weather data across 7 cities, including daily average temperature, precipitation, and maximum wind speed.

- **[Frankfurter Exchange Rates API](https://api.frankfurter.dev/v2/rates):** Historical exchange rate data for AZN, USD, and EUR covering January–June 2026.

- **Calendar Reference (CSV):** Calendar data containing working days, weekends, public holidays, and estimated salary-day indicators.


**Note:** Record counts refer to the original datasets before data cleaning and transformation. Final record counts may differ after preprocessing.


## Data Architecture — Medallion Architecture

The project follows a three-layer Medallion Architecture in SQL Server to organize data integration, cleaning, and analytical reporting.

| Layer | Purpose |
|---|---|
| **Bronze** | Stores raw banking data and two enriched datasets integrating customer, loan, transaction, calendar, weather, and exchange rate information. |
| **Silver** | Contains cleaned and standardized loan and transaction datasets, with duplicate handling, missing value treatment, and data validation. |
| **Gold** | Contains 25 business-focused reporting tables for customer churn and loan application analysis, used to build Power BI dashboards. |



## Data Preparation & Cleaning

### Bronze Layer — Data Integration

The raw banking datasets were loaded into SQL Server and integrated with external data sources using Python and Pandas.

Two enriched datasets were created:

- **Loans Enriched:** Combined customer and loan records with calendar and weather data.
- **Transactions Enriched:** Combined transaction and customer records with calendar, weather, and currency exchange rate data.

The enriched datasets were stored in the SQL Server `bronze` schema.

### Silver Layer — Data Cleaning & Transformation

Both enriched datasets were processed to improve data quality, consistency, and reliability.

**Key cleaning operations:**

- **Data Type Conversion:** Standardized date columns and converted relevant numerical fields to appropriate data types.
- **Text Standardization:** Converted text values to lowercase and removed unnecessary whitespace.
- **Duplicate & Referential Integrity Handling:** Removed 15 duplicate loan records and 5 loan records linked to a customer ID missing from the customer dataset.
- **Missing Value Analysis:** Investigated missing values and distinguished expected nulls from data quality issues.
- **Loan Data Cleaning:** Filled missing interest rates for approved loans using median rates grouped by loan product type.
- **Rejection Reason Handling:** Replaced missing rejection reasons for rejected applications with an appropriate descriptive label.
- **Exchange Rate Handling:** Assigned an exchange rate of 1 to AZN-denominated transactions.
- **Data Validation:** Checked missing values in holiday-related fields to ensure consistency with calendar indicators.

The cleaned datasets were saved in the SQL Server `silver` schema as `silver.loans` and `silver.transactions`, and exported as CSV files for further analysis.


### Gold Layer — Business Analytics & Reporting

Using SQL queries and Python, **25 analytical reporting tables** were created from the cleaned Silver-layer data and stored in the SQL Server `gold` schema.

The analysis focuses on two main areas:

- **Customer Churn Analysis (15 tables):** Churn patterns across customer demographics, financial profiles, activity levels, and transaction behavior.
- **Loan Application Analysis (10 tables):** Loan approval and rejection rates, rejection reasons, application trends, and comparisons across customer segments and branches.

The Gold-layer tables were connected to **Power BI Desktop** to develop interactive dashboards supporting business decision-making.


## Power BI Dashboard & Business Insights

An interactive, four-page Power BI dashboard was developed using the SQL Server Gold-layer reporting tables to analyze customer churn and loan application performance.


<p align="center">
  <img src="images/dashboard.png" alt="Power BI Banking Analytics Dashboard" width="100%" />
</p>

### Customer Churn Analysis

- **5,000 customers**, with **1,008 churned customers** and an overall **20.16% churn rate**.
- Inactive customers have a higher churn rate (**28.78%**) than active customers (**14.27%**).
- Customers aged **56+** have the highest churn rate (**33.33%**).
- Churn is particularly high among customers holding **four banking products (66.03%)**.

### Loan Application Analysis

- **4,800 loan applications**, with **2,975 approvals (62%)** and **1,825 rejections (38%)**.
- **Business loans** have the highest rejection rate among loan products (**approximately 74%**).
- Applications exceeding **50,000 AZN** have the highest rejection rate by loan amount group (**approximately 74%**).
- **High debt burden** is the most frequently recorded rejection reason.

The dashboard includes interactive filters for city, branch, gender, and loan product, enabling comparisons across customer segments and banking locations.



## Exploratory Data Analysis & Statistical Testing

Transaction behavior was analyzed using daily transaction counts and amounts converted to AZN, with a focus on calendar events, estimated salary periods, exchange rates, and weather conditions.

**Statistical methods:** Shapiro–Wilk normality test, Welch's t-test, Spearman correlation, Holm correction, and multiple linear regression (OLS) with HAC standard errors.

### Key Findings


- **Holidays:** Daily transaction amounts were 33.02% lower than on regular workdays, while the difference in transaction counts was not statistically significant. This decline was largely associated with the absence of high-value deposit and loan repayment transactions, despite increased shopping activity during holidays.
- **Salary Periods:** Estimated salary periods (days 1–5 and 25–end of month) were associated with higher transaction counts and amounts.
- **Exchange Rates:** EUR exchange rates showed a weak negative correlation with transaction activity, while USD showed no statistically significant relationship.
- **Weather:** Temperature initially showed a negative correlation with transaction activity, but the relationship was not statistically significant after accounting for month and day type.
- **Multivariable Analysis:** Salary periods and day types showed the strongest associations with transaction activity. The regression models explained 69.6% of variation in daily transaction counts and 74.6% in daily transaction amounts (R²).

**Business Insight:** Transaction activity is more strongly associated with salary periods and calendar patterns than with temperature or exchange rate movements after accounting for other factors.




















## 🚀 Live Demo

Try the Bank Customer Churn Risk Predictor application live:

📌 **Canlı Veb Portala Keçid:** [https://bank--churn-analysis.streamlit.app/](https://bank--churn-analysis.streamlit.app/)

---

## 📌 Layihə Haqqında

Bank sektorunda yeni müştəri cəlb etmək, mövcud müştərini saxlamaqdan (**Customer Retention**) 5 dəfə daha baha başa gəlir. Müştərilərin bankı tərk etməsi (**Churn**) maliyyə itkilərinə və bazar payının azalmasına birbaşa təsir göstərir.

**Bank Customer Churn Analytics & AI Portal** bank verilənlərinin təhlili, tarixi makro-iqtisadi və hava şəraiti göstəriciləri ilə zənginləşdirilməsi, statistik araşdırmaların aparılması və müştəri itkisinin öncədən proqnozlaşdırılması üçün Machine Learning modellərinin hazırlanmasını əhatə edən **End-to-End Data Analytics** layihəsidir.

Layihə məlumatların SQL-də Medallion arxitekturası üzrə işlənməsindən başlayaraq statistik təhlil, xüsusiyyətlərin yaradılması (Feature Engineering), proqnozlaşdırıcı modellərin qurulması və canlı AI veb-portalının təqdim edilməsinə qədər olan bütöv mərhələləri əhatə edir.

---

## 🎯 Layihənin Məqsədləri

* Müştərilərin bankı tərk etmə (**Churn**) riskini öncədən proqnozlaşdırmaq.
* Müştəri tranzaksiyalarına təsir edən makro-iqtisadi, təqvim və hava şəraiti faktorlarını statistik testlərlə araşdırmaq.
* Kredit müraciətlərində rədd cavabı alan müştərilərin Churn riski ilə əlaqəsini təhlil etmək.
* Disbalanslı data mühitində biznes maraqlarına uyğun optimal decision threshold (qərar həddi) təyin etmək.
* Filiallar, kredit satışı və tranzaksiya dinamikasını Power BI dashboard-ları vasitəsilə vizuallaşdırmaq.
* Streamlit üzərində bank menecerləri üçün avtomatik **AI Risk Consultant Engine** (Retention Plan) generatoru təqdim etmək.

---

## 📊 Əsas KPI-lar (Key Performance Indicators)

<p align="center">
  <img src="images/dashboard.png" alt="Power BI Customer Churn Analytics Dashboard" width="100%" />
</p>

| İstiqamət | KPI-lar | Biznes Məqsədi |
| --- | --- | --- |
| **Kredit Proqnozu (ML & Streamlit)** | Proqnozlaşdırılan kredit sayı, filiallar üzrə gözlənilən kredit tələbi | Kredit tələbatını və satış həcmini öncədən planlaşdırmaq |
| **Müştəri İtkisi (Power BI)** | Churn Rate (%), Risk altında olan müştəri sayı, Retention Rate (%) | Müştəri itkisini izləmək və riskli müştəriləri vaxtında tutmaq |
| **Kredit Müraciətləri (Power BI)** | Approval Rate (%), Rejection Rate (%), Conversion Rate (%) | Kredit satışındakı dar boğazları və rədd olunma səbəblərini müəyyən etmək |
| **Müştəri Davranışı (Statistika)** | Gündəlik tranzaksiya sayı/məbləği (AZN), Average Ticket (AZN), Bayram və Maaş dövrü aktivlik fərqi (%) | Müştərinin maliyyə ritmini və xərcləmə vərdişlərini qiymətləndirmək |

---

## 🛠️ İstifadə Olunan Texnologiyalar

| Texnologiya | İstifadə Məqsədi |
| --- | --- |
| **Python (3.14)** | Məlumatların emalı, təhlili, pipeline arxitekturası və modelləşdirmə |
| **Pandas & NumPy** | Data manipulyasiyası, valyuta çevrilmələri, aqreqasiya və təmizləmə |
| **SQL Server** | Məlumatların Medallion arxitekturası (Bronze-Silver-Gold) üzrə saxlanılması |
| **Jupyter Notebook** | Exploratory Data Analysis (EDA) və statistik təhlillərin sənədləşdirilməsi |
| **SciPy & Statsmodels** | Hipotez testləri (Welch t-test, Shapiro-Wilk, Spearman Correlation, Linear Regression) |
| **Scikit-Learn** | ML modellərinin qurulması, ColumnTransformer, Pipeline və Threshold Optimization |
| **Power BI Desktop** | İcraçı rəhbərlik üçün interaktiv vizuallaşdırma və biznes dashboard-ları |
| **Streamlit** | Canlı interaktiv veb-portal və AI Risk Consultant mühərrikinin təqdim olunması |
| **Joblib** | ML modelinin və optimal biznes həddinin (`.pkl`) seriallaşdırılması |
| **Git & GitHub** | Versiyaların idarə edilməsi və Streamlit Cloud avtomatik deployment (CI/CD) |

---

## 📂 Məlumat Mənbələri

### 1. Bank daxili datasetlər (2026-cı il yanvar–iyun)

* **Customers (5,000 müştəri):** Yaş, cinsiyyət, şəhər, hesabdakı balans, illik gəlir, kredit skoru, istifadə etdiyi məhsul sayı və Churn statusu.
* **Loans (6,876 müraciət):** Kredit ID-si, müştəri ID-si, müraciət məbləği, statusu (*Təsdiqləndi / Rədd edildi*) və rədd səbəbləri.
* **Transactions (77,396 tranzaksiya):** Əməliyyat ID-si, məbləğ, valyuta (AZN, USD, EUR), əməliyyat tarixi və bayram günü göstəricisi (`is_holiday`).

### 2. Xarici zənginləşdirmə data mənbələri (External APIs)

* **Open-Meteo API:** Şəhərlər üzrə tarixi hava temperaturu və meteoroloji göstəricilər.
* **Frankfurter API:** USD/AZN və EUR/AZN valyuta məzənnələrinin dinamik tarixçəsi.
* **Calendar Reference:** İş, həftəsonu, bayram və ehtimal olunan maaş günləri haqqında təqvim məlumatları.

---

## 🔄 Layihənin İş Mərhələləri

<p align="center">
  <img src="images/project_workflow.png" alt="End-to-End Data Analytics Workflow" width="100%" />
</p>

### 1. Data Engineering Və Məlumatların Hazırlanması

* Relasiyalı verilənlər bazasındakı dağınıq cədvəllər `customer_id` açarı üzrə tək müştəri oxuna (1 Row Per Customer) gətirilmişdir.
* Foreign currency (USD, EUR) tranzaksiyaları dinamik məzənnə ilə vahid AZN ekvivalentinə çevrilmişdir.
* Müştəri narazılığını ölçmək üçün rədd edilmiş kredit sayı (`rejected_loan_count`) və orta xərcləmə məbləğləri yeni əlamət (Feature Engineering) kimi yaradılmışdır.



### 3. Exploratory Data Analysis (EDA)

* Müştərilərin 20.16%-nin bankı tərk etdiyi (Churn Rate) müəyyən edilmişdir.
* Hesab balansı sıfıra yaxın olan və kredit müraciəti rədd edilən müştərilərdə Churn riskinin kəskin yüksəldiyi müşahidə olunmuşdur.
* Yaş və xərcləmə meylləri üzrə paylanmalar (distributions) və kənar qiymətlər (outliers) təhlil edilmişdir.

### 4. Statistik Təhlil Və Hipotez Testləri

* **Bayram Günləri Təsiri:** İş günlərinə nisbətən bayram günlərində tranzaksiya məbləği 33% aşağıdır. Lakin tranzaksiya sayındakı fərq statistik əhəmiyyətlilik həddinə çatmamışdır ($p > 0.05$).
* **Maaş Dövrü Təsiri:** Ehtimal olunan maaş günlərində tranzaksiya sayı **28.4%**, tranzaksiya məbləği isə **25.4% yüksəkdir**. Hər iki fərq statistik olaraq tam əhəmiyyətlidir ($p < 0.01$).
* **Valyuta Məzənnəsi (USD/EUR):** EUR kursu artdıqda tranzaksiya həcmi arasında zəif mənfi korrelyasiya müşahidə olunmuşdur.
* **Hava Temperaturu Təsiri:** Reqressiya modelinə mövsümilik (aylar) əlavə edildikdə temperaturun birbaşa effekti statistik əhəmiyyətini itirmişdir ($p > 0.05$).

### 5. Feature Engineering

* `total_trans_count` & `total_trans_amount`: Aktivlik və həcm göstəriciləri.
* `avg_trans_amount`: Bir dəfəyə xərclənən orta səbət məbləği.
* `holiday_trans_ratio`: Bayram günlərindəki xərcləmə payı.
* `rejected_loan_count`: Bankdan narazılıq indikatoru.

### 6. Machine Learning Və Biznes Həddinin (Threshold) Optimallaşdırılması

Müştəri itkisi ikili təsnifat (Binary Classification) məsələsi kimi modelləşdirilmişdir:

* **Hədəf dəyişən (`churned`):** `1` — Müştəri bankı tərk edir, `0` — Bankda qalır.
* **Data Leakage-Free:** Transformation addımları (`StandardScaler`, `OneHotEncoder`) yalnız `Train` dəstinə fit olunmuşdur.
* **Class Imbalance:** Random Forest modelində `class_weight='balanced'` parametrindən istifadə edilmişdir.
* **Threshold Tuning ($0.50 \rightarrow 0.35$):** Bank üçün gedəcək müştərini qaçırmaq (False Negative) daha zərərli olduğu üçün decision threshold **$0.35$-ə endirilmiş** və gedəcək müştəriləri tutma nisbəti (**Recall**) **78.5%**-ə yüksəldilmişdir.

---

## 📊 İlkin Analitik Nəticələr

* **ROC-AUC Balı:** `0.8410` (Modelin riski ayırt etmə qabiliyyəti yüksəkdir).
* **Recall (Gedənləri Tutma Faizi):** `78.5%` (Real gedəcək müştərilərin böyük əksəriyyəti öncədən təyin edilir).
* **Precision:** `52.3%` (Hədəflənən retention kampaniyalarının dəqiqliyi).
* **Maaş Günləri Aktivliyi:** Maaş günlərində kart əməliyyatlarının həcmi statistik əhəmiyyətli dərəcədə artır ($p < 0.01$).

---

## 📊 Biznes Insight-ları və Tövsiyələr

### 1. Müştəri İtkisi (Churn) & Balans Riski 📉

**Insight:**

* Müştərilərin 20.16%-i bankı tərk edir. Hesab balansı kritik həddən (2,000 AZN) aşağı olan müştərilərdə Churn meyli 3 dəfə yüksəkdir.

**Biznes Tövsiyələri:**

* Balansı düşən müştərilərə avtomatik +0.5% dərəcəli depozit hesabı və ya pulsuz kart xidməti təklif etmək.
* Müştəri hesabında passivlik yarandıqda stimullaşdırıcı kəşbek kampaniyaları işə salmaq.

### 2. Kredit Müraciətləri Narazılığı & Rədd Səbəbləri ⚠️

**Insight:**

* Kredit müraciəti rədd edilən müştərilər bankdan incəyərək hesablarını bağlamağa daha meyllidir (`rejected_loan_count` Top 10 Churn faktorları arasındadır).

**Biznes Tövsiyələri:**

* Rədd cavabı alan müştəriyə dərhal imtina vermək əvəzinə, daha kiçik həcmli və ya girovlu yumşaq alternativ kredit məhsulları təklif etmək.
* Kredit müraciəti rədd edilən riskli müştəriləri CRM sistemində xüsusi izləməyə götürmək.

### 3. Tranzaksiya Aktivliyi (Maaş Və Bayram Dövrü) 💰

**Insight:**

* Maaş günlərində tranzaksiya həcmi 28.4% artır, bayram günlərində isə əməliyyatlar azalır.

**Biznes Tövsiyələri:**

* Marketing bildirişlərini və kredit təkliflərini məhz maaş dövründən 1-2 gün əvvəl göndərmək.
* Bayram günlərində ticarət tərəfdaşları ilə birlikdə xüsusi bədəlli kampaniyalar keçirmək.

### 4. Proqnozlaşdırıcı AI Və Qərarvermə (AI Risk Consultant Engine) 🤖

**Insight:**

* Streamlit portala inteqrasiya edilmiş AI mühərriki müştərinin risk profilini anlıq təhlil edərək avtomatik **Retention Plan** yaradır.

**Biznes Tövsiyələri:**

* Filial menecerlərinin gündəlik iş prosesinə AI Risk Konsultantının tövsiyələrini inteqrasiya etmək.
* Power BI dashboard-ları vasitəsilə filiallar üzrə riskli müştəri siyahılarını canlı izləmək.

---

## 🎯 Gözlənilən Biznes Faydaları

| İstiqamət | Gözlənilən Fayda |
| --- | --- |
| **Müştəri Retention** | Gedəcək müştərilərin 78.5%-ni öncədən müəyyən edərək saxlamaq |
| **Maliyyə Səmərəliliyi** | Yeni müştəri cəlb etmə xərclərinə (CAC) 5 dəfəyə qədər qənaət etmək |
| **Kredit Satışı** | Rədd edilmiş müraciətləri alternativ məhsullara yönəldərək konversiyanı artırmaq |
| **Əməliyyat Effektivliyi** | Filial menecerlərinin AI tövsiyələri ilə daha sürətli qərar verməsini təmin etmək |
| **Data-Driven Qərarlar** | Subyektiv mülahizələr əvəzinə statistik və ML modellərinə əsaslanmaq |

---