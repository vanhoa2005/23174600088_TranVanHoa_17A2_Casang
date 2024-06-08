import random
import csv

def mô_phỏng_lựa_chọn_người_chơi():
    return random.choice([0, 1, 2])

def hiển_thị_cửa_dê(cửa, lựa_chọn_người_chơi, cửa_xe):
    cửa_còn_lại = [i for i in range(3) if i != lựa_chọn_người_chơi and i != cửa_xe]
    return random.choice(cửa_còn_lại)

def xác_định_kết_quả(cửa, lựa_chọn_người_chơi, đổi_lựa_chọn):
    cửa_xe = cửa.index("Xe")
    if đổi_lựa_chọn:
        cửa_dê_hiển_thị = hiển_thị_cửa_dê(cửa, lựa_chọn_người_chơi, cửa_xe)
        lựa_chọn_mới = [i for i in range(3) if i != lựa_chọn_người_chơi and i != cửa_dê_hiển_thị][0]
        return cửa[lựa_chọn_mới] == "Xe", lựa_chọn_mới
    else:
        return cửa[lựa_chọn_người_chơi] == "Xe", lựa_chọn_người_chơi

def mô_phỏng_lượt_chơi(lựa_chọn_người_chơi, đổi_lựa_chọn):
    cửa = ["Xe", "Dê", "Dê"]
    random.shuffle(cửa)
    cửa_xe = cửa.index("Xe")
    cửa_dê_hiển_thị = hiển_thị_cửa_dê(cửa, lựa_chọn_người_chơi, cửa_xe)
    
    kết_quả, lựa_chọn_cuối = xác_định_kết_quả(cửa, lựa_chọn_người_chơi, đổi_lựa_chọn)
    return lựa_chọn_người_chơi, cửa_dê_hiển_thị, đổi_lựa_chọn, kết_quả

def tính_toán_xác_suất_thắng(số_lần_mô_phỏng):
    xác_suất_thắng = {"Giữ nguyên": 0, "Đổi lựa chọn": 0}
    kết_quả_mô_phỏng = []

    for _ in range(số_lần_mô_phỏng):
        lựa_chọn_người_chơi = mô_phỏng_lựa_chọn_người_chơi()
        
        # Người chơi có cơ hội đổi lựa chọn
        đổi_lựa_chọn = random.choice([True, False])
        
        lựa_chọn, cửa_dê, đổi_lựa_chọn, kết_quả = mô_phỏng_lượt_chơi(lựa_chọn_người_chơi, đổi_lựa_chọn)

        if đổi_lựa_chọn:
            xác_suất_thắng["Đổi lựa chọn"] += kết_quả
        else:
            xác_suất_thắng["Giữ nguyên"] += kết_quả

        kết_quả_mô_phỏng.append((lựa_chọn, cửa_dê, đổi_lựa_chọn, kết_quả))

    for chiến_lược in xác_suất_thắng:
        xác_suất_thắng[chiến_lược] /= số_lần_mô_phỏng

    return xác_suất_thắng, kết_quả_mô_phỏng

def lưu_kết_quả_vào_csv(xác_suất_thắng, số_lần_mô_phỏng, kết_quả_mô_phỏng):
    with open("kết_quả_monty_hall.csv", "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Số lần mô phỏng", số_lần_mô_phỏng])
        writer.writerow(["Chiến lược", "Xác suất thắng"])
        for chiến_lược, xác_suất in xác_suất_thắng.items():
            writer.writerow([chiến_lược, xác_suất])
        
        writer.writerow([])
        writer.writerow(["Lựa chọn ban đầu", "Cửa dê hiển thị", "Đổi lựa chọn", "Kết quả"])
        for kết_quả in kết_quả_mô_phỏng:
            writer.writerow(kết_quả)

def main():
    số_lần_mô_phỏng = 200
    xác_suất_thắng, kết_quả_mô_phỏng = tính_toán_xác_suất_thắng(số_lần_mô_phỏng)
    print(f"Xác suất thắng khi giữ nguyên: {xác_suất_thắng['Giữ nguyên']:.2f}")
    print(f"Xác suất thắng khi đổi lựa chọn: {xác_suất_thắng['Đổi lựa chọn']:.2f}")
    lưu_kết_quả_vào_csv(xác_suất_thắng, số_lần_mô_phỏng, kết_quả_mô_phỏng)

if __name__ == "__main__":
    main()
