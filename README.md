# 🛰️ Satellite Service Finder (Pro Edition)

![License](https://img.shields.io/github/license/username/repo)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![PostGIS](https://img.shields.io/badge/PostGIS-Spatial--DB-blue)
![OSM](https://img.shields.io/badge/OpenStreetMap-Data-orange)

نظام معلومات جغرافي (**GIS**) متطور مبني باستخدام **GeoDjango** و **PostGIS**. يعتمد التطبيق على بيانات **OpenStreetMap (OSM)** الضخمة لتحديد الخدمات القريبة (مستشفيات، مدارس، مطاعم) وعرضها على خريطة قمر صناعي هجينة مع توفير ميزة حساب المسارات.

---

## 🚀 المميزات الرئيسية (Core Features)

- **OSM Integration:** معالجة واستيراد ملايين النقاط الجغرافية (POIs) من ملفات PBF.
- **Spatial Searching:** البحث الذكي في نطاق 5 كم باستخدام دوال PostGIS المكانية.
- **Satellite Hybrid Map:** عرض صور الأقمار الصناعية من Esri مع طبقة أسماء الشوارع الشفافة لسهولة التوجيه.
- **One-Click Routing:** حساب مسارات القيادة فورياً بين موقع المستخدم والمرفق المختار.
- **Responsive Sidebar:** قائمة جانبية تفاعلية تعرض النتائج مرتبة حسب المسافة.

---

## 🛠️ البنية التقنية (Tech Stack)

| الطبقة | التقنية المستخدمة |
| :--- | :--- |
| **Backend** | Python / Django / GeoDjango |
| **Database** | PostgreSQL + PostGIS |
| **Frontend** | Leaflet.js / Leaflet Routing Machine |
| **Data Pipeline** | osm2pgsql (لتحويل بيانات PBF إلى SQL) |
| **Map Source** | Esri World Imagery / CartoDB Labels |

---

## ⚙️ إعداد نظام البيانات (Data Pipeline Setup)

يعتمد هذا المشروع على سحب البيانات من ملفات **OpenStreetMap PBF**.

### 1. استيراد البيانات باستخدام `osm2pgsql`
بعد تحميل ملف المنطقة المطلوبة (مثلاً من Geofabrik)، قم بتنفيذ الأمر التالي لاستيراد البيانات إلى قاعدة بيانات PostGIS:

```bash
osm2pgsql -d your_db_name -U your_user -H localhost --slim --hstore map_data.osm.pbf
