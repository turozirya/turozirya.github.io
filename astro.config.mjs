// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://turozirya.github.io',
	integrations: [
		starlight({
			title: 'kod_turozirya',
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
			],
			customCss: ['./src/styles/makecode-renkleri.css'],
			components: {
				PageTitle: './src/components/KonuBasligi.astro',
			},
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
