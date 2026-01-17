import { getAllRooms, getRoom } from "@/features/rooms/bindings/api";
import { notFound } from "next/navigation";
import Link from "next/link";

export async function generateStaticParams() {
  const rooms = await getAllRooms();
  return rooms.map((room) => ({
    id: room.id,
  }));
}

export default async function RoomPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const room = await getRoom(id);

  if (!room) {
    notFound();
  }

  return (
    <main className="container" style={{ padding: "4rem 1.5rem" }}>
      <Link
        href="/"
        style={{
          fontSize: "0.9rem",
          color: "var(--text)",
          marginBottom: "2rem",
          display: "inline-block",
        }}
      >
        &larr; Back to Home
      </Link>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
          gap: "4rem",
          alignItems: "start",
        }}
      >
        <div>
          <div
            style={{
              height: "400px",
              backgroundColor: "#eee",
              borderRadius: "8px",
              overflow: "hidden",
              marginBottom: "2rem",
              position: "relative",
            }}
          >
            {room.images && room.images[0] ? (
              <img
                src={room.images[0]}
                alt={room.type}
                style={{ width: "100%", height: "100%", objectFit: "cover" }}
              />
            ) : (
              <div
                style={{
                  width: "100%",
                  height: "100%",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "#999",
                }}
              >
                {room.type} Image Placeholder
              </div>
            )}
          </div>
          <h1 style={{ fontSize: "3rem", marginBottom: "1rem" }}>
            {room.type}
          </h1>
          <p
            style={{ fontSize: "1.25rem", color: "#666", marginBottom: "2rem" }}
          >
            {room.features.view || "Standard View"} •{" "}
            {room.features.floor || "Floor info n/a"}
          </p>

          <h2 style={{ fontSize: "1.5rem", marginBottom: "1rem" }}>
            Description
          </h2>
          <p style={{ lineHeight: 1.8, marginBottom: "2rem" }}>
            {room.description}
          </p>

          <h3 style={{ fontSize: "1.25rem", marginBottom: "1rem" }}>
            Amenity Highlights
          </h3>
          <ul
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 1fr",
              gap: "0.5rem",
              paddingLeft: "1rem",
            }}
          >
            <li style={{ color: "#555" }}>
              • Capacity: {room.capacity.description}
            </li>
            {room.features.terrace && (
              <li style={{ color: "#555" }}>
                • Terrace: {room.features.terrace}
              </li>
            )}
            {room.features.amenities?.map((amenity) => (
              <li key={amenity} style={{ color: "#555" }}>
                • {amenity}
              </li>
            ))}
          </ul>
          <div style={{ marginTop: "2rem" }}>
            <strong>Beds:</strong> {room.beds.join(", ")}
          </div>
        </div>

        <div
          style={{
            position: "sticky",
            top: "100px",
            padding: "2rem",
            border: "1px solid var(--border)",
            borderRadius: "8px",
            backgroundColor: "var(--surface)",
            boxShadow: "0 4px 12px rgba(0,0,0,0.05)",
          }}
        >
          <h3 style={{ marginBottom: "1rem" }}>Reserve this Room</h3>
          <div
            style={{
              fontSize: "2.5rem",
              color: "var(--accent)",
              fontWeight: "bold",
              marginBottom: "0.5rem",
            }}
          >
            €{room.price.amount}
          </div>
          <div style={{ color: "#666", marginBottom: "2rem" }}>
            per night / {room.capacity.description}
          </div>

          <button
            className="btn"
            style={{ width: "100%", textAlign: "center", cursor: "pointer" }}
          >
            Check Availability
          </button>
          <p
            style={{
              fontSize: "0.8rem",
              color: "#999",
              marginTop: "1rem",
              textAlign: "center",
            }}
          >
            Best Price Guaranteed
          </p>
        </div>
      </div>
    </main>
  );
}
