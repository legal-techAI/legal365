# Cloud Demo V108

## تجربة محلية
```bash
docker compose up -d --build
```
ثم افتح `http://localhost:8080`.

## الحسابات التجريبية
يمكن اختيار أي دور من شاشة الدخول:
- المدير العام
- المستشار العام
- مدير إدارة / وكيل
- مراجع مساءلة

كلمة المرور التجريبية:
`demo123`

## نشر عام للعرض
يمكن نشر الـ frontend على Vercel/Netlify، والـ API على Render/Railway/Azure/AWS.
لبيئة مؤسسية حقيقية يفضل Azure/AWS مع SSO/MFA وPostgreSQL وSecret Manager وWAF.

هذه النسخة Demo وليست إنتاجًا ولا تحتوي بيانات قانونية حقيقية.
