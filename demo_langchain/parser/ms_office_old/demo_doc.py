# 使用 LibreOffice 将 doc 转换为 docx
"""
1、在系统上安装 LibreOffice
    - mac: brew install --cask libreoffice
    - Linux (Ubuntu/Debian): sudo apt-get install libreoffice
    - Windows: 从官网下载安装 https://www.libreoffice.org/
"""

import subprocess
import threading
import os
import logging
from typing import List, Optional, Tuple

# 配置日志
logger = logging.getLogger(__name__)

libreoffice_lock = threading.Lock()


class LibreOfficeConverter:
    """
    LibreOffice 文档转换工具类
    支持格式: doc -> docx, xls -> xlsx, ppt -> pptx 等
    """

    # 支持的转换格式映射
    SUPPORTED_CONVERSIONS = {
        "doc": "docx",
        "dot": "docx",
        "xls": "xlsx",
        "xlt": "xlsx",
        "ppt": "pptx",
        "pot": "pptx",
        "odt": "docx",
        "ods": "xlsx",
        "odp": "pptx",
        "rtf": "docx",
    }

    def __init__(self, libreoffice_path: str, timeout: int = 60, headless: bool = True):
        """
        初始化转换器

        Args:
            libreoffice_path: LibreOffice 命令路径（必需）
            timeout: 转换超时时间（秒）
            headless: 是否使用无头模式
        """
        if not libreoffice_path:
            raise ValueError("libreoffice_path 参数不能为空")

        self.libreoffice_path = libreoffice_path
        self.timeout = timeout
        self.headless = headless

        logger.debug(
            f"初始化 LibreOfficeConverter: cmd={libreoffice_path}, timeout={timeout}s"
        )

    def convert_document(
        self,
        input_file: str,
        output_dir: Optional[str] = None,
        output_filename: Optional[str] = None,
    ) -> str:
        """
        转换文档格式

        Args:
            input_file: 输入文件路径
            output_dir: 输出目录（默认为输入文件所在目录）
            output_filename: 输出文件名（不包含扩展名，默认为输入文件名）

        Returns:
            Tuple[bool, Optional[str]]: (是否成功, 输出文件路径)
        """
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            raise FileNotFoundError(input_file)

        # 检查格式是否支持
        file_ext = os.path.splitext(os.path.basename(input_file))[1][1:]
        target_format = self.SUPPORTED_CONVERSIONS.get(file_ext)
        if not target_format:
            raise Exception(f"unsupported convert file format {input_file}")

        # 获取输入文件信息
        input_file_path = os.path.abspath(input_file)
        input_dir = os.path.dirname(input_file_path)
        input_filename = os.path.splitext(os.path.basename(input_file))[0]

        # 设置输出路径
        if output_dir is None:
            output_dir = input_dir
        else:
            output_dir = os.path.abspath(output_dir)
            os.makedirs(output_dir, exist_ok=True)

        if output_filename is None:
            output_filename = input_filename

        # 构建转换命令
        cmd = [self.libreoffice_path]

        if self.headless:
            cmd.append("--headless")

        cmd.extend(
            ["--convert-to", target_format, "--outdir", output_dir, input_file_path]
        )

        logger.info(f"开始转换: {input_file} -> {target_format}")
        logger.debug(f"执行命令: {' '.join(cmd)}")

        try:
            with libreoffice_lock:
                result = subprocess.run(
                    cmd, check=True, capture_output=True, timeout=self.timeout, text=True
                )

            # 记录命令执行输出
            if result.stdout:
                logger.debug(f"LibreOffice 标准输出: {result.stdout}")
            if result.stderr:
                logger.warning(f"LibreOffice 错误输出: {result.stderr}")

            # 构建预期的输出文件路径
            output_file = os.path.join(output_dir, f"{output_filename}.{target_format}")

            if os.path.exists(output_file):
                logger.info(f"✓ 转换成功: {input_file} -> {output_file}")
                return output_file
            else:
                # 如果指定文件名不存在，尝试查找 LibreOffice 生成的默认文件名
                default_output = os.path.join(
                    output_dir, f"{input_filename}.{target_format}"
                )
                if os.path.exists(default_output):
                    logger.info(f"✓ 转换成功: {input_file} -> {default_output}")
                    return default_output
                else:
                    logger.error(f"转换成功但未找到输出文件，输入文件: {input_file}")
                    raise Exception("not found converted file")

        except subprocess.CalledProcessError as e:
            logger.error(f"转换失败: {e}")
            logger.error(f"标准输出: {e.stdout}")
            logger.error(f"错误输出: {e.stderr}")
            raise
        except subprocess.TimeoutExpired:
            logger.error(
                f"转换超时，输入文件: {input_file}, 超时时间: {self.timeout}秒"
            )
            raise
        except FileNotFoundError:
            logger.error(f"未找到 LibreOffice 命令: {self.libreoffice_path}")
            raise
        except Exception as e:
            logger.error(f"转换过程中发生错误: {e}", exc_info=True)
            raise


# 使用示例
if __name__ == "__main__":
    import threading
    # 配置日志
    logging.basicConfig(level=logging.INFO)

    # 从配置中获取命令（这里假设 config.LIBRE_OFFICE 已定义）
    # 在实际项目中，这可能是从 Django settings 或其他配置系统获取


    try:
        # 直接使用配置的命令创建转换器

        LIBRE_OFFICE_CMD = "soffice"  # 替换为 config.LIBRE_OFFICE
        converter = LibreOfficeConverter(libreoffice_path=LIBRE_OFFICE_CMD, timeout=60)

        def convert(input_file):
            success = converter.convert_document(input_file)

            if success:
                print(f"转换成功")
            else:
                print("转换失败")
        # 执行转换
        thread1 = threading.Thread(target=convert, args=("example.doc",))
        thread2 = threading.Thread(target=convert, args=("demo1.xls",))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

    except Exception as e:
        print(f"转换器初始化失败: {e}")