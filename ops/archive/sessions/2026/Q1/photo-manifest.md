# Photo Manifest (Not Up to Date)

Generated: 2026-01-30
Source: legacy/content_source/facilities/rooms/

## Summary

| Room | Photos | Ready for HotelRunner | Notes                |
| ---- | ------ | --------------------- | -------------------- |
| 01   | 9      | No - resize needed    | HDR photos 2.2-2.8MB |
| 02   | 9      | Partial               | Mix of sizes         |
| 03   | 8      | No - resize needed    | HDR photos 2.1-2.6MB |
| 04   | 9      | Partial               | Mix of sizes         |
| 05   | 18     | No - resize needed    | HDR photos 2.1-3.2MB |
| 06   | 11     | No - resize needed    | HDR photos 2.5-3.6MB |
| 07   | 11     | Partial               | Mix of sizes         |
| 08   | 7      | Partial               | Mix of sizes         |
| 09   | 10     | Yes                   | All under 500KB      |
| 10   | 11     | Yes                   | All under 500KB      |
| 11   | 14     | Yes                   | All under 500KB      |
| 12   | 10     | Yes (OPS-03 ready)    | All under 500KB      |

**Total: 127 photos across 12 rooms**

## Room Details

### Room 01

- main.jpg - Professional HDR (2.4MB)
- photo-01.jpg - Professional HDR (2.4MB)
- photo-02.jpg - Professional HDR (2.5MB)
- photo-03.jpg - Professional HDR (2.8MB)
- photo-04.jpg - Professional HDR (2.2MB)
- photo-05.jpg - Professional HDR (1.9MB)
- photo-06.jpg - Professional HDR (1.8MB)
- photo-07.jpg - Professional HDR (1.8MB)
- photo-08.jpg - Professional HDR (1.6MB)

### Room 02

- main.jpg through photo-08.jpg (9 photos)
- Professional HDR photos, various sizes

### Room 03

- main.jpg through photo-07.jpg (8 photos)
- Professional HDR photos 2.1-2.6MB

### Room 04

- main.jpg through photo-08.jpg (9 photos)
- Professional HDR photos, various sizes

### Room 05

- main.jpg through photo-17.jpg (18 photos)
- Professional HDR photos, some 2-3.2MB

### Room 06

- main.jpg through photo-10.jpg (11 photos)
- Professional HDR photos 2.5-3.6MB

### Room 07

- main.jpg through photo-10.jpg (11 photos)
- Professional HDR photos with some modified versions

### Room 08

- main.jpg through photo-06.jpg (7 photos)
- Professional HDR photos

### Room 09

- main.jpg through photo-09.jpg (10 photos)
- UUID-named source files, all under 500KB

### Room 10

- main.jpg through photo-10.jpg (11 photos)
- UUID-named source files, all under 500KB

### Room 11

- main.jpg through photo-13.jpg (14 photos)
- UUID-named source files, all under 500KB

### Room 12 (Priority: OPS-03)

- main.jpg - 403KB
- photo-01.jpg - 386KB
- photo-02.jpg - 334KB
- photo-03.jpg - 298KB
- photo-04.jpg - 298KB
- photo-05.jpg - 293KB
- photo-06.jpg - 284KB
- photo-07.jpg - 278KB
- photo-08.jpg - 275KB
- photo-09.jpg - 232KB

**Status: Ready for HotelRunner upload**

## HotelRunner Compatibility

**Limit:** 2MB per photo

### Rooms Ready (under 2MB)

- Room 09: 10 photos ready
- Room 10: 11 photos ready
- Room 11: 14 photos ready
- Room 12: 10 photos ready (OPS-03 priority)

**Total ready: 45 photos**

### Rooms Needing Resize

- Room 01: 5 photos over 2MB
- Room 02: TBD (check sizes)
- Room 03: 6 photos over 2MB
- Room 04: TBD (check sizes)
- Room 05: 4+ photos over 2MB
- Room 06: 8+ photos over 2MB
- Room 07: TBD (check sizes)
- Room 08: TBD (check sizes)

**42 photos exceed 2MB** - will need resizing before HotelRunner upload

## Notes

- All photos copied from `legacy/content_source/facilities/rooms/{room}/images/`
- Rooms 01-08 used professional HDR photos (\_DSC\*.jpg files)
- Rooms 09-12 used UUID-named JPEG files (smaller, mobile-quality)
- Original UUID filenames mapped to sequential naming (main.jpg, photo-01.jpg, etc.)
- WhatsApp images (with spaces in filenames) were skipped to avoid copy issues
- Photo content not visually verified - naming based on file size sorting (largest = main)

## Recommendations

1. **OPS-03 Ready:** Room 12 can be uploaded immediately
2. **Batch resize:** Use ImageMagick or similar to resize oversized photos to under 2MB
3. **Quality review:** Consider visual review of main.jpg selections per room
4. **Missing metadata:** Consider adding room descriptions to photos after content review
