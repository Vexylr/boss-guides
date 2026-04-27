# **FIRELANDS — BALEROC**
## Boss guide · Normal + Heroic · Discord-ready

**Tag key:** **[N]** = Normal only · **[H]** = Heroic only · **[N/H]** = Both

---

## **OVERVIEW**

Baleroc is a **single-phase** encounter that tests **healer throughput** and **crystal discipline**. **Meta (both modes):** use **one tank** — the tank’s HP balloons from **Blaze of Glory** to survive **Inferno Blade**, while **Decimation Blade** always hits for **90% of the tank’s current max HP** (minimum 250k). If you **swap tanks**, the incoming tank often has the **wrong** HP profile and gets **one-shot** by whichever blade is active because blade damage **scales with the current tank’s Vitals**. Therefore **solo tank** + heavy external healing is standard; a second tank is only an emergency cooldown, not a rotation. **Shards of Torment** force DPS to **soak** stacking **Torment**; **healers** must alternate building **Vital Spark** on soakers and unloading **Vital Flame** into the tank. **6-minute hard enrage.** Heroic adds **Countdown** (two players within **4 yd** or both explode) and **Tormented** spreading.

| Phase | Goal |
|--------|------|
| **Fight** | Solo tank holds boss; shard soakers rotate Torment; healers cycle Vital Spark → Vital Flame on the tank. [H] Countdown: linked players stand within 4 yd. |

---

## **HEALTH & TIMERS**

| Unit | **[N]** Normal | **[H]** Heroic |
|------|----------------|----------------|
| **Baleroc** | ~12.7M (10) / ~39.1M (25) | ~19.5M (10) / ~59.5M (25) |

- **Enrage:** **6 minutes** [N/H]. Does not instantly wipe the raid; Baleroc can be kited with avoidance, but kill before or soon after.
- **Shards of Torment** [N/H]: **1 shard** (10-man) / **2 shards** (25-man). Spawn on the **closest non-tank** to Baleroc. If **no one** is in range of a shard, **Wave of Torment** hits the **entire raid** — never leave shards unmanned.
- **Blades of Baleroc** [N/H]: Every **~15 seconds** Baleroc empowers one blade for **15 sec**. **First blade is always Inferno Blade.** Then random Inferno / Decimation.

---

## **SHARDS & TORMENT** [N/H]

### **Shard placement**

- Shards spawn on the **closest non-tank** (usually melee). Stack melee in a **predictable spot** before each shard so the crystal appears where you want.
- **Only DPS** should take Torment. **Tanks and healers must never** stand in the beam — **Tormented** halves healing and makes Decimation/Inferno lethal on tanks.

### **Torment & Tormented**

- The shard **channels** on the **nearest player** in range, applying **Torment** (stacking Shadow damage). Damage per tick increases with stacks; each shard applies about **24–25 stacks** total.
- When you **leave** the shard (or another player becomes closer), you **lose** Torment after 1–2 seconds and gain **Tormented** [N/H]:
  - **Tormented:** +Shadow damage taken; **healing done reduced by 50%** for **40 seconds**.
  - Do **not** take Torment again until Tormented expires. Rotate so the next soaker steps in.
- **Soak strategies:** e.g. 2 DPS take ~12 stacks each (high damage on soaker); or 3 DPS take ~8 stacks each (~32k Shadow/sec at peak). Or one DPS with a strong defensive (e.g. glyphed Divine Protection) takes 15–18 stacks, another takes the rest — healers gain more **Vital Spark** from higher stacks.
- **[H]** **Tormented spreads to nearby players.** Keep Tormented players **away from** tanks, other soakers, and healers (but still in range for **Countdown** if needed).

---

## **BLADES & SOLO TANKING** [N/H]

### **Blaze of Glory**

- Baleroc applies **Blaze of Glory** to his **current tank**: +**20% max HP**, +**20% physical damage taken**. Stacks. Each application gives Baleroc **Incendiary Soul** (+20% Fire damage dealt).
- **Solo tank:** Keeps stacking Blaze all fight — HP climbs into the **millions** late, which is required to survive **Inferno Blade** after many **Incendiary Soul** stacks.

### **Inferno Blade & Decimation Blade**

- **Inferno Blade** [N/H]: For 15 sec, Baleroc’s melee attacks deal **100,000 Fire** (no Physical). With huge HP pools + CDs the solo tank eats the swings.
- **Decimation Blade** [N/H]: For 15 sec, melee attacks deal **Shadow damage = 90% of target’s max HP** (minimum **250,000**). Cannot be mitigated; swings are slow. Because the value scales off **current max HP**, the solo tank simply needs to be **fully topped** between swings — externals, healer Vital Flame, personal CDs.
- **Why not swap?** A second tank enters with **low/no Blaze stacks** and wrong max HP → **Decimation** or **Inferno** removes them instantly. Only use a backup tank if the main dies.

---

## **HEALING: VITAL SPARK & VITAL FLAME** [N/H]

- **Vital Spark:** When a healer casts a **direct heal** (single-target, not HoT/AoE) on a player who has **Torment** stacks, the healer gains **Vital Spark** (1 stack per 3 Torment stacks on the target). Stack Spark by healing **shard soakers**.
- **Vital Flame:** When a healer with **Vital Spark** casts a **direct heal** on a target with **Blaze of Glory** (the tank), Spark is **consumed** and becomes **Vital Flame**: +**5% healing done** to that tank per stack consumed, for **15 sec**. When Vital Flame expires, the **Spark stacks are restored**.
- **Rotation:** One healer team heals **Torment soakers** to build Spark; the other heals the **tank** and uses Vital Flame. Every **15 sec** (or every 30 sec if you do two Flame cycles then swap), **swap roles** so the Spark builders become Flame users and vice versa. Time swaps with shard phases (~28 sec per shard) for smooth execution.

---

## **HEROIC-ONLY MECHANICS** [H]

- **Countdown** [H]: Baleroc **links two players** for **8 sec**. They must **move within 4 yards** of each other before the effect ends, or **both explode** for **100,000 Fire** to everyone within **100 yards** (wipe). If one of the two has **Tormented**, moving together can spread Tormented — with perfect play you can avoid spreading, but have backup soakers/healers ready. **Do not run away from your partner.**
- **Tormented** [H]: When a player gains Tormented, it **spreads to all nearby** players. Keep Tormented players **isolated** from tanks and healers (but still able to close for Countdown if they’re linked).
- Higher boss HP and damage; 6 min enrage is tight. Healer Spark/Flame coordination is mandatory.

---

## **STRATEGY SUMMARY**

**Tanks** [N/H]
- **Primary tank:** Solo-tank entire fight; never touch Shards. Stack Blaze, rotate CDs through Inferno windows, be 100% topped before each Decimation swing.
- **Bench tank (optional):** Only enter if main dies — expect to use battle rez instead, because picking up mid-blade without Blaze stacks is nearly impossible.

**Shard soakers (DPS)** [N/H]
- Pre-position so shards spawn in a set spot. Rotate who stands in the beam; leave before Tormented would overlap with next soaker. **[H]** Stay away from others when you have Tormented; if you get **Countdown**, run to your linked partner and stand within 4 yd.

**Healers** [N/H]
- Split: one team builds **Vital Spark** on Torment targets, the other uses **Vital Flame** on the active tank. Swap every 15–30 sec. Never stand in Shard beam. **[H]** If Countdown links two healers or a healer + soaker, still close to 4 yd — have backup heals/soakers.

**DPS (non-soakers)** [N/H]
- Burn Baleroc. Don’t stand in Shard beam unless you’re in the rotation. **[H]** Countdown: move to your linked partner within 4 yd immediately.

---

## **QUICK REFERENCE**

| Mechanic | **[N]** Normal | **[H]** Heroic |
|----------|----------------|----------------|
| 6 min enrage | &#10003; | &#10003; |
| 1 Shard (10) / 2 Shards (25); DPS only soak | &#10003; | &#10003; |
| Tormented 40s — don’t re-soak until it drops | &#10003; | &#10003; |
| Solo tank (no blade swap) | &#10003; | &#10003; |
| Vital Spark on Torment targets → Vital Flame on tank | &#10003; | &#10003; |
| Countdown: stand within 4 yd of linked player | — | &#10003; |
| Tormented spreads to nearby | — | &#10003; |

---

*Firelands — Baleroc. All mechanics tagged [N] / [H]. Copy-paste into Discord as needed.*

---
← [Back to Firelands index](../README.md)
