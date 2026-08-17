# Frontend Deployment Notes (Vercel / Netlify)

The UI dashboard located in the `frontend/` directory is designed to be hosted on static hosting platforms like Vercel or Netlify.

### Vercel Deployment Steps:
1. Import the GitHub repository into Vercel.
2. Set the **Root Directory** to `frontend/`.
3. **Build Command:** Leave empty (Vanilla HTML/CSS/JS).
4. **Output Directory:** Leave empty.

*Note for Production:* Before deploying, ensure that the API fetch URL in `frontend/script.js` is updated from `http://localhost:8000` to the live URL of your deployed backend.