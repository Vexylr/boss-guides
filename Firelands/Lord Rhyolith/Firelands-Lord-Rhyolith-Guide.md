# **FIRELANDS — LORD RHYOLITH**
## Boss guide · Normal + Heroic · Discord-ready

**Tag key:** **[N]** = Normal only · **[H]** = Heroic only · **[N/H]** = Both

---

## **OVERVIEW**

Lord Rhyolith is a **two-phase** encounter. The raid **steers him by damaging his feet** so he walks over **active volcanoes** to break his **Obsidian Armor**. If he reaches the **lava at the plateau edge**, he gains **Drink Magma** [N/H] and will wipe the raid.

| Phase | Health | Goal |
|--------|--------|------|
| **Phase 1** | 100% → 25% | No tank on Rhyolith. Control movement, kill adds, break armor. |
| **Phase 2** | 25% → 0% | Tank Rhyolith. Burn before **Immolation** [N/H] and **Superheated** [N/H] overwhelm the raid. |

---

## **HEALTH & TIMERS**

| Unit | **[N]** Normal | **[H]** Heroic |
|------|----------------|----------------|
| **Lord Rhyolith** | 12.7M (10) / 39.1M (25) | 19.5M (10) / 59.5M (25) |
| **Spark of Rhyolith** | 1.4M (10) / 4.8M (25) | 2.1M (10) / 7.1M (25) |
| **Fragment of Rhyolith** | 99k (10) / 395k (25) | 197k (10) / 652k (25) |
| **Liquid Obsidian** | — | 210k (10) / 458k (25) |

- **Enrage:** No hard enrage. Phase 2 acts as a **soft enrage** (Immolation [N/H] + **Superheated** [N/H]).
- **Superheated** [N/H]: Stacks every 10s, +10% damage per stack.
  - **[N]** Starts **6 minutes** into the fight.
  - **[H]** Starts **5 minutes** into the fight (tighter DPS/heal check).

---

## **PHASE 1 — ARMOR PHASE (100% → 25%)** [N/H]

### **Steering Rhyolith** [N/H]

- Rhyolith has **left** and **right** feet (separate health bars). Damage is **equalized** between feet over time.
- **More damage on left foot** → he turns **left**. **More on right** → **right**. Equal → straight.
- **Direction gauge** (default UI/addons): 0% = left, 50% = straight, 100% = right. ~1s delay before he turns.
- **Do not** let him reach the **lava edge** → **Drink Magma** [N/H]: **35,000 Fire/sec for 4s** (raid wipe).
- Assign a **pilot** (often a melee DPS) to call “left foot” / “right foot” and choose which **active** volcano to hit next. **Ranged** usually prioritize **Spark → Fragments** while melee **drive**; this split is not mandatory but is the most common pug layout.

### **Turning sensitivity (community notes)** [N/H]

- Different clients (retail 4.x vs modern private realms) weight **damage vs. hit count vs. class** differently when resolving how fast Rhyolith’s **direction gauge** moves. Some groups report **more players on a foot** feels better than one player tunneling huge burst; others swear by **rogue/feral/Death Knight** tick density or **Warrior Colossus Smash** windows. **Treat steering as a black box:** pick pilots who communicate, keep **multiple** damage sources on the correct foot when you need sharp turns, and validate what works on **your** server instead of arguing a universal formula.

### **Armor & volcanoes** [N/H]

- **Obsidian Armor** [N/H]: Starts at **80% damage reduction**. Each time he steps on an **active** (erupting) volcano, his armor is **reduced by 10%**.
- **Concussive Stomp** [N/H] (every ~20–25s): Creates **2–3 volcanoes**; deals Fire damage to the raid.
- Volcanoes are **dormant** or **active**. Only **active** volcanoes remove armor when he steps on them.
- **Dormant volcano:** If he steps on it, he gains **Molten Armor** [N/H] (increased damage):
  - **[N]** +2% damage per stack.
  - **[H]** +5% damage per stack — **avoid stepping on dormant**.
- When he steps on any volcano, it is **destroyed**. **10s later** a **crater** appears at that location.

### **Craters & Magma Flow** [N/H]

- Crater triggers **Magma Flow** [N/H]: **4–6 lava streams** move outward from it.
- **65,000 Fire** to anyone in the stream path; after **10s** streams **explode** for **130,000 Fire**. Then the crater leaves a damaging lava pool.
- **Everyone:** Move out of lava streams. Learn the common patterns.

### **Adds — Thermal Ignition** [N/H] (every 20–25s)

**Thermal Ignition** [N/H]: **15,000 Fire** to players within **7 yards** of Rhyolith. He then spawns **either**:

- **Fragments of Rhyolith** [N/H]: **[N]** 5 Fragments · **[H]** 10 Fragments.  
  Low HP, light melee. **Kill within 30s** or they **Meltdown** (deal 100% of their remaining HP to a random player and die).
- **Spark of Rhyolith** [N/H]: **1 Spark**.  
  High HP, melee on tank. **Immolation**: ~**8,500 Fire/sec** to everyone within **12 yards**. **Infernal Rage** every 5s (+10% damage dealt and taken, stacks to 20).  
  **Tank Spark ≥12 yards from raid** (e.g. near plateau edge). Ranged kill Spark; melee can help on Fragments if needed.

### **Active volcanoes — Eruption** [N/H]

- When a volcano is **active**, it **Erupts** for **20s**: every **2s** it hits **3 (10-man) / 6 (25-man)** players for **10,000 Fire** and applies a **stacking debuff** (+5% Fire damage taken, 14s, max 20 stacks).
- More active volcanoes = more Eruption = very high Fire damage later. Push armor down and reach Phase 2 before stacks get out of hand.

---

## **PHASE 2 — BURN (25% → 0%)** [N/H]

- At **25%** health, his armor **shatters**. He becomes tankable and **melees** the tank (~25–30k per hit).
- **All adds despawn** (Fragments, Sparks, **[H]** Liquid Obsidian).
- **Immolation** [N/H]: ~**8,000 Fire/sec** to the **entire raid** (constant).
- **Concussive Stomp** [N/H]: Still occurs — **35,000 Fire** to all players; volcanoes, craters, and Magma Flow continue. **Eruption** debuff is **reset** when Phase 2 starts (Mage Ice Block, Paladin Divine Shield, Rogue Cloak can also clear the Fire debuff).
- **Superheated** [N/H]: Once it starts, damage ramps quickly. Use **Bloodlust / Heroism / Time Warp** in Phase 2. Healers use cooldowns; raid stacks for AoE heals and avoids lava (and **[H]** Unleashed Flame).

---

## **HEROIC-ONLY MECHANICS** [H]

- **Liquid Obsidian** [H]: **10** spawn when Rhyolith steps on an **active** volcano. They **walk slowly toward Rhyolith** (no aggro). If they reach him, they **Fuse** — each Fuse **increases his damage reduction by 1%** (effectively restoring armor).  
  **Slow, root, stun, knockback** them. They die to AoE; a few reaching him is acceptable; many = too much armor and you hit enrage.
- **Superheated at 5 minutes** [H] (not 6) — Phase 2 must be short.
- **Molten Armor** [H]: +5% per stack (stepping on dormant is very punishing).
- **Unleashed Flame** [H]: Rhyolith unleashes **beams of fire that pursue random players**. Impact deals **10,000 Fire** to everyone within **5 yards** of the beam. **Move out of impacts**; stay spread and keep avoiding Magma Flow lava.
- **[H]** Higher add and boss HP/damage. Prefer **1 tank**, **2–3 (10) / 5–6 (25) healers**, rest DPS. More **ranged** helps (Sparks, Fragments, feet, avoiding ground).

---

## **STRATEGY SUMMARY**

**Phase 1** [N/H]
- **Pilot:** Keep Rhyolith away from lava edge; steer him only over **active** volcanoes; avoid dormant. **[H]** Be vocal — direction gauge is more reactive.
- **Tank:** Hold Spark(s) and Fragments. Spark **≥12 yd** from raid. **[H]** Optionally tank Fragments on top of Liquid Obsidian for cleave.
- **Melee:** Focus on **feet** to steer; help on Fragments **[H]** / Liquid Obsidian when free.
- **Ranged:** Priority Spark → Fragments (kill before 30s) → Rhyolith/feet. Don’t stand in Magma Flow or near Spark.
- **Healers:** Eruption, Concussive Stomp, Spark tank, occasional add cleave. Fire debuff stacks get high late in the phase.

**Phase 2** [N/H]
- **Tank:** Face Rhyolith; survive melee + Concussive Stomp (use CDs on Stomp after Superheated).
- **Raid:** Stack for heals, **Lust** early, avoid lava streams **[H]** and **Unleashed Flame** impacts. Personal defensives and healthstones on Stomps.
- **Kill before** Superheated + Immolation overwhelm healers (~40s after Superheated on **[H]** if you’re late).

---

## **QUICK REFERENCE**

| Mechanic | **[N]** Normal | **[H]** Heroic |
|----------|----------------|----------------|
| Steer with feet | ✓ | ✓ |
| Step on **active** volcanoes only | ✓ | ✓ (dormant = +5% dmg) |
| Kill Fragments before 30s | ✓ (5 per wave) | ✓ (10 per wave) |
| Tank Spark away (12 yd) | ✓ | ✓ |
| Liquid Obsidian | — | ✓ Slow/root/knockback |
| Superheated | 6 min | **5 min** |
| Unleashed Flame (beams chase players) | — | ✓ Move out of impact (5 yd) |
| Molten Armor per stack | +2% | **+5%** |

---

*Firelands — Lord Rhyolith. All mechanics tagged [N] / [H]. Copy-paste into Discord as needed.*

---
← [Back to Firelands index](../README.md)
