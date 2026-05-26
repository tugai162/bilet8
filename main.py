def objective(x1, x2):
    return 5*x1 + 4*x2

def check_constraints(x1, x2):
    if x1 + x2 > 5:
        return False
    if 2*x1 + x2 > 8:
        return False
    if x1 + x2 < 2:
        return False
    if x1 < 0 or x2 < 0:
        return False
    return True

def solve():
    points = [(0,0), (0,4), (2,3), (3,2), (4,0)]
    
    best_x1 = 0
    best_x2 = 0
    best_z = -999999
    
    print("="*50)
    print("БИЛЕТ №8: Распределение времени сотрудников")
    print("="*50)
    print("\nЦелевая функция: Z = 5x1 + 4x2 → max")
    print("\nОграничения:")
    print("  1) x1 + x2 ≤ 5")
    print("  2) 2x1 + x2 ≤ 8")
    print("  3) x1 + x2 ≥ 2")
    print("  4) x1 ≥ 0, x2 ≥ 0")
    print("\n" + "-"*50)
    print("Перебор вариантов:")
    print("-"*50)
    
    for x1, x2 in points:
        if check_constraints(x1, x2):
            z = objective(x1, x2)
            print(f"  x1={x1}, x2={x2} → Z={z} ✅")
            if z > best_z:
                best_z = z
                best_x1 = x1
                best_x2 = x2
        else:
            print(f"  x1={x1}, x2={x2} → ❌ не подходит")
    
    print("-"*50)
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТ:")
    print("="*50)
    print(f"  Оптимальное решение:")
    print(f"    x1 = {best_x1} (задача А)")
    print(f"    x2 = {best_x2} (задача Б)")
    print(f"  Максимальное значение: Z = {best_z}")
    print("="*50)
    
    return best_x1, best_x2, best_z

if __name__ == "__main__":
    solve()
    input("\nНажми Enter для выхода...")
