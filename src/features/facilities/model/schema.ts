import { z } from "zod";

export const FacilitySchema = z.object({
  id: z.string(), // "pool", "spa"
  name: z.string(), // "Piscine"
  description: z.string(), // "La piscine de Villa Thaifa..."
  features: z
    .array(
      z.object({
        label: z.string(),
        value: z.string(), // "A confirmer" mostly for now
      }),
    )
    .optional(),
  images: z.array(z.string()).optional(),
});

export type Facility = z.infer<typeof FacilitySchema>;
