# Conway's Game of Life
Author: Michael Trossbach

Contact: mptrossbach@gmail.com

## Oveview
Python implementation of Conway's Game of Life. My final assignment from the class where I first learned Python.

**Rules**:
1. A **DEAD** cell with exactly 3 **LIVING** neighbors will become a **LIVING** cell
2. A **LIVING** cell with 2 or 3 **LIVING** neighbors will remain **LIVING**
3. A **LIVING** cell with 1, 4, 5, 6, 7 or 8 **LIVING** neighbors will become **DEAD**
4. A **DEAD** cell without exactly 3 **LIVING** neighbors will remain **DEAD**

## Usage
**Example simulation of 3 generations**

```
$ python game_of_life.py
How many generations would you like to simulate?
Please enter an integer (min: 1; max: 15) and then press [ENTER]: 3
```

```
+----------------+
| GENERATION #01 |
+----------------+
 * |   |   |   |   
---+---+---+---+---
   | * | * |   |   
---+---+---+---+---
 * | * |   |   |   
---+---+---+---+---
   |   |   |   |   
---+---+---+---+---
   |   |   |   |   
+----------------+
| GENERATION #02 |
+----------------+
   | * |   |   |   
---+---+---+---+---
   |   | * |   |   
---+---+---+---+---
 * | * | * |   |   
---+---+---+---+---
   |   |   |   |   
---+---+---+---+---
   |   |   |   |   
+----------------+
| GENERATION #03 |
+----------------+
   |   |   |   |   
---+---+---+---+---
 * |   | * |   |   
---+---+---+---+---
   | * | * |   |   
---+---+---+---+---
   | * |   |   |   
---+---+---+---+---
   |   |   |   |   

```
