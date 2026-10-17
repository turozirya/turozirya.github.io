import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Konu sayfalarının başındaki ek bilgiler (yol haritasındaki alanlar).
// "baslik" yerine Starlight'ın zorunlu "title" alanı kullanılır.
// Bağlantı alanları boş bırakılabilir (makecode: "").
const baglanti = z.union([z.string().url(), z.literal('')]).optional();

const konuBilgileri = z.object({
	hafta: z.number().optional(),
	seviye: z.string().optional(),
	sure: z.string().optional(),
	kazanimlar: z.array(z.string()).optional(),
	makecode: baglanti,
	video: baglanti,
});

export const collections = {
	docs: defineCollection({ loader: docsLoader(), schema: docsSchema({ extend: konuBilgileri }) }),
};
