import facilitiesData from "@/data/facilities.json";
import { Facility } from "../model/schema";

export const getFacilities = async (): Promise<Facility[]> => {
  return facilitiesData as Facility[];
};

export const getFacility = async (id: string): Promise<Facility | null> => {
  const facility = facilitiesData.find((f) => f.id === id);
  return facility ? (facility as Facility) : null;
};
