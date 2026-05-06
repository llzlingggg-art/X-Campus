import streamlit as st
import pandas as pd
import time

# 1. 页面基本设置
st.set_page_config(page_title="X-Campus: AI 校园信息差终结者", page_icon="🎓", layout="wide")

# 2. 侧边栏：用户身份与状态
st.sidebar.title("🎓 X-Campus 智享校园")
st.sidebar.caption("打破信息孤岛，AI 为你的学业护航")
st.sidebar.markdown("---")

identity = st.sidebar.radio("当前活跃身份切换", ["👤 匿名学神 (ID: u_8921)", "🎓 实名认证 (罗聆榛 - 国际商务)"])
st.sidebar.metric(label="账户学分 (可提现)", value="🪙 1,250", delta="+350 今日收益")

st.sidebar.markdown("---")
st.sidebar.info("💡 **AI 质检系统运行中**\n\n全站所有上架资源均经过大模型初步审核，杜绝虚假/灌水资料。")

# 3. 主页面标题
st.title("📚 打破学业信息差：高价值资源流转枢纽")
st.markdown("在这里，你可以**匿名/实名**出售你的独家复习笔记、历年真题回忆、导师选课避坑指南，或寻找你急需的过考秘籍。")

# 4. 核心功能区 (Tabs)
tab1, tab2, tab3 = st.tabs(["🔥 资源交易大厅", "🤖 AI 需求精准匹配", "📤 一键发布资源"])

# --- Tab 1: 资源交易大厅 ---
with tab1:
    st.subheader("今日高热度学业资源")
    
    # 模拟数据
    data = {
        '资源类型': ['历年真题', '选课指南', '高分笔记', '保研经验', '竞赛组队'],
        '资源标题': ['大三下《计量经济学》近五年期末考点预测与真题回忆版', '经管学院四大“魔鬼导师”选课防坑/给分揭秘', '雅思首战7.5：纯自学一个月备考全套笔记+时间表', '2025届曼大/港理工商科硕士申请全套文书拆解', '全国大创项目国家级金奖：立项申报书完整参考'],
        '卖家身份': ['匿名学姐 (已认证)', '实名: 张三(大四)', '匿名学长 (已认证)', '实名: 罗聆榛', '匿名大佬 (已认证)'],
        'AI 质量评分': ['⭐⭐⭐⭐⭐ (98分)', '⭐⭐⭐⭐ (85分)', '⭐⭐⭐⭐⭐ (95分)', '⭐⭐⭐⭐⭐ (99分)', '⭐⭐⭐⭐ (88分)'],
        '价格': ['🪙 50 学分', '🪙 15 学分', '🪙 80 学分', '🪙 120 学分', '🪙 100 学分']
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # 模拟购买动作
    col1, col2 = st.columns([3, 1])
    with col1:
        st.selectbox("选择你想购买的资源", df['资源标题'])
    with col2:
        st.write("")
        st.write("")
        if st.button("立即购买 (匿名交易)"):
            st.success("🎉 购买成功！资源已发送至您的网盘，扣除相应学分。")

# --- Tab 2: AI 需求精准匹配 (核心亮点) ---
with tab2:
    st.subheader("🤖 不知道买什么？告诉 AI 你的烦恼")
    st.markdown("描述你当前遇到的学业瓶颈，大模型将自动从海量库中为你提取匹配度最高的资源，并生成学习路径。")
    
    user_need = st.text_area("例如：下周就要考国际商务核心课了，但我完全没听懂供应链模型，怎么办？急！", height=100)
    if st.button("✨ 让 AI 帮我找资源"):
        if user_need:
            with st.spinner("AI 正在解析您的痛点，检索全校学霸资源库..."):
                time.sleep(2) # 模拟 AI 思考时间
            st.success("✅ 检索完成！为您匹配到以下救命方案：")
            
            st.markdown("""
            ### 🎯 AI 诊断与推荐路径
            **你的痛点：** 缺乏供应链模型基础，备考时间极短 (不到一周)。
            
            **AI 推荐资源组合：**
            1. **《供应链核心模型 3小时速成版 (含手绘图解)》** - 匹配度 99% - 匿名卖家出品
               * **AI 质检摘要：** 该笔记摒弃了复杂推导，直接给出应试公式和 5 道必考母题，极度适合突击。
            2. **《2023年往届期末考卷真题回忆》** - 匹配度 90%
            
            **💡 AI 备考建议：** 建议先花 3 小时消化图解笔记，直接背诵框架，然后立刻默写往届真题中的计算题部分。
            """)
        else:
            st.warning("请先输入您的烦心事哦！")

# --- Tab 3: 发布资源 ---
with tab3:
    st.subheader("📤 将你的知识变现")
    with st.form("upload_form"):
        res_title = st.text_input("资源标题")
        res_desc = st.text_area("资源描述 (包含哪些干货？)")
        st.file_uploader("上传文件 (PDF/Word/ZIP)")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.number_input("定价 (学分)", min_value=0, max_value=500, value=20)
        with col_b:
            st.selectbox("发布身份", ["使用匿名身份 (保护隐私)", "使用实名身份 (建立个人品牌)"])
            
        submitted = st.form_submit_button("提交 AI 审核并上架")
        if submitted:
            st.info("🤖 AI 正在对您的文件进行脱敏检查（去除个人隐私）和质量评估...")
            time.sleep(1.5)
            st.success("✨ 审核通过！您的资源被 AI 评定为「高质量原创」，已获得首页流量倾斜！")