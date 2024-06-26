js_sql = {
    "activities": [
        {
            "alias": "店铺抽奖-JK",
            "name": "jd_dpcj.py",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=DPCJID",
            "re_url": "shopId=(\\d+)",
            "head_url": "shop/lottery",
            "cutting": "&",
            "value1": "export DPCJID"
        },
        {
            "alias": "邀好友赢大礼",
            "name": "jd_inviteFriendsGift.py",
            "match_url": "https://prodev.m.jd.com/mall/active/index.html?code=jd_inv_authorCode",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export jd_inv_authorCode"
        },
        {
            "alias": "jinggeng邀请入会有礼",
            "name": "jd_jinggengInvite.py",
            "match_url": "https://jinggeng-isv.isvjcloud.com/ql/front/showInviteJoin?id=#0&user_id=#1",
            "re_url": "activityId=(\\w+)",
            "head_url": "ql/front/showInviteJoin",
            "cutting": "&",
            "value1": "export jinggengInviteJoin"
        },
        {
            "alias": "通用开卡-joinCommon系列",
            "name": "jd_joinCommon_opencard.py",
            "match_url": "https://lzdz1-isv.isvjcloud.com/m/unite/dzlh0001?activityId=#0&venderId=#1",
            "re_url": "activityId=(\\w+)&venderId=(\\d+)",
            "head_url": "wxShopGift/activity|m/unite",
            "cutting": "&",
            "value1": "export jd_joinCommonId"
        },
        {
            "alias": "jd_lzkjInteract邀请有礼",
            "name": "jd_lzkjInteract.py",
            "match_url": "jd_lzkjInteractUrl",
            "re_url": "(https://.*?activityType=10070.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkjInteractUrl"
        },
        {
            "alias": "jd_lzkjInteract加购有礼",
            "name": "jd_lzkjInteractAddCart.py",
            "match_url": "jd_lzkjInteractAddCartUrl",
            "re_url": "(https://.*?activityType=10024.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkjInteractAddCartUrl"
        },
        {
            "alias": "jd_lzkjInteract关注有礼",
            "name": "jd_lzkjInteractFollow.py",
            "match_url": "jd_lzkjInteractFollowUrl",
            "re_url": "(https.*?activityType=(?:10069|10053)&templateId=\\w+&activityId=\\w+)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkjInteractFollowUrl"
        },
        {
            "alias": "店铺会员礼包-JK",
            "name": "jd_shopCollectGift.py",
            "match_url": "https://shop.m.jd.com/shop/home?shopId=jd_shopCollectGiftId",
            "re_url": "shopId=(\\w+)",
            "head_url": "shop/home",
            "value1": "export jd_shopCollectGiftId"
        },
        {
            "alias": "关注有礼-JK",
            "name": "jd_shopFollowGift.py",
            "value1": "export jd_shopFollowGiftId"
        },
        {
            "alias": "通用开卡-shopLeague系列脚本",
            "name": "jd_shopLeague_opencard.py",
            "match_url": "https://lzdz1-isv.isvjd.com/dingzhi/shop/league/activity?activityId=jd_shopLeagueId",
            "re_url": "activityId=(\\w+)",
            "head_url": "dingzhi/shop",
            "value1": "export jd_shopLeagueId"
        },
        {
            "alias": "生日礼包-JK",
            "name": "jd_wxBirthGifts.py",
            "match_url": "https://cjhy-isv.isvjcloud.com/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_wxBirthGiftsId",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "value1": "export jd_wxBirthGiftsId"
        },
        {
            "alias": "盖楼有礼-JK",
            "name": "jd_wxBulidActivity.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxBuildActivity/activity?activityId=jd_wxBulidActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxBuildActivity/activity",
            "value1": "export jd_wxBulidActivityId"
        },
        {
            "alias": "加购有礼-监控脚本",
            "name": "jd_wxCollectionActivity.py",
            "match_url": "jd_wxCollectionActivityUrl",
            "re_url": ".*",
            "head_url": "wxCollectionActivity/activity",
            "value1": "export jd_wxCollectionActivityUrl"
        },
        {
            "alias": "完善信息有礼-JK",
            "name": "jd_wxCompleteInfo.py",
            "match_url": "https://cjhy-isv.isvjcloud.com/wx/completeInfoActivity/view/activity?activityId=#0&venderId=#1",
            "re_url": "activityId=(\\w+)&venderId=(\\w+)",
            "head_url": "wx/completeInfoActivity",
            "cutting": "&",
            "value1": "export jd_wxCompleteInfoId"
        },
        {
            "alias": "关注店铺有礼-JK",
            "name": "jd_wxShopFollow.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_wxShopFollowId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "value1": "export jd_wxShopFollowId"
        },
        {
            "alias": "店铺特效关注有礼-监控脚本",
            "name": "jd_wxShopGift.py",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_wxShopGiftId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "value1": "export jd_wxShopGiftId"
        },
        {
            "alias": "入会开卡领取礼包(通用)",
            "name": "jd_card_force.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxInviteActivity/openCard/invitee/442818?activityId=VENDER_ID",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxInviteActivity/openCard",
            "value1": "export VENDER_ID"
        },
        {
            "alias": "cjhy完善信息",
            "name": "jd_cjhy_completeInfoActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wx/completeInfoActivity/view/activity?activityId=jd_cjhy_completeInfoActivity_Ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "wx/completeInfoActivity",
            "cutting": "&",
            "value1": "export jd_cjhy_completeInfoActivity_Ids"
        },
        {
            "alias": "cjhy每日抢",
            "name": "jd_cjhy_daily.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/activity/daily/wx/indexPage1?activityId=jd_cjhy_daily_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_daily_ids"
        },
        {
            "alias": "cjhy七日签到",
            "name": "jd_cjhy_sevenDay.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/sign/sevenDay/signActivity?activityId=jd_cjhy_sevenDay_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/sevenDay",
            "type_url": "cj",
            "cutting": "&",
            "value1": "export jd_cjhy_sevenDay_ids"
        },
        {
            "alias": "cjhy签到有礼",
            "name": "jd_cjhy_signActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/sign/signActivity?activityId=jd_cjhy_signActivity_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/signActivity",
            "value1": "export jd_cjhy_signActivity_ids"
        },
        {
            "alias": "cjhy加购物车抽奖",
            "name": "jd_cjhy_wxCollectionActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxCollectionActivity/activity?activityId=jd_cjhy_wxCollectionActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectionActivity/activity",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxCollectionActivityId"
        },
        {
            "alias": "cjhy幸运抽奖",
            "name": "jd_cjhy_wxDrawActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxDrawActivity/activity?activityId=jd_cjhy_wxDrawActivity_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_cjhy_wxDrawActivity_Id"
        },
        {
            "alias": "cjhy游戏活动",
            "name": "jd_cjhy_wxGameActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxGameActivity/activity?activityId=jd_cjhy_wxGameActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxGameActivity/activity",
            "cutting": "cj",
            "value1": "export jd_cjhy_wxGameActivity_activityId"
        },
        {
            "alias": "cjhy知识超人",
            "name": "jd_cjhy_wxKnowledgeActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxKnowledgeActivity/activity?activityId=jd_cjhy_wxKnowledgeActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxKnowledgeActivity/activity",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxKnowledgeActivity_activityId"
        },
        {
            "alias": "cjhy生日礼",
            "name": "jd_cjhy_wxMcLevelAndBirthGifts.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_cjhy_wxMcLevelAndBirthGifts_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxMcLevelAndBirthGifts_ids"
        },
        {
            "alias": "cjhy积分兑换京豆",
            "name": "jd_cjhy_wxPointShopView.js",
            "match_url": "jd_cjhy_wxMcLevelAndBirthGifts_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxPointShopView",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxPointShopView_url"
        },
        {
            "alias": "cjhy关注店铺有礼",
            "name": "jd_cjhy_wxShopFollowActivity.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_cjhy_wxShopFollowActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxShopFollowActivity_activityId"
        },
        {
            "alias": "cjhy店铺礼包",
            "name": "jd_cjhy_wxShopGift.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_cjhy_wxShopGift_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "cutting": "&",
            "type_url": "cj",
            "value1": "export jd_cjhy_wxShopGift_ids"
        },
        {
            "alias": "cj组队瓜分",
            "name": "jd_cjhydz_wxTeam.js",
            "match_url": "https://cjhydz-isv.isvjcloud.com/wxTeam/activity?activityId=jd_cjhydz_wxTeam_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxTeam/activity",
            "type_url": "cj",
            "js_level": 4,
            "value1": "export jd_cjhydz_wxTeam_Id"
        },
        {
            "alias": "店铺签到",
            "name": "jd_dpqd.js",
            "match_url": "https://h5.m.jd.com/babelDiy/Zeus/2PAAf74aG3D61qvfKUM5dxUssJQ9/index.html?token=DPQDTK",
            "re_url": "token=(\\w+)",
            "cutting": "&",
            "head_url": "babelDiy/Zeus",
            "value1": "export DPQDTK"
        },
        {
            "alias": "店铺签到-定时",
            "name": "jd_dpqd_own.js",
            "match_url": "https://h5.m.jd.com/babelDiy/Zeus/2PAAf74aG3D61qvfKUM5dxUssJQ9/index.html?token=dpqd_token_own",
            "re_url": "token=(\\w+)",
            "cutting": "&",
            "head_url": "babelDiy/Zeus",
            "value1": "export dpqd_token_own"
        },
        {
            "alias": "常规店铺签到监控",
            "name": "jd_dpqd_monitor.js",
            "match_url": "https://h5.m.jd.com/babelDiy/Zeus/2PAAf74aG3D61qvfKUM5dxUssJQ9/index.html?token=DPQDTK",
            "re_url": "token=(\\w+)",
            "cutting": "&",
            "js_level": 4,
            "head_url": "babelDiy/Zeus",
            "value1": "export jd_dpqd_monitor_token"
        },
        {
            "alias": "loreal_10001累计签到有好礼",
            "name": "jd_lzkj_10001_ljqdcj.js",
            "cutting": "&",
            "value1": "export jd_loreal_10001_ljqdysl_Ids"
        },
        {
            "alias": "lzkj_10001累计签到有好礼",
            "name": "jd_loreal_10001_ljqdysl.js",
            "cutting": "&",
            "value1": "export jd_lzkj_10001_ljqdcj_Ids"
        },
        {
            "alias": "lzkj_10002连续签到有礼",
            "name": "jd_lzkj_10002_lxqdyl.js",
            "cutting": "&",
            "value1": "export jd_lzkj_10002_lxqdyl_Ids"
        },
        {
            "alias": "lzkj_10006_v1邀请入会有礼",
            "name": "jd_lzkj_10006_v1.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interaction/v1/index?activityType=10006&activityId=jd_lzkj_10006_v1_ids",
            "re_url": "activityType=10006.*?activityId=(\\w+)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10006_v1_ids"
        },
        {
            "alias": "lzkj_10023日历签到",
            "name": "jd_lzkj_10023_rlqd.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10023&activityId=jd_lzkj_10023_rlqd_Ids&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10023.*?activityId=\\w+.*)",
            "cutting": "&",
            "type_url": "lz",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_10023_rlqd_Ids"
        },
        {
            "alias": "lzkj_10024加购有礼",
            "name": "jd_lzkj_10024_jgyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10024&activityId=jd_lzkj_10024_jgyl_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10024.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10024_jgyl_activityId"
        },
        {
            "alias": "lzkj_10033组队瓜分",
            "name": "jd_lzkj_10033_zdgf.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10033&activityId=jd_lzkj_10033_zdgf_Ids&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10033.*?activityId=\\w+.*)",
            "cutting": "&",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10033_zdgf_Ids"
        },
        {
            "alias": "lzkj_10038邀请好友帮砍价",
            "name": "jd_lzkj_10038_lrkj.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10038&activityId=jd_lzkj_10038_lrkj_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10038.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10038_lrkj_activityId"
        },
        {
            "alias": "lzkj_10040签到",
            "name": "jd_lzkj_10040_qrqd.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10040&activityId=jd_lzkj_10040_qrqd_Ids&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10040.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10040_qrqd_Ids"
        },
        {
            "alias": "lzkj_10043分享有礼",
            "name": "jd_lzkj_10043_fxyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10043&activityId=jd_lzkj_10043_fxyl_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10043.*?activityId=\\w+",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10043_fxyl_activityId"
        },
        {
            "alias": "lzkj_10044投票有礼抽奖",
            "name": "jd_lzkj_10044_tpyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10044&activityId=jd_lzkj_10044_tpyl_Ids&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10044.*?activityId=\\w+.*)",
            "cutting": "&",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10044_tpyl_Ids"
        },
        {
            "alias": "lzkj_10047盖楼有",
            "name": "jd_lzkj_10047_glyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10047&activityId=jd_lzkj_10047_tpyl_Ids&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10047.*?activityId=\\w+.*)",
            "cutting": "&",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10047_glyl_Id"
        },
        {
            "alias": "lzkj_10053关注商品有礼",
            "name": "jd_lzkj_10053_gzspyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10053&activityId=jd_lzkj_10053_gzspyl_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10053.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10053_gzspyl_activityId"
        },
        {
            "alias": "lzkj_10058店铺礼包",
            "name": "jd_lzkj_10058_dplb.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10058&activityId=jd_lzkj_10058_dplb_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10058.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10058_dplb_activityId"
        },
        {
            "alias": "lzkj_10069关注店铺有礼",
            "name": "jd_lzkj_10069_gzyl.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&activityId=jd_lzkj_10069_gzyl_activityId&nodeId=101001&prd=cjwx",
            "re_url": "(https.*?activityType=10069.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10069_gzyl_activityId"
        },
        {
            "alias": "lzkj_10070_v1邀请好友入会",
            "name": "jd_lzkj_10070_v1.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interaction/v1/index?activityType=10069&activityId=jd_lzkj_10070_v1_idsx",
            "re_url": "(https.*?prod/cc/interaction/v1.*?activityType=10069.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "cutting": "&",
            "value1": "export jd_lzkj_10070_v1_ids"
        },
        {
            "alias": "lzkj_10070邀请好友入会",
            "name": "jd_lzkj_10070_yqhyrh.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10069&activityId=jd_lzkj_10070_yqhyrh_activityId",
            "re_url": "(https.*?activityType=10070.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "type_url": "lz",
            "value1": "export jd_lzkj_10070_yqhyrh_activityId"
        },
        {
            "alias": "lzkj_10079积分兑换",
            "name": "jd_lzkj_10079_jfdh.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/prod/cc/interactsaas/index?activityType=10079&activityId=jd_lzkj_10079_jfdh_Ids",
            "cutting": "&",
            "type_url": "lz",
            "re_url": "(https.*?activityType=10079.*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_10079_jfdh_Ids"
        },
        {
            "alias": "lzkj_100 抽奖",
            "name": "jd_lzkj_100_draw.js",
            "match_url": "jd_lzkj_100_draw_urls",
            "cutting": "@",
            "type_url": "lz",
            "re_url": "(https.*?activityType=(!?10020|10021|10026|10031|10041|10042|10046|10054|10062|10063|10073|10080).*?activityId=\\w+.*)",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_100_draw_urls"
        },
        {
            "alias": "lzkj每日抢",
            "name": "jd_lzkj_daily.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/activity/daily/wx/indexPage?activityId=jd_lzkj_daily_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "activity/daily",
            "type_url": "lz",
            "cutting": "&",
            "value1": "export jd_lzkj_daily_ids"
        },
        {
            "alias": "通用抽奖机",
            "name": "jd_lottery.js",
            "match_url": "https://jdjoy.jd.com/module/task/draw/get?configCode=JD_Lottery",
            "re_url": "configCode=(\\w+)",
            "head_url": "module/task",
            "value1": "export JD_Lottery"
        },
        {
            "alias": "lzkj七日签到",
            "name": "jd_lzkj_sevenDay.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/sign/sevenDay/signActivity?activityId=jd_lzkj_sevenDay_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/sevenDay",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_sevenDay_ids"
        },
        {
            "alias": "lzkj签到有礼",
            "name": "jd_lzkj_signActivity2.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/sign/signActivity2?activityId=jd_lzkj_signActivity2_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "sign/signActivity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_signActivity2_ids"
        },
        {
            "alias": "lzkj v2 生日礼包",
            "name": "jd_lzkj_v2_birthday.js",
            "match_url": "jd_lzkj_v2_birthday_urls",
            "re_url": "(https://.*?prod/cc/interaction/v2/20002.*?)",
            "head_url": "prod/cc",
            "cutting": "@",
            "type_url": "lz",
            "value1": "export jd_lzkj_v2_birthday_urls"
        },
        {
            "alias": "lzkj v2 完善信息",
            "name": "jd_lzkj_v2_completeInfo.js",
            "match_url": "jd_lzkj_v2_completeInfo_urls",
            "re_url": "(https://.*?prod/cc/interaction/v2/10049.*?)",
            "head_url": "prod/cc",
            "cutting": "@",
            "type_url": "lz",
            "value1": "export jd_lzkj_v2_completeInfo_urls"
        },
        {
            "alias": "lzkj v2 抽奖",
            "name": "jd_lzkj_v2_draw.js",
            "match_url": "jd_lzkj_v2_draw_urls",
            "re_url": "(https://.*?prod/cc/interaction/v2/(!?10020|10021|10031|30003).*?)",
            "head_url": "prod/cc",
            "cutting": "@",
            "type_url": "lz",
            "value1": "export jd_lzkj_v2_draw_urls"
        },
        {
            "alias": "lzkj v2 签到",
            "name": "jd_lzkj_v2_sign.js",
            "match_url": "jd_lzkj_v2_sign_urls",
            "re_url": "(https://.*?prod/cc/interaction/v2/(!?10023/|10001/|10003/).*?)",
            "head_url": "prod/cc",
            "cutting": "@",
            "type_url": "lz",
            "value1": "export jd_lzkj_v2_sign_urls"
        },
        {
            "alias": "lzkj加购物车抽奖",
            "name": "jd_lzkj_wxCollectionActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxCollectionActivity/activity2?activityId=jd_lzkj_wxCollectionActivityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectionActivity/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxCollectionActivityId"
        },
        {
            "alias": "lzkj幸运抽大奖通用活动",
            "name": "jd_lzkj_wxDrawActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/lzclient/1685415463857/cjwx/common/entry.html?activityId=jd_lzkj_wxDrawActivity_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "lzclient",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxDrawActivity_Id"
        },
        {
            "alias": "lzkj关注店铺有礼",
            "name": "jd_lzkj_wxShopFollowActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopFollowActivity/activity?activityId=jd_lzkj_wxShopFollowActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopFollowActivity/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxShopFollowActivity_activityId"
        },
        {
            "alias": "lzkj店铺礼包",
            "name": "jd_lzkj_wxShopGift.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxShopGift/activity?activityId=jd_lzkj_wxShopGift_ids",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShopGift/activity",
            "cutting": "&",
            "type_url": "lz",
            "value1": "export jd_lzkj_wxShopGift_ids"
        },
        {
            "alias": "大牌联合通用开卡",
            "name": "jd_opencardDPLHTY.js",
            "match_url": "https://jinggengjcq-isv.isvjcloud.com/jdbeverage/pages/oC202301010wee/oC202301010wee?actId=DPLHTY",
            "re_url": "actId=(\\w+)",
            "head_url": "jdbeverage/pages",
            "value1": "export DPLHTY"
        },
        {
            "alias": "常规卡通用",
            "name": "jd_opencard_common.js",
            "match_url": "https://lzdz1-isv.isvjcloud.com/dingzhi/joinCommon/activity/activity?activityId=jd_lzdz1_joinCommon_Id",
            "re_url": "activityId=(\\w+)",
            "head_url": "dingzhi/joinCommon",
            "type_url": "lz",
            "value1": "export jd_lzdz1_joinCommon_Id"
        },
        {
            "alias": "超店通用",
            "name": "jd_opencard_shopLeague.js",
            "type_url": "lz",
            "value1": "export jd_lzdz1_shopLeague_Id"
        },
        {
            "alias": "翻牌签到",
            "name": "jd_sendbeans.js",
            "match_url": "jd_sendbeans_urls",
            "head_url": "jump/index",
            "cutting": "&",
            "value1": "export jd_sendbeans_urls"
        },
        {
            "alias": "店铺礼包",
            "name": "jd_shopGifts.js",
            "value1": "export jd_shopGifts_ids"
        },
        {
            "alias": "店铺抽奖",
            "name": "jd_shop_draw.js",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=jd_shop_draw_ids",
            "re_url": "shopId=(\\w+)",
            "cutting": "&",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_shop_draw_ids"
        },
        {
            "alias": "txzj 加购有礼",
            "name": "jd_txzj_cart_item.js",
            "match_url": "https://txzj-isv.isvjcloud.com/cart_item/home?a=jd_txzj_cart_item_id",
            "re_url": "a=(\\w+)",
            "head_url": "cart_item/home",
            "value1": "export jd_txzj_cart_item_id"
        },
        {
            "alias": "txzj 关注有礼",
            "name": "jd_txzj_collect_item.js",
            "match_url": "https://txzj-isv.isvjcloud.com/collect_item/home?a=jd_txzj_collect_item_id",
            "re_url": "a=(\\w+)",
            "head_url": "collect_item/home",
            "value1": "export jd_txzj_collect_item_id"
        },
        {
            "alias": "txzj抽奖",
            "name": "jd_txzj_lottery.js",
            "match_url": "https://txzj-isv.isvjcloud.com/lottery/home?a=jd_txzj_collect_item_id",
            "re_url": "a=(\\w+)",
            "head_url": "lottery/home",
            "value1": "export jd_txzj_collect_item_id"
        },
        {
            "alias": "txzj 签到",
            "name": "jd_txzj_sign_in.js",
            "match_url": "https://txzj-isv.isvjcloud.com/sign_in/home?a=jd_txzj_sign_in_id",
            "re_url": "a=(\\w+)",
            "cutting": "&",
            "head_url": "sign_in/home",
            "value1": "export jd_txzj_sign_in_id"
        },
        {
            "alias": "微定制瓜分福袋-加密",
            "name": "jd_wdzfd.js",
            "match_url": "jd_wdzfd_activityUrl/microDz/invite/openLuckBag/wx/view/index/8882761?activityId=jd_wdzfd_activityId",
            "re_url": "(https://.*?com).*?activityId=(\\w+)",
            "head_url": "microDz/invite",
            "value1": "export jd_wdzfd_activityUrl",
            "value2": "export jd_wdzfd_activityId"
        },
        {
            "alias": "微信红包团",
            "name": "jd_wechat_openGroup.js",
            "value1": "export jd_wechat_openGroup_id"
        },
        {
            "alias": "关注有礼-自动解析通用",
            "name": "jd_whx_drawShopGift.js",
            "value1": "export whx_drawShopGift"
        },
        {
            "alias": "盖楼有礼（超级无线）",
            "name": "jd_wxBuildActivity.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxBuildActivity/activity?activityId=jd_wxBuildActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxBuildActivity/activity",
            "value1": "export jd_wxBuildActivity_activityId"
        },
        {
            "alias": "购物车锦鲤（超级无线）",
            "name": "jd_wxCartKoi.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxCartKoi/cartkoi/activity?activityId=jd_wxCartKoi_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCartKoi/cartkoi",
            "value1": "export jd_wxCartKoi_activityId"
        },
        {
            "alias": "集卡有礼（超级无线）",
            "name": "jd_wxCollectCard.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxCollectCard/activity/activity?activityId=jd_wxCollectCard_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxCollectCard/activity",
            "value1": "export jd_wxCollectCard_activityId"
        },
        {
            "alias": "加购有礼通用",
            "name": "jd_wxCollectionActivity.js",
            "match_url": "jd_wxCollectionActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wxCollectionActivity/activity",
            "value1": "export jd_wxCollectionActivity_activityUrl"
        },
        {
            "alias": "加购物车抽奖",
            "name": "jd_wxCollectionActivity2.js",
            "match_url": "https://lzkj-isv.isvjcloud.com/wxgame/activity?activityId=ACTIVITY_ID",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxgame/activity",
            "value1": "export ACTIVITY_ID"
        },
        {
            "alias": "粉丝互动（超级无线）",
            "name": "jd_wxFansInterActionActivity.js",
            "match_url": "https://lzkjdz-isv.isvjd.com/wxFansInterActionActivity/activity?activityId=jd_wxFansInterActionActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxFansInterActionActivity/activity",
            "value1": "export jd_wxFansInterActionActivity_activityId"
        },
        {
            "alias": "游戏赢大礼（超级无线/超级会员）",
            "name": "jd_wxGameActivity.js",
            "match_url": "jd_wxGameActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wxGameActivity/activity",
            "value1": "export jd_wxGameActivity_activityUrl"
        },
        {
            "alias": "知识超人（超级无线/超级会员）",
            "name": "jd_wxKnowledgeActivity.js",
            "match_url": "jd_wxKnowledgeActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wxKnowledgeActivity/activity",
            "value1": "export jd_wxKnowledgeActivity_activityUrl"
        },
        {
            "alias": "生日礼包/会员等级礼包（超级会员）",
            "name": "jd_wxMcLevelAndBirthGifts.js",
            "match_url": "https://cjhy-isv.isvjcloud.com/mc/wxMcLevelAndBirthGifts/activity?activityId=jd_wxMcLevelAndBirthGifts_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "mc/wxMcLevelAndBirthGifts",
            "value1": "export jd_wxMcLevelAndBirthGifts_activityId"
        },
        {
            "alias": "读秒拼手速（超级无线）",
            "name": "jd_wxSecond.js",
            "match_url": "https://lzkjdz-isv.isvjd.com/wxSecond/activity/activity?activityId=jd_wxSecond_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxSecond/activity",
            "value1": "export jd_wxSecond_activityId"
        },
        {
            "alias": "分享有礼（超级无线）",
            "name": "jd_wxShareActivity.js",
            "match_url": "https://lzkjdz-isv.isvjcloud.com/wxShareActivity/activity?activityId=jd_wxShareActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxShareActivity/activity",
            "value1": "export jd_wxShareActivity_activityId"
        },
        {
            "alias": "关注店铺有礼（超级无线/超级会员）",
            "name": "jd_wxShopFollowActivity.js",
            "match_url": "jd_wxShopFollowActivity_activityUrl",
            "re_url": "(https://.*?activityId=\\w+.*)",
            "head_url": "wxShopFollowActivity/activity",
            "value1": "export jd_wxShopFollowActivity_activityUrl"
        },
        {
            "alias": "店铺礼包（超级无线/超级会员）",
            "name": "jd_wxShopGift.js",
            "match_url": "jd_wxShopGift_activityUrl",
            "re_url": "(https://.*?activityId=.*)",
            "head_url": "wxShopGift/activity",
            "value1": "export jd_wxShopGift_activityUrl"
        },
        {
            "alias": "组队瓜分奖品（超级无线/超级会员）",
            "name": "jd_wxTeam.js",
            "match_url": "jd_wxTeam_activityUrl",
            "re_url": ".*",
            "head_url": "wxTeam/activity",
            "value1": "export jd_wxTeam_activityUrl"
        },
        {
            "alias": "让福袋飞（超级无线）",
            "name": "jd_wxUnPackingActivity.js",
            "match_url": "https://lzkjdz-isv.isvjd.com/wxUnPackingActivity/activity/activity?activityId=jd_wxUnPackingActivity_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxUnPackingActivity/activity",
            "value1": "export jd_wxUnPackingActivity_activityId"
        },
        {
            "alias": "无线游戏（超级无线）",
            "name": "jd_wxgame.js",
            "match_url": "https://lzkj-isv.isvjd.com/wxgame/activity/activity?activityId=jd_wxgame_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxgame/activity",
            "value1": "export jd_wxgame_activityId"
        },
        {
            "alias": "惊喜开盲盒（京耕）",
            "name": "jd_jinggeng_blindBox.js",
            "match_url": "jd_jinggeng_blindBox_url",
            "re_url": ".*",
            "head_url": "ql/front/loadBlindBox",
            "value1": "export jd_jinggeng_blindBox_url"
        },
        {
            "alias": "加购有礼（京耕）",
            "name": "jd_jinggeng_cart.js",
            "match_url": "jd_jinggeng_cart_url",
            "re_url": ".*",
            "head_url": "ql/front/showCart",
            "value1": "export jd_jinggeng_cart_url"
        },
        {
            "alias": "积分抽奖（京耕）",
            "name": "jd_jinggeng_showDrawOne.js",
            "match_url": "jd_jinggeng_drawOne_url",
            "re_url": ".*",
            "head_url": "ql/front/showDrawOne",
            "value1": "export jd_jinggeng_drawOne_url"
        },
        {
            "alias": "积分兑换（京耕）",
            "name": "jd_jinggeng_exchangeActDetail.js",
            "match_url": "jd_jinggeng_exchangeActDetail_url",
            "re_url": ".*",
            "head_url": "ql/front/exchangeActDetail",
            "value1": "export jd_jinggeng_exchangeActDetail_url"
        },
        {
            "alias": "关注店铺有礼（京耕）",
            "name": "jd_jinggeng_favoriteShop.js",
            "match_url": "jd_jinggeng_favoriteShop_url",
            "re_url": ".*",
            "head_url": "ql/front/showFavoriteShop",
            "value1": "export jd_jinggeng_favoriteShop_url"
        },
        {
            "alias": "盖楼有礼（京耕）",
            "name": "jd_jinggeng_floor.js",
            "match_url": "jd_jinggeng_floor_url",
            "re_url": ".*",
            "head_url": "ql/front/floor",
            "value1": "export jd_jinggeng_floor_url"
        },
        {
            "alias": "完善有礼（京耕）",
            "name": "jd_jinggeng_perfectInformation.js",
            "match_url": "jd_jinggeng_perfectInformation_url",
            "re_url": ".*",
            "head_url": "ql/front/showPerfectInformation",
            "value1": "export jd_jinggeng_perfectInformation_url"
        },
        {
            "alias": "签到有礼（京耕）",
            "name": "jd_jinggeng_sign.js",
            "match_url": "jd_jinggeng_sign_url",
            "re_url": ".*",
            "head_url": "ql/front/showSign",
            "value1": "export jd_jinggeng_sign_url"
        },
        {
            "alias": "幸运抽奖（京耕）",
            "name": "jd_jinggeng_taskDraw.js",
            "match_url": "jd_jinggeng_taskDraw_url",
            "re_url": ".*",
            "head_url": "ql/front/showTaskDraw",
            "value1": "export jd_jinggeng_taskDraw_url"
        },
        {
            "alias": "加购有礼（超级无线）",
            "name": "jd_lzkj_loreal_cart.js",
            "match_url": "jd_lzkj_loreal_cart_url",
            "re_url": ".*activityType=10024.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_cart_url"
        },
        {
            "alias": "每日抢好礼（超级无线）",
            "name": "jd_lzkj_loreal_dailyGrabs.js",
            "match_url": "jd_lzkj_loreal_dailyGrabs_url",
            "re_url": ".*activityType=10022.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_dailyGrabs_url"
        },
        {
            "alias": "签到有礼（超级无线）",
            "name": "jd_lzkj_loreal_daySign.js",
            "match_url": "jd_lzkj_loreal_daySign_url",
            "re_url": ".*activityType=(?:10023|10040).*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_daySign_url"
        },
        {
            "alias": "幸运抽奖（超级无线）",
            "name": "jd_lzkj_loreal_draw.js",
            "match_url": "jd_lzkj_loreal_draw_url",
            "re_url": ".*activityType=(?:10001|10004|10020|10021|10026|10031|10041|10042|10046|10054|10062|10063|10073|10080).*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_draw_url"
        },
        {
            "alias": "关注商品有礼（超级无线）",
            "name": "jd_lzkj_loreal_followGoods.js",
            "match_url": "jd_lzkj_loreal_followGoods_url",
            "re_url": ".*activityType=10053.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_followGoods_url"
        },
        {
            "alias": "邀请关注店铺有礼（超级无线）",
            "name": "jd_lzkj_loreal_inviteFollowShop.js",
            "match_url": "jd_lzkj_loreal_inviteFollowShop_url",
            "re_url": ".*activityType=10068.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_inviteFollowShop_url"
        },
        {
            "alias": "知识超人（超级无线）",
            "name": "jd_lzkj_loreal_know.js",
            "match_url": "jd_lzkj_loreal_know_url",
            "re_url": ".*activityType=10039.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_know_url"
        },
        {
            "alias": "关注店铺有礼（超级无线）",
            "name": "jd_lzkj_loreal_lkFollowShop.js",
            "match_url": "jd_lzkj_loreal_lkFollowShop_url",
            "re_url": ".*activityType=10069.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_lkFollowShop_url"
        },
        {
            "alias": "组队瓜分奖品（超级无线）",
            "name": "jd_lzkj_loreal_organizeTeam.js",
            "match_url": "jd_lzkj_loreal_organizeTeam_url",
            "re_url": ".*activityType=10033.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_organizeTeam_url"
        },
        {
            "alias": "完善有礼（超级无线）",
            "name": "jd_lzkj_loreal_perfectInfo.js",
            "match_url": "jd_lzkj_loreal_perfectInfo_url",
            "re_url": ".*activityType=10049.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_perfectInfo_url"
        },
        {
            "alias": "积分兑换（超级无线）",
            "name": "jd_lzkj_loreal_pointsExchange.js",
            "match_url": "jd_lzkj_loreal_pointsExchange_url",
            "re_url": ".*activityType=10079.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_pointsExchange_url"
        },
        {
            "alias": "店铺礼包（超级无线）",
            "name": "jd_lzkj_loreal_shopGift.js",
            "match_url": "jd_lzkj_loreal_shopGift_url",
            "re_url": ".*activityType=10058.*?activityId=\\w+.*?",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_loreal_shopGift_url"
        },
        {
            "alias": "生日礼包（超级无线V2）",
            "name": "jd_lzkj_v2_birthday.js",
            "match_url": "jd_lzkj_v2_birthday_url",
            "re_url": ".*cc/interaction/v2/20002/1001.*",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_v2_birthday_url"
        },
        {
            "alias": "幸运抽奖（超级无线V2）",
            "name": "jd_lzkj_v2_draw.js",
            "match_url": "jd_lzkj_v2_draw_url",
            "re_url": ".*cc/interaction/v2/(?:10020|10021|10031|30003)/.*",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_v2_draw_url"
        },
        {
            "alias": "完善有礼（超级无线V2）",
            "name": "jd_lzkj_v2_perfectInfo.js",
            "match_url": "jd_lzkj_v2_perfectInfo_url",
            "re_url": ".*cc/interaction/v2/10049/.*",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_v2_perfectInfo_url"
        },
        {
            "alias": "签到（超级无线V2）",
            "name": "jd_lzkj_v2_sign.js",
            "match_url": "jd_lzkj_v2_sign_url",
            "re_url": ".*cc/interaction/v2/(?:10001|10004|10023|10040|10002|10003)/.*",
            "head_url": "prod/cc",
            "value1": "export jd_lzkj_v2_sign_url"
        },
        {
            "alias": "超店会员福利社通用开卡",
            "name": "jd_opencard_shopleague.js",
            "match_url": "https://lzdz1-isv.isvjd.com/dingzhi/shop/league/activity?activityId=jd_opencard_shopleague_id",
            "re_url": "activityId=(\\w+)",
            "head_url": "dingzhi/shop",
            "value1": "export jd_opencard_shopleague_id"
        },
        {
            "alias": "积分兑换京豆（超级会员）",
            "name": "jd_pointExgBeans.js",
            "match_url": "jd_pointExgBeans_activityUrl",
            "re_url": ".*mc/wxPointShopView/pointExgBeans.*",
            "head_url": "mc/wxPointShopView",
            "value1": "export jd_pointExgBeans_activityUrl"
        },
        {
            "alias": "积分兑换E卡（超级会员）",
            "name": "jd_pointExgECard.js",
            "match_url": "jd_pointExgECard_activityUrl",
            "re_url": ".*mc/wxPointShopView/pointExgECard.*",
            "head_url": "mc/wxPointShopView",
            "value1": "export jd_pointExgECard_activityUrl"
        },
        {
            "alias": "积分兑换红包（超级会员）",
            "name": "jd_pointExgHb.js",
            "match_url": "jd_pointExgHb_activityUrl",
            "re_url": ".*mc/wxPointShopView/pointExgHb.*",
            "head_url": "mc/wxPointShopView",
            "value1": "export jd_pointExgHb_activityUrl"
        },
        {
            "alias": "积分兑换实物（超级会员）",
            "name": "jd_pointExgShiWu.js",
            "match_url": "jd_pointExgShiWu_activityUrl",
            "re_url": ".*mc/wxPointShopView/pointExgShiWu.*",
            "head_url": "mc/wxPointShopView",
            "value1": "export jd_pointExgShiWu_activityUrl"
        },
        {
            "alias": "邀好友赢大礼",
            "name": "jd_prodev.js",
            "match_url": "https://prodev.m.jd.com/mall/active/index.html?code=jd_prodev_actCode",
            "re_url": "code=(\\w+)",
            "head_url": "mall/active",
            "value1": "export jd_prodev_actCode"
        },
        {
            "alias": "店铺刮刮乐（刮一刮）",
            "name": "jd_shop_lottery.js",
            "match_url": "https://shop.m.jd.com/shop/lottery?shopId=jd_shopLottery_venderIds",
            "re_url": "shopId=(\\w+)",
            "head_url": "shop/lottery",
            "cutting": ",",
            "value1": "export jd_shopLottery_venderIds"
        },
        {
            "alias": "微信红包团",
            "name": "jd_wechat_openGroup.js",
            "value1": "export jd_wechat_openGroup_id"
        },
        {
            "alias": "完善信息有礼（超级会员）",
            "name": "jd_wx_completeInfoActivity.js",
            "match_url": "jd_wx_completeInfoActivity_activityUrl",
            "re_url": ".*",
            "head_url": "wx/completeInfoActivity",
            "value1": "export jd_wx_completeInfoActivity_activityUrl"
        },
        {
            "alias": "每日抢好礼（超级无线/超级会员）",
            "name": "jd_wx_completeInfoActivity.js",
            "match_url": "jd_wx_daily_url",
            "re_url": ".*",
            "head_url": "activity/daily",
            "value1": "export jd_wx_daily_url"
        },
        {
            "alias": "店铺抽奖（超级无线/超级会员）",
            "name": "jd_wx_draw.js",
            "match_url": "jd_wx_draw_url",
            "re_url": ".*",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_wx_draw_url"
        },
        {
            "alias": "店铺抽奖中心（超级无线）",
            "name": "jd_wx_drawCenter.js",
            "match_url": "https://lzkj-isv.isvjd.com/drawCenter/activity/activity?activityId=jd_wx_drawCenter_activityId",
            "re_url": "activityId=(\\w+)",
            "head_url": "wxDrawActivity/activity",
            "value1": "export jd_wx_drawCenter_activityId"
        },
        {
            "alias": "店铺签到监控（超级无线/超级会员）",
            "name": "jd_wx_shopSign.js",
            "match_url": "jd_wx_shopSign_activityUrl",
            "re_url": ".*",
            "head_url": "sign/sevenDay",
            "value1": "export jd_wx_shopSign_activityUrl"
        }
    ]
}