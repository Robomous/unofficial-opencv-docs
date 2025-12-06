<img src="https://robomous.ai/images/layout/robomous-banner.svg" alt="Robomous.ai" width=300 />

-----------------

Documentation focused on OpenCV for Python. An open source project by Robomous for the community.

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

## 🚀 Project Structure

```
.
├── public/
├── src/
│   ├── assets/
│   │   ├── robomous-logo-banner.svg
│   │   └── houston.webp
│   ├── content/
│   │   └── docs/
│   │       ├── index.md              # English homepage
│   │       ├── getting-started/     # English "Getting Started" section
│   │       │   ├── what-is-opencv.mdx
│   │       │   ├── installation.mdx
│   │       │   └── quick-start.mdx
│   │       ├── guides/               # English "Guides" section
│   │       │   ├── index.md
│   │       │   ├── core-concepts/     # Core Concepts subsection
│   │       │   │   └── introduction-to-computer-vision.mdx
│   │       │   └── image-preprocessing.md
│   │       └── es/                   # Spanish content
│   │           ├── index.md          # Spanish homepage
│   │           ├── getting-started/
│   │           │   ├── what-is-opencv.mdx
│   │           │   ├── installation.mdx
│   │           │   └── quick-start.mdx
│   │           └── guides/
│   │               ├── index.md
│   │               ├── core-concepts/     # Core Concepts subsection
│   │               │   └── introduction-to-computer-vision.mdx
│   │               └── image-preprocessing.md
│   ├── content.config.ts
│   └── styles/
│       └── custom-colors.css
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

## 📝 Content Organization

- **English content** is located directly in `src/content/docs/` (root level)
- **Spanish content** is located in `src/content/docs/es/`
- Starlight automatically generates routes based on the file structure
- English content is served at root paths (e.g., `/`, `/start-here/getting-started/`)
- Spanish content is served under `/es/` (e.g., `/es/`, `/es/start-here/getting-started/`)

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 🚀 Deployment

For AWS Amplify deployment:
- **Build command**: `npm run build`
- **Output directory**: `dist`

## 👀 Want to learn more?

Check out [Starlight's docs](https://starlight.astro.build/), read [the Astro documentation](https://docs.astro.build), or jump into the [Astro Discord server](https://astro.build/chat).

---

This project is a contribution from [Robomous](https://robomous.ai) to the open-source community, providing modern and up-to-date OpenCV documentation in an accessible format.
