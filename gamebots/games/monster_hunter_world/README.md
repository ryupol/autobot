# Monster Hunter: World

[ภาษาไทย](#ภาษาไทย) | [English](#english)

## ภาษาไทย

ระบบอัตโนมัติที่มี:

- ฟาร์มเควส Icebloom
- กด Tailraider ซ้ำ

สคริปต์ใช้ปุ่มควบคุมเริ่มต้นและทำงานตามเวลา ไม่มีระบบตรวจจับภาพหน้าจอ

### สิ่งที่ต้องเตรียมสำหรับ Icebloom

เส้นทางปัจจุบันกำหนดว่า:

- เริ่มที่ Seliana Central Area
- เควส Icebloom อยู่ลำดับ 3 ในรายการเควส
- camp 7 อยู่ลำดับ 3 ในรายการ camp
- ปุ่ม interact คือ `F`
- ใช้ปุ่มเมนูและปุ่มเดินค่าเริ่มต้น

เตรียมเกม:

1. เข้าเควสเป้าหมายหนึ่งครั้ง แล้วกดออกจากเควส
2. เข้า Seliana Central Area ถ้าอยู่ที่นี่แล้ว ให้ไปพื้นที่อื่นแล้วกลับมาใหม่
3. หลังโหลดเสร็จห้ามขยับตัวละคร
4. ถ้าเผลอขยับเมาส์หรือตำแหน่งกล้อง ให้กด `Left Ctrl` เพื่อ reset ก่อนเริ่ม
5. เลื่อนเมาส์ออกจากกลางจอ เพราะ pointer อาจเลือกปุ่มผิดตอนเปิด Quest Board

### เวลาโหลด

ใส่เวลาโหลดโดยประมาณในไฟล์ `loading_time.txt` ที่ root:

```text
15
```

หน่วยเป็นวินาที ถ้าไฟล์หายหรือว่าง ระบบใช้ 15 วินาที

- เครื่องเร็ว: ลอง 10–11 วินาที
- เครื่องช้า: ลอง 16–17 วินาที
- ควรเผื่อเวลา ถ้าสั้นเกินไป sequence จะคลาดเคลื่อน

### รันฟาร์ม Icebloom

รันจาก root ของโปรเจกต์:

```powershell
python -m gamebots.games.monster_hunter_world icebloom
```

ระหว่างนับถอยหลัง 3 วินาที ให้สลับกลับไปหน้าเกม

ค่าเริ่มต้นรัน 20 big rounds โดยหนึ่ง big round มี 5 เควส รวม 100 เควส

กำหนดจำนวนรอบ เปิดเก็บของและเติมปุ๋ย หรือเปลี่ยน camp ได้:

```powershell
python -m gamebots.games.monster_hunter_world icebloom --rounds 1 --gather-item
python -m gamebots.games.monster_hunter_world icebloom --camp 3
```

### รัน Tailraider

เตรียมตัวละครให้อยู่ในสถานะที่กด Tailraider ได้ แล้วรัน:

```powershell
python -m gamebots.games.monster_hunter_world tailraider
```

ค่าเริ่มต้นกด interaction ของ Tailraider 40 รอบ

เปลี่ยนจำนวนรอบ:

```powershell
python -m gamebots.games.monster_hunter_world tailraider --rounds 10
```

### ตรวจสอบครั้งแรก

ควรเฝ้าดูอย่างน้อยหนึ่ง big round เต็ม ใช้เวลาประมาณ 17 นาที
ขึ้นอยู่กับเวลาโหลด ตรวจสอบว่า:

- Quest Board เลือกรายการถูก
- ตัวละครเริ่มจากตำแหน่งที่กำหนด
- ลำดับ camp และ quest ตรงกับสคริปต์
- ขั้นตอนรับรางวัลและออกจากเควสยังตรงเวลา

ถ้าเส้นทางคลาดเคลื่อน ให้หยุดด้วย `Ctrl+C` แล้ว reset ตำแหน่งก่อนลองใหม่


---

## English

Available automation:

- Icebloom quest farming;
- Tailraider interaction loop.

Scripts expect default keyboard controls and run through timed input. No screen
recognition is used.

## Icebloom prerequisites

Current route expects:

- Seliana Central Area starting position;
- Icebloom quest at quest-list position 3;
- camp 7 at camp-list position 3;
- default interaction key `F`;
- default menu and movement bindings.

Prepare game:

1. Enter target quest once, then leave quest.
2. Enter Seliana Central Area. If already there, travel elsewhere and return.
3. Do not move character after area loads.
4. If mouse moved character/camera, press `Left Ctrl` to reset before starting.
5. Move mouse pointer away from screen center. Pointer can select wrong
   quest-board buttons.

## Loading time

Set estimated loading duration in root `loading_time.txt`:

```text
15
```

Value uses seconds. Missing or empty file defaults to 15.

- Faster system: try 10–11 seconds.
- Slower system: try 16–17 seconds.
- Leave safety margin. Short value can desynchronize route.

## Run Icebloom farming

From project root:

```powershell
python -m gamebots.games.monster_hunter_world icebloom
```

During 3-second countdown, switch focus back to game.

Default launcher runs 20 big rounds. Each big round runs 5 quests, producing
100 quest runs total.

Set round count, enable botanical gathering, or change camp:

```powershell
python -m gamebots.games.monster_hunter_world icebloom --rounds 1 --gather-item
python -m gamebots.games.monster_hunter_world icebloom --camp 3
```

## Run Tailraider loop

Prepare game at expected Tailraider interaction state, then run:

```powershell
python -m gamebots.games.monster_hunter_world tailraider
```

Default launcher repeats Tailraider interaction 40 times.

Change round count:

```powershell
python -m gamebots.games.monster_hunter_world tailraider --rounds 10
```

## First-run checks

Watch at least one full big round, about 17 minutes depending on loading time.
Check:

- quest-board cursor selects correct entries;
- character starts from exact expected position;
- camp and quest menu ordering matches assumptions;
- reward and abandon sequence remains synchronized.

Stop with `Ctrl+C` if route drifts. Reset starting position before retrying.
