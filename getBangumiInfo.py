import json
import time

from bilibili_api import user, sync

# 实例化用户对象
u = user.User(361883361)


# 获取所有追番列表（分页）
async def get_all_bangumi():
    page = 1
    all_items = []

    while True:
        try:
            print(f"正在获取第 {page} 页数据...")
            result = await u.get_subscribed_bangumi(pn=page, ps=24)
            # 检查是否有数据
            if not result["list"]:
                print(f"第 {page} 页无数据，停止获取")
                break

            all_items.extend(result["list"])
            print(f"已获取 {len(result['list'])} 条数据，总计 {len(all_items)} 条")

            page += 1

            # 添加延迟避免请求过快
            time.sleep(0.5)

        except Exception as e:
            print(f"获取第 {page} 页时出错: {str(e)}")
            break

    return {"list": all_items, "total": len(all_items)}


def main():
    # 使用sync同步执行异步函数
    print("开始获取B站追番列表...")
    subscribe_list = sync(get_all_bangumi())

    if not subscribe_list["list"]:
        print("未获取到任何追番数据，请检查用户ID是否正确")
        return []

    # 提取需要的信息（番剧名称和季/版本信息）
    bangumi_data = []
    for item in subscribe_list["list"]:
        # 提取番剧名
        title = item["title"]

        # 合并为完整名称
        full_name = title

        bangumi_data.append(
            {
                "name": full_name,
                "media_id": item["media_id"],
                "season_id": item.get("season_id", ""),
                "cover": item.get("cover", ""),
            }
        )

    # 保存结果到JSON文件
    with open("bilibili_bangumi.json", "w", encoding="utf-8") as f:
        json.dump(bangumi_data, f, ensure_ascii=False, indent=2)
    print(f"\n已保存 {len(bangumi_data)} 条追番数据到 bilibili_bangumi.json")

    # 打印结果
    print("\n获取到追番列表:")
    for idx, bangumi in enumerate(bangumi_data, 1):
        print(f"{idx}. {bangumi['name']} (媒体ID: {bangumi['media_id']})")

    return bangumi_data


# 入口
if __name__ == "__main__":
    result = main()
