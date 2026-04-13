<img src="https://cdn.robomous.ai/public-images/robomous-banner.svg" alt="Robomous.ai" width=300 />

---

Documentation focused on OpenCV for Python. An open source project by Robomous for the community.

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

## 🚀 Project Structure

```
.
├── public/
├── src/
│   ├── assets/
│   │   ├── opencv_logo.svg
│   │   └── opencv_logo_white.svg
│   ├── content/
│   │   └── docs/
│   │       ├── index.mdx              # English homepage
│   │       ├── getting-started/       # "Getting Started" section
│   │       │   ├── what-is-opencv.mdx
│   │       │   ├── installation.mdx
│   │       │   └── quick-start.mdx
│   │       ├── fundamentals/          # "Fundamentals" section
│   │       │   ├── digital-image.mdx
│   │       │   └── introduction-to-computer-vision.mdx
│   │       ├── image-preprocessing/   # "Image Preprocessing" section
│   │       │   └── index.md
│   │       └── es/                    # Spanish content (mirrors English structure)
│   │           ├── index.mdx
│   │           ├── getting-started/
│   │           ├── fundamentals/
│   │           └── image-preprocessing/
│   └── styles/
│       └── custom.css
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

## 📝 Content Organization

- **English content** is located directly in `src/content/docs/` (root level)
- **Spanish content** is located in `src/content/docs/es/`
- Starlight automatically generates routes based on the file structure
- English content is served at root paths (e.g., `/`, `/getting-started/quick-start/`)
- Spanish content is served under `/es/` (e.g., `/es/`, `/es/getting-started/quick-start/`)

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command             | Action                                           |
| :------------------ | :----------------------------------------------- |
| `yarn install`      | Installs dependencies                            |
| `yarn dev`          | Starts local dev server at `localhost:4321`      |
| `yarn build`        | Build your production site to `./dist/`          |
| `yarn preview`      | Preview your build locally, before deploying     |
| `yarn astro ...`    | Run CLI commands like `astro add`, `astro check` |
| `yarn astro --help` | Get help using the Astro CLI                     |

## 🚀 Deployment

For AWS Amplify deployment (configured in `amplify.yml`):

- **Build command**: `yarn build`
- **Output directory**: `dist`

## 👀 Want to learn more?

Check out [Starlight's docs](https://starlight.astro.build/), read [the Astro documentation](https://docs.astro.build), or jump into the [Astro Discord server](https://astro.build/chat).

---

This project is a contribution from [Robomous](https://robomous.ai) to the open-source community, providing modern and up-to-date OpenCV documentation in an accessible format.
