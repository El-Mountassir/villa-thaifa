---
phase: 01-operational-urgency
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - photos/01/
  - photos/02/
  - photos/03/
  - photos/04/
  - photos/05/
  - photos/06/
  - photos/07/
  - photos/08/
  - photos/09/
  - photos/10/
  - photos/11/
  - photos/12/
autonomous: true

must_haves:
  truths:
    - "Photos for all 12 rooms exist in organized structure"
    - "Each room directory contains named photos (main.jpg, bathroom.jpg, etc.)"
    - "Room 12 has minimum 5 photos ready for HotelRunner upload"
  artifacts:
    - path: "photos/"
      provides: "Organized photo directory structure for all 12 rooms"
      min_items: 12
    - path: "photos/12/"
      provides: "Room 12 photos for HotelRunner upload (OPS-03)"
      min_items: 5
  key_links:
    - from: "legacy/content_source/facilities/rooms/"
      to: "photos/"
      via: "Copy and rename operation"
      pattern: "12 room directories with named photos"
---

<objective>
Organize all professional room photos into structured directory with naming conventions.

Purpose: Enable efficient photo management and prepare Room 12 photos for HotelRunner upload (OPS-03 dependency). This task can proceed immediately without HotelRunner access.

Output: `photos/{room-id}/` directories with consistently named files for all 12 rooms.
</objective>

<execution_context>
@/home/director/.claude/get-shit-done/workflows/execute-plan.md
@/home/director/.claude/get-shit-done/templates/summary.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md
@.planning/phases/01-operational-urgency/01-RESEARCH.md

Source photos location: legacy/content_source/facilities/rooms/{01-12}/images/
Photo inventory from research: Room 12 has 10 JPEG files (all under 400KB)
</context>

<tasks>

<task type="auto">
  <name>Task 1: Create photo directory structure</name>
  <files>photos/</files>
  <action>
Create the `photos/` directory at project root with 12 room subdirectories:

```bash
mkdir -p photos/{01,02,03,04,05,06,07,08,09,10,11,12}
```

This creates the target structure for organized photos. Each room gets its own directory using the 2-digit room ID format (01-12).
  </action>
  <verify>
```bash
ls -la photos/ | wc -l  # Should show 14 lines (12 dirs + . and ..)
```
  </verify>
  <done>12 room directories exist at photos/01 through photos/12</done>
</task>

<task type="auto">
  <name>Task 2: Copy and organize photos for all rooms</name>
  <files>photos/01/, photos/02/, photos/03/, photos/04/, photos/05/, photos/06/, photos/07/, photos/08/, photos/09/, photos/10/, photos/11/, photos/12/</files>
  <action>
Copy photos from legacy folder and rename with descriptive names for each room.

**Source:** `legacy/content_source/facilities/rooms/{room}/images/*.jpg` or `*.jpeg`

**Naming convention:**
- `main.jpg` - Hero/featured image (first/best photo)
- `bedroom-01.jpg`, `bedroom-02.jpg` - Bed views
- `bathroom.jpg` - Bathroom
- `terrace.jpg` - Outdoor space (if exists)
- `detail-01.jpg`, `detail-02.jpg` - Additional details

**Process for each room:**
1. List photos in legacy folder: `ls legacy/content_source/facilities/rooms/{room}/images/`
2. View first photo to identify content (if needed): `file` or image viewer
3. Copy with descriptive name: `cp legacy/.../uuid.jpeg photos/{room}/main.jpg`
4. Repeat for remaining photos with appropriate names

**Priority:** Complete Room 12 first (needed for OPS-03), then remaining rooms.

**Photo type identification hints:**
- Larger files (~300-400KB) often bedroom/main shots
- Smaller files (~200-280KB) often detail shots
- UUID filenames provide no context - must inspect or use first-come naming

If unable to determine photo content, use sequential naming:
- `photo-01.jpg`, `photo-02.jpg`, etc.
  </action>
  <verify>
```bash
# Verify each room has photos
for room in 01 02 03 04 05 06 07 08 09 10 11 12; do
  echo "Room $room: $(ls photos/$room/*.jpg 2>/dev/null | wc -l) photos"
done

# Verify Room 12 specifically (critical for OPS-03)
ls -la photos/12/
```
  </verify>
  <done>
- All 12 rooms have photos copied and named
- Room 12 has minimum 5 photos ready for HotelRunner upload
- Photos use descriptive naming convention (main.jpg, bathroom.jpg, etc.) or sequential naming
  </done>
</task>

<task type="auto">
  <name>Task 3: Generate photo inventory manifest</name>
  <files>photos/MANIFEST.md</files>
  <action>
Create a manifest file documenting the organized photos:

```markdown
# Photo Manifest

Generated: {date}
Source: legacy/content_source/facilities/rooms/

## Summary

| Room | Photos | Ready for HotelRunner |
|------|--------|----------------------|
| 01   | X      | Yes                  |
| ...  | ...    | ...                  |
| 12   | X      | Yes (OPS-03)         |

## Room Details

### Room 01
- main.jpg - {description if known}
- bathroom.jpg
- ...

### Room 12 (Priority: OPS-03)
- main.jpg
- ...

## Notes

- All photos under 2MB (HotelRunner limit: 2MB)
- Original UUIDs mapped to descriptive names where possible
```
  </action>
  <verify>
```bash
cat photos/MANIFEST.md | head -30
```
  </verify>
  <done>MANIFEST.md exists with complete inventory of all 12 rooms</done>
</task>

</tasks>

<verification>
1. `ls photos/ | wc -l` returns 12 (or 13 with MANIFEST.md)
2. `ls photos/12/ | wc -l` returns at least 5
3. `cat photos/MANIFEST.md` shows all rooms documented
4. No photos exceed 2MB: `find photos/ -size +2M | wc -l` returns 0
</verification>

<success_criteria>
- Photos for all 12 rooms organized in `photos/{room-id}/` structure
- Room 12 has minimum 5 photos ready for OPS-03 (HotelRunner upload)
- MANIFEST.md documents the complete photo inventory
- OPS-04 requirement acceptance criteria met
</success_criteria>

<output>
After completion, create `.planning/phases/01-operational-urgency/01-01-SUMMARY.md` with:
- Files created (photos directories, MANIFEST.md)
- Photo count per room
- Any issues encountered (missing photos, quality concerns)
- Readiness status for OPS-03 (Room 12 upload)
</output>
