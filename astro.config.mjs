import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	// IMPORTANT: Do NOT configure Astro's own `i18n` here.
	// Starlight will handle i18n based on its `locales` config.
	integrations: [
		starlight({
			title: 'OpenCV Documentation',
			favicon: '/favicon.ico',
			logo: {
				light: './src/assets/robomous-logo-banner.svg',
				dark: './src/assets/robomous-logo-banner-white.png',
				alt: 'Robomous Logo'
			},
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/Robomous/unofficial-opencv-docs'
				}
			],
			customCss: ['./src/styles/custom-colors.css'],
			expressiveCode: {
				defaultProps: {
					overridesByLang: {
						// Code editor languages: explicitly set language names as titles
						// Terminal languages (bash, sh, etc.) should NOT have titles - they show as terminal windows
						'python': { title: 'Python' },
						'py': { title: 'Python' },
					},
				},
			},
			locales: {
				// English (default) content files are at `src/content/docs/...` (root)
				// Using 'root' as the key makes it serve at / instead of /en/
				root: {
					label: 'English',
					lang: 'en-US'
				},
				// Spanish content files will live under `src/content/docs/es/...`
				es: {
					label: 'Español',
					lang: 'es-MX'
				}
			},
			sidebar: [
				{
					label: 'Getting Started',
					translations: {
						es: 'Comenzando'
					},
					// Starlight must autogenerate from the `getting-started` directory.
					autogenerate: {
						directory: 'getting-started'
					}
				},
				{
					label: 'Guides',
					translations: {
						es: 'Guías'
					},
					autogenerate: {
						directory: 'guides'
					}
				}
			]
		})
	]
});
