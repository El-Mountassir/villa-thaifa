import { z } from "zod";

export const PriceSchema = z.object({
  amount: z.number(),
  currency: z.string(),
});

export const FeaturesSchema = z.object({
  view: z.string().optional(),
  floor: z.string().optional(),
  area: z.string().optional(),
  terrace: z.string().optional(),
  amenities: z.array(z.string()).optional(),
});

export const RoomSchema = z.object({
  id: z.string(),
  number: z.string(),
  type: z.string(),
  capacity: z.object({
    adults: z.number(),
    children: z.number().optional(),
    description: z.string(),
  }),
  beds: z.array(z.string()),
  price: PriceSchema,
  features: FeaturesSchema,
  description: z.string(),
  images: z.array(z.string()).optional(), // Added for Data Rescue
});

export type Room = z.infer<typeof RoomSchema>;
