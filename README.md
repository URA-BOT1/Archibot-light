# Archibot-light Setup Guide

This repository contains the source code for **Archibot-light**. Below are
instructions for running the project locally and deploying it to the cloud.

## Local Development

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd Archibot-light
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Create a `.env` file** with the required environment variables. Common
   variables include:

   - `DATABASE_URL` &ndash; database connection string
   - `OPENAI_API_KEY` &ndash; API key for OpenAI services

   Adjust these to match your environment.

4. **Run the backend locally**

   ```bash
   npm run dev
   ```

   Once running, you can check the health endpoint:

   ```bash
   curl http://localhost:3000/health
   ```

## Deploying the Backend to Railway

1. **Install the Railway CLI**

   ```bash
   npm install -g railway
   ```

2. **Login and link your project**

   ```bash
   railway login
   railway init
   ```

3. **Set environment variables** in the Railway dashboard or via CLI:

   ```bash
   railway variables set DATABASE_URL="..." OPENAI_API_KEY="..."
   ```

4. **Deploy**

   ```bash
   railway up
   ```

## Deploying the Frontend to Vercel

1. **Install the Vercel CLI**

   ```bash
   npm install -g vercel
   ```

2. **Login and link your project**

   ```bash
   vercel login
   vercel link
   ```

3. **Add environment variables** through the Vercel dashboard or by running:

   ```bash
   vercel env add DATABASE_URL production
   vercel env add OPENAI_API_KEY production
   ```

4. **Deploy**

   ```bash
   vercel --prod
   ```

## Sample Health Check

After deploying, you can confirm the backend is running by executing:

```bash
curl https://<your-railway-app>.railway.app/health
```

A successful response confirms that the backend is up and responding.

