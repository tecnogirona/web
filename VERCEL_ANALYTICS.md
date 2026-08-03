# Vercel Web Analytics - Setup Guide

## Overview

This project has been configured with Vercel Web Analytics to provide privacy-friendly, real-time traffic insights.

## Implementation

### What Was Added

1. **Analytics Script Tag**: Added to all 27 HTML files in the project
   ```html
   <script defer src="/_vercel/insights/script.js"></script>
   ```
   - Located in the `<head>` section of each HTML file
   - Uses `defer` attribute for optimal loading performance
   - Loads asynchronously without blocking page rendering

2. **Vercel Configuration**: Created `vercel.json` with basic deployment settings
   ```json
   {
     "buildCommand": null,
     "outputDirectory": ".",
     "cleanUrls": true,
     "trailingSlash": false
   }
   ```

### Files Modified

All HTML files in the root directory now include the Vercel Analytics script:
- index.html
- All service pages (reparacion-*.html, etc.)
- Landing pages
- Utility pages (404.html, form.html, etc.)
- Legal pages (politica-privacidad.html, terminos-condiciones.html)

## How to Enable Analytics

### Step 1: Deploy to Vercel

The analytics will only work when the site is deployed to Vercel. To deploy:

```bash
# Install Vercel CLI (if not already installed)
npm i -g vercel

# Deploy the project
vercel
```

Follow the prompts to link the project to your Vercel account.

### Step 2: Enable Analytics in Vercel Dashboard

1. Go to your project in the Vercel Dashboard
2. Navigate to the **Analytics** tab
3. Click **Enable Web Analytics**
4. Deploy your site (the script will automatically start tracking)

### Step 3: Verify Installation

After deployment:
1. Visit your deployed site
2. Open browser DevTools (F12)
3. Go to the **Network** tab
4. Look for requests to `/_vercel/insights/`
5. You should see successful requests indicating analytics is working

## Features

- **Privacy-Friendly**: First-party analytics with no cookies or personal data collection
- **Real-Time**: See visitor data in real-time in the Vercel Dashboard
- **Lightweight**: Minimal performance impact with deferred loading
- **Automatic**: No additional configuration needed once deployed

## Important Notes

### Current Deployment

According to `STACK.md`, the DNS for `tecnogirona.es` currently points to an external nginx server (213.158.94.183), not Vercel/GitHub Pages.

**To use Vercel Analytics, you'll need to either:**

1. **Option A - Deploy to Vercel (Recommended)**:
   - Deploy the site to Vercel
   - Update DNS to point to Vercel's servers
   - Analytics will work automatically

2. **Option B - Use Vercel as Primary + Nginx as Backup**:
   - Deploy to Vercel for analytics and CDN benefits
   - Keep nginx as failover if needed

### Migration Path

If you decide to migrate to Vercel:
1. Deploy the project to Vercel using the Vercel CLI or GitHub integration
2. Test the Vercel deployment URL
3. Update DNS records for tecnogirona.es to point to Vercel
4. Enable analytics in the Vercel dashboard

## Documentation References

- [Vercel Analytics Quickstart](https://vercel.com/docs/analytics/quickstart)
- [Vercel Analytics Package Documentation](https://vercel.com/docs/analytics/package)
- [Deploying Static Sites to Vercel](https://vercel.com/docs/deployments/overview)

## Support

For issues or questions about Vercel Analytics:
- Visit [Vercel Documentation](https://vercel.com/docs)
- Check [Vercel Community](https://github.com/vercel/vercel/discussions)
