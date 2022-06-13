## 🚀 Usage

Initialize server local

```
uvicorn api.main:app --reload
```

Change after **token** for same token from /api/main.py
```js
fetch("https://examplename.vercel.app/mailjet", {
  method: "POST",
  body: JSON.stringify({
    from_email: "github@alexanderiscoding.com",
    from_name: "Alexanderiscoding",
    to_email: "github@alexanderiscoding.com",
    to_name: "Alexanderiscoding",
    subject_email: "Saudações da Mailjet.",
    content_email:  "<strong>Bem-vindo(a) à <a href='https://www.mailjet.com/'>Mailjet</a>!</strong>",
    token: "a8919de3b6f0f44a8799c8854deb3e43",
  }),
});
```
```js
fetch("https://examplename.vercel.app/sendgrid", {
  method: "POST",
  body: JSON.stringify({
    from_email: "github@alexanderiscoding.com",
    from_name: "Alexanderiscoding",
    to_email: "github@alexanderiscoding.com",
    to_name: "Alexanderiscoding",
    subject_email: "Saudações da Mailjet.",
    content_email:  "<strong>and easy to do anywhere, even with Python</strong>",
    token: "a8919de3b6f0f44a8799c8854deb3e43",
  }),
});
```
