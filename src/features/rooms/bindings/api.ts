// src/features/rooms/bindings/api.ts

import roomsData from "@/data/rooms.json";
import { Room } from "../model/schema";

export const getRoom = async (id: string): Promise<Room | null> => {
  const room = roomsData.find((r) => r.id === id);
  return room ? (room as Room) : null;
};

export const getAllRooms = async (): Promise<Room[]> => {
  return roomsData as Room[];
};
