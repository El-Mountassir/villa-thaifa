import { getAllRooms } from "@/features/rooms/bindings/api";
import { getFacilities } from "@/features/facilities/bindings/api";

export default async function Home() {
  const rooms = await getAllRooms();
  const facilities = await getFacilities();

  return (
    <main className="min-h-screen p-24">
      <h1 style={{ marginBottom: "2rem" }}>
        Villa Thaifa - Digital Experience
      </h1>

      <section style={{ marginBottom: "4rem" }}>
        <h2
          style={{
            fontSize: "1.5rem",
            marginBottom: "1rem",
            borderBottom: "2px solid #d4a373",
            paddingBottom: "0.5rem",
          }}
        >
          Accommodations
        </h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
            gap: "1.5rem",
          }}
        >
          {rooms.map((room) => (
            <div
              key={room.id}
              style={{
                padding: "1.5rem",
                border: "1px solid #ccc",
                borderRadius: "8px",
              }}
            >
              <h3 style={{ fontSize: "1.25rem", marginBottom: "0.5rem" }}>
                {room.number} - {room.type}
              </h3>
              <p
                style={{
                  color: "#666",
                  marginBottom: "1rem",
                  fontSize: "0.9rem",
                }}
              >
                {room.description}
              </p>
              <ul style={{ fontSize: "0.9rem", listStyle: "none", padding: 0 }}>
                <li>
                  <strong>Price:</strong> {room.price.amount}{" "}
                  {room.price.currency}
                </li>
                <li>
                  <strong>Capacity:</strong> {room.capacity.description}
                </li>
                <li>
                  <strong>View:</strong> {room.features.view || "N/A"}
                </li>
              </ul>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2
          style={{
            fontSize: "1.5rem",
            marginBottom: "1rem",
            borderBottom: "2px solid #d4a373",
            paddingBottom: "0.5rem",
          }}
        >
          Facilities
        </h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
            gap: "1.5rem",
          }}
        >
          {facilities.map((facility) => (
            <div
              key={facility.id}
              style={{
                padding: "1.5rem",
                border: "1px solid #eee",
                borderRadius: "8px",
                backgroundColor: "#f9f9f9",
              }}
            >
              <h3 style={{ fontSize: "1.25rem", marginBottom: "0.5rem" }}>
                {facility.name}
              </h3>
              <p
                style={{
                  color: "#666",
                  marginBottom: "1rem",
                  fontSize: "0.9rem",
                }}
              >
                {facility.description}
              </p>
              {facility.features && (
                <ul
                  style={{
                    fontSize: "0.85rem",
                    color: "#555",
                    paddingLeft: "1rem",
                  }}
                >
                  {facility.features.map((feat, idx) => (
                    <li key={idx}>
                      <strong>{feat.label}:</strong> {feat.value}
                    </li>
                  ))}
                </ul>
              )}
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
