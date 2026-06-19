class SiteSummary:
    def __init__(self, name, url, keywords, tags, description):
        self.name = name
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description
        }

    def brief(self):
        return f"[{self.name}]({self.url}) — {', '.join(self.tags[:3])}"

    def full_summary(self):
        lines = [
            f"站点名称：{self.name}",
            f"访问地址：{self.url}",
            f"关键词：{', '.join(self.keywords)}",
            f"标签：{', '.join(self.tags)}",
            f"简介：{self.description}",
        ]
        return "\n".join(lines)


def load_sample_sites():
    return [
        SiteSummary(
            name="Aoke 主站",
            url="https://main-web-aoke.com",
            keywords=["aoke", "平台", "服务"],
            tags=["主页", "入口", "核心"],
            description="Aoke 主站点，提供平台核心服务与最新动态。"
        ),
        SiteSummary(
            name="Aoke 博客",
            url="https://blog.main-web-aoke.com",
            keywords=["aoke", "博客", "技术"],
            tags=["文章", "更新", "开发"],
            description="Aoke 官方博客，发布技术文章与产品更新。"
        ),
        SiteSummary(
            name="Aoke API",
            url="https://api.main-web-aoke.com",
            keywords=["aoke", "接口", "开发者"],
            tags=["API", "文档", "集成"],
            description="Aoke 开发者接口，提供数据与功能调用能力。"
        ),
        SiteSummary(
            name="Aoke 帮助中心",
            url="https://help.main-web-aoke.com",
            keywords=["aoke", "帮助", "支持"],
            tags=["FAQ", "客服", "指南"],
            description="Aoke 帮助中心，包含常见问题与使用指南。"
        ),
    ]


def generate_markdown_summary(sites):
    lines = ["# 站点资料结构化摘要\n"]
    for idx, site in enumerate(sites, 1):
        lines.append(f"## {idx}. {site.name}")
        lines.append(f"- **URL**：{site.url}")
        lines.append(f"- **关键词**：{', '.join(site.keywords)}")
        lines.append(f"- **标签**：{', '.join(site.tags)}")
        lines.append(f"- **说明**：{site.description}\n")
    return "\n".join(lines)


def generate_text_summary(sites):
    result = []
    for site in sites:
        result.append(site.full_summary())
        result.append("---")
    return "\n".join(result)


def generate_html_snippet(sites):
    items = []
    for site in sites:
        safe_name = site.name.replace("&", "&amp;").replace("<", "&lt;")
        safe_url = site.url.replace("&", "&amp;").replace("<", "&lt;")
        safe_desc = site.description.replace("&", "&amp;").replace("<", "&lt;")
        tags_html = ", ".join(
            f"<span class='tag'>{t.replace('&', '&amp;').replace('<', '&lt;')}</span>"
            for t in site.tags
        )
        items.append(
            f'<div class="site-card">'
            f'<h3>{safe_name}</h3>'
            f'<a href="{safe_url}" target="_blank">{safe_url}</a>'
            f'<p>{safe_desc}</p>'
            f'<div class="tags">{tags_html}</div>'
            f"</div>"
        )
    return "\n".join(items)


def main():
    sites = load_sample_sites()

    print("=== Markdown 摘要 ===\n")
    print(generate_markdown_summary(sites))

    print("\n=== 纯文本摘要 ===\n")
    print(generate_text_summary(sites))

    print("\n=== HTML 卡片摘要 ===\n")
    print(generate_html_snippet(sites))


if __name__ == "__main__":
    main()