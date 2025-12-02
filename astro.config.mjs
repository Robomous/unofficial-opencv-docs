import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	// IMPORTANT: Do NOT configure Astro's own `i18n` here.
	// Starlight will handle i18n based on its `locales` config.
	integrations: [
		starlight({
			title: 'Unofficial OpenCV Documentation',
			favicon: '/favicon.ico',
			logo: {
				src: './src/assets/robomous-logo-banner.svg',
				alt: 'Robomous Logo'
			},
			customCss: ['./src/styles/custom-colors.css'],
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
					label: 'Start Here',
					translations: {
						es: 'Comienza aquí'
					},
					// Starlight must autogenerate from the `start-here` directory.
					autogenerate: {
						directory: 'start-here'
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
