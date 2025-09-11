import math

# 定义 SVG 文件的大小和圆心
width = 400
height = 400
center_x = width / 2
center_y = height / 2
radius = 150

# 计算每个扇形的角度
angle_step = 360 / 6

# 生成 SVG 文件内容
svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">'

for i in range(6):
    start_angle = i * angle_step
    end_angle = (i + 1) * angle_step

    # 计算扇形的起点和终点坐标
    start_x = center_x + radius * math.cos(math.radians(start_angle))
    start_y = center_y + radius * math.sin(math.radians(start_angle))
    end_x = center_x + radius * math.cos(math.radians(end_angle))
    end_y = center_y + radius * math.sin(math.radians(end_angle))

    # 确定是否为大圆弧
    large_arc_flag = 1 if end_angle - start_angle > 180 else 0

    # 生成扇形的路径数据
    path_data = f'M {center_x},{center_y} L {start_x},{start_y} A {radius},{radius} 0 {large_arc_flag},1 {end_x},{end_y} Z'

    # 为每个扇形设置不同的颜色
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    color = colors[i % len(colors)]

    # 添加扇形到 SVG 内容
    svg_content += f'<path d="{path_data}" fill="{color}" />'

svg_content += '</svg>'

# 将 SVG 内容保存到文件
with open('six_sectors.svg', 'w') as f:
    f.write(svg_content)

print("SVG 文件已生成：six_sectors.svg")
