import random

def generateboxes(bigbox, num):
    retry = 500 * num
    while num > 1:
        cuboid = random.choice(bigbox)
        while cuboid[3] <= 11 or cuboid[4] <= 11 or cuboid[5] <= 11:
            retry -= 1
            if retry == 0:
                print("Khong the tao them hop, vui long thu lai.")
                return
            cuboid = random.choice(bigbox)

        bigbox.remove(cuboid)
        prob = random.uniform(0, 1)

        x1 = cuboid[0]
        y1 = cuboid[1]
        z1 = cuboid[2]
        x2 = cuboid[3]
        y2 = cuboid[4]
        z2 = cuboid[5]

        if prob < 0.33:
            # Chia theo chieu dai (ti le 1/3)
            t = random.randint(5, int(x2 / 2))
            package1 = [x1 + t, y1, z1, x2 - t, y2, z2]
            package2 = [x1, y1, z1, t, y2, z2]

        elif prob < 0.66:
            # Chia theo chieu rong (ti le 1/3)
            t = random.randint(5, int(y2 / 2))
            package1 = [x1, y1 + t, z1, x2, y2 - t, z2]
            package2 = [x1, y1, z1, x2, t, z2]

        else:
            # Chia theo chieu cao (ti le 1/3)
            t = random.randint(5, int(z2 / 2))
            package1 = [x1, y1, z1 + t, x2, y2, z2 - t]
            package2 = [x1, y1, z1, x2, y2, t]

        # gom hop
        bigbox.append(package1)
        bigbox.append(package2)
        num -= 1

    return bigbox
