import { z } from "zod";

export const RoomSchema = z.object({
  id: z.string(), // "01"
  number: z.string(), // "01"
  type: z.string(), // "Deluxe Triple Room"
  capacity: z.object({
    adults: z.number(), // 3
    children: z.number().optional(),
    description: z.string(), // "3 personnes"
  }),
  beds: z.array(z.string()), // ["1 lit king", "1 canape-lit"]
  price: z.object({
    amount: z.number(), // 200
    currency: z.literal("EUR"),
    bookingPrice: z.number().optional(),
  }),
  features: z.object({
    view: z.string().optional(), // "Jardin"
    floor: z.string().optional(), // "Rez-de-chaussée"
    area: z.string().optional(), // "82 m2"
    terrace: z.string().optional(), // "40 m²"
    amenities: z.array(z.string()).optional(), // ["Cheminée", "Salon"]
  }),
  description: z.string().optional(),
  images: z.array(z.string()).optional(),
});

export type Room = z.infer<typeof RoomSchema>;
