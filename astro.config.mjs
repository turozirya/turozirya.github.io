// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://turozirya.github.io',
	integrations: [
		starlight({
			title: 'kod_turozirya',
			logo: { src: './src/assets/logo.svg', alt: '' },
			description: 'Ortaokul robotik kodlama kulübü için micro:bit dersleri',
			// Raspberry Pi 5 çekirdeği (16 KB bellek sayfası) Pagefind aramasını çalıştıramıyor;
			// Pi'de "npm run build:pi" ile aramasız derlenir. Yayın sunucusunda arama çalışır.
			pagefind: process.env.ARAMA !== 'kapali',
			defaultLocale: 'root',
			locales: {
				root: { label: 'Türkçe', lang: 'tr' },
			},
			social: [
				{ icon: 'youtube', label: 'YouTube', href: 'https://www.youtube.com/@kod_turozirya' },
				{ icon: 'instagram', label: 'Instagram', href: 'https://www.instagram.com/kod_turozirya' },
			],
			customCss: ['./src/styles/makecode-renkleri.css'],
			components: {
				PageTitle: './src/components/KonuBasligi.astro',
				SiteTitle: './src/components/SiteBasligi.astro',
			},
			head: [
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
				{
					tag: 'link',
					attrs: {
						rel: 'stylesheet',
						href: 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@800&family=Lexend:wght@400;600;700&display=swap',
					},
				},
			],
			sidebar: [
				{
					label: 'micro:bit ile Robotik Kodlama',
					items: [
						{ label: 'Ders tanıtımı', slug: 'dersler/microbit' },
						{
							label: 'Blok dönemi (1–18. hafta)',
							items: [{ autogenerate: { directory: 'dersler/microbit/blok' } }],
						},
						{
							label: 'Metin dönemi (19–28. hafta)',
							collapsed: true,
							items: [{ autogenerate: { directory: 'dersler/microbit/metin' } }],
						},
					],
				},
			],
		}),
	],
});
