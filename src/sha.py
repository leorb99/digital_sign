h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a

hash_size = 128
block_size = 64
rounds = 16

def rote(n, num):
    n = n << num
    n = n | (n >> 32)
    return n & ((1 << 32) - 1)

def converter_bytes_para_palavras(bytes_lista):
    # Verifica se a lista tem 64 bytes
    if len(bytes_lista) != 64:
        raise ValueError("A lista deve ter exatamente 64 elementos (bytes).")
    
    # Cria uma lista de 16 palavras de 32 bits (4 bytes cada)
    palavras = [(
        (bytes_lista[i] << 24) | 
        (bytes_lista[i+1] << 16) | 
        (bytes_lista[i+2] << 8) | 
        bytes_lista[i+3]
    ) for i in range(0, len(bytes_lista), 4)]
    
    return palavras

def process_block(buffer: list, h: list):
    a = h[0]
    b = h[1]
    c = h[2]
    d = h[3]
    w = converter_bytes_para_palavras(buffer)
    for i in range(16):
        f = (b & c) | ((~b) & d)
        temp = (rote(a, 5) + f + d + w[i]) % 2**32
        d = c
        c = b
        b = a
        a = temp
    h[0] = (h[0] + a) % 2**32
    h[1] = (h[1] + b) % 2**32
    h[2] = (h[2] + c) % 2**32
    h[3] = (h[3] + d) % 2**32
    H = h[0] ^ h[1] ^ h[2] ^ h[3]
    return hex(H)

def sha(m: str):
    h = [h0, h1, h2, h3]
    buffer = [-1] * block_size
    i = 0
    msg = m.encode('utf-8')
    for byte in msg:
        if i < block_size:
            buffer[i] = byte
            i += 1
        else:
            process_block(buffer, h)
            i = 0
    
    buffer[i] = 0x80
    i += 1

    if i > 56:
        while i < block_size:
            buffer[i] = 0x00
            i += 1
        process_block(buffer, h)
        i = 0
    
    while i < 56:
        buffer[i] = 0x00
        i += 1
    
    buffer[63] = 0x40
    return process_block(buffer, h) 

print(sha('ooo'))

html = '''
<body data-theme="light" class="legacyBackground" data-react-helmet="data-theme,class" style="visibility: visible;">
        <div id="root"><div><div class="appBackground"><iframe name="adsOptOut-sync-iframe" referrerpolicy="strict-origin" sandbox="allow-scripts allow-same-origin" src="https://www.microsoft.com/store/XboxComMsCom3PAdsOptOutCookieSync.html" width="0" height="0" class="AdsOptOutSync-module__syncFrame___vfV8q"></iframe><div id="pageBannerContainer" class="PageBanner-module__bannerContainer___YuHV3 PageBanner-module__hidden___MkKJW"></div><section aria-label="Notifications alt+T" tabindex="-1" aria-live="polite" aria-relevant="additions text" aria-atomic="false"></section><div class="uhf-header static-header uhf-header-mode-full">    <div id="headerArea" class="uhf" data-m="{&quot;cN&quot;:&quot;headerArea&quot;,&quot;cT&quot;:&quot;Area_coreuiArea&quot;,&quot;id&quot;:&quot;a1Body&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;Body&quot;}">
                <div id="headerRegion" data-region-key="headerregion" data-m="{&quot;cN&quot;:&quot;headerRegion&quot;,&quot;cT&quot;:&quot;Region_coreui-region&quot;,&quot;id&quot;:&quot;r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;a1&quot;}" style="overflow-x: visible;">

    <div id="headerUniversaHeaer" data-m="{&quot;cN&quot;:&quot;headerUniversalHeader&quot;,&quot;cT&quot;:&quot;Module_coreui-universalheader&quot;,&quot;id&quot;:&quot;m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;r1a1&quot;}" data-module-id="Category|headerRegion|coreui-region|headerUniversalHeader|coreui-universalheader" style="overflow-x: visible;">
        


                        <div data-m="{&quot;cN&quot;:&quot;cookiebanner_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;m1r1a1&quot;}" style="overflow-x: visible;">

<div id="uhfCookieAlert" data-locale="pt-br" style="overflow-x: visible;">
    <div id="msccBannerV2" style="overflow-x: visible;"></div>
</div>

                            
                        </div>




        <a id="uhfSkipToMain" class="m-skip-to-main" href="javascript:void(0)" data-href="#PageContent" tabindex="0" data-m="{&quot;cN&quot;:&quot;Skip to content_nonnav&quot;,&quot;id&quot;:&quot;nn2m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;m1r1a1&quot;}" style="overflow-x: visible;">Pular para o conteúdo principal</a>


<header class="c-uhfh context-uhf c-sgl-stck c-category-header" itemscope="itemscope" data-header-footprint="/XboxComUHF/Xboxcomheader, fromService: True" data-magict="true" itemtype="http://schema.org/Organization" style="overflow-x: visible;">
    <div class="theme-light js-global-head f-closed  global-head-cont" data-m="{&quot;cN&quot;:&quot;Universal Header_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;m1r1a1&quot;}" style="overflow-x: visible;">
        <div class="c-uhfh-gcontainer-st" style="overflow-x: visible;">
            <button type="button" class="c-action-trigger c-glyph glyph-global-nav-button" aria-label="All Microsoft expand to see list of Microsoft products and services" initialstate-label="All Microsoft expand to see list of Microsoft products and services" togglestate-label="Close All Microsoft list" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;Mobile menu button_nonnav&quot;,&quot;id&quot;:&quot;nn1c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;"></button>
            <button type="button" class="c-action-trigger c-glyph glyph-arrow-htmllegacy c-close-search" aria-label="Fechar pesquisa" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;Close Search_nonnav&quot;,&quot;id&quot;:&quot;nn2c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;"></button>
                    <a id="uhfLogo" class="c-logo c-sgl-stk-uhfLogo" itemprop="url" href="https://www.microsoft.com" aria-label="Microsoft" data-m="{&quot;cN&quot;:&quot;GlobalNav_Logo_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;">
                        <img alt="" itemprop="logo" class="c-image" src="https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png" role="presentation" aria-hidden="true" style="overflow-x: visible;">
                        <span itemprop="name" role="presentation" aria-hidden="true" style="overflow-x: visible;">Microsoft</span>
                    </a>
            <div class="f-mobile-title" style="overflow-x: visible;">
                <button type="button" class="c-action-trigger c-glyph glyph-chevron-left" aria-label="Ver mais opções de menu" data-m="{&quot;cN&quot;:&quot;Mobile back button_nonnav&quot;,&quot;id&quot;:&quot;nn4c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;"></button>
                <span data-global-title="Home page da Microsoft" class="js-mobile-title" style="overflow-x: visible;">Xbox</span>
                <button type="button" class="c-action-trigger c-glyph glyph-chevron-right" aria-label="Ver mais opções de menu" data-m="{&quot;cN&quot;:&quot;Mobile forward button_nonnav&quot;,&quot;id&quot;:&quot;nn5c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;"></button>
            </div>
                    <div class="c-show-pipe x-hidden-vp-mobile-st" style="overflow-x: visible;">
                        <a id="uhfCatLogo" class="c-logo c-cat-logo" href="https://www.xbox.com/pt-BR/?xr=mebarnav" aria-label="Xbox" itemprop="url" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_nav&quot;,&quot;id&quot;:&quot;n6c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;">
                                <img itemprop="cat-logo" alt="Xbox" src="https://uhf.microsoft.com/images/xbox/RW4ESm.png" aria-hidden="true" style="overflow-x: visible;">
                                <div class=".c-uhf-img-tooltip" style="overflow-x: visible;">
                                    <span class="c-uhf-tooltiptext" role="tooltip" style="overflow-x: visible;">Xbox Home</span>
                                </div>
                        </a>
                    </div>
                <div class="cat-logo-button-cont x-hidden" style="overflow-x: visible;">
                        <button type="button" id="uhfCatLogoButton" class="c-cat-logo-button c-cat-logo-img x-hidden" aria-expanded="false" aria-label="Xbox" data-m="{&quot;cN&quot;:&quot;Xbox_nonnav&quot;,&quot;id&quot;:&quot;nn7c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;">
                        </button>
                </div>



                    <nav id="uhf-g-nav" aria-label="Menu contextual" class="c-uhfh-gnav" data-m="{&quot;cN&quot;:&quot;Category nav_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;">
            <ul class="js-paddle-items" style="overflow-x: visible;">
                    <li class="single-link js-nav-menu x-hidden-none-mobile-vp uhf-menu-item" style="overflow-x: visible;">
                        <a class="c-uhf-nav-link" href="https://www.xbox.com/pt-BR/?xr=mebarnav" data-m="{&quot;cN&quot;:&quot;CatNav_Início_nav&quot;,&quot;id&quot;:&quot;n1c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;"> Início </a>
                    </li>
                                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="c-shellmenu_44" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Game_Pass​_nonnav&quot;,&quot;id&quot;:&quot;nn2c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Game Pass​</button>

                                <ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Game_Pass​_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Overview_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c3c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_45" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/xbox-game-pass?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Overview_nav&quot;,&quot;id&quot;:&quot;n1c1c3c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">Assine o Game Pass</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Browse_Games​​_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c3c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_46" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-game-pass/games?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Browse_Games​​_nav&quot;,&quot;id&quot;:&quot;n1c2c3c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">Buscar jogos​​</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Deals with Game Pass​_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c3c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Deals with Game Pass" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-game-pass/deals?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Deals with Game Pass​_nav&quot;,&quot;id&quot;:&quot;n1c3c3c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">Ofertas com o Game Pass</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Cloud_gaming​_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c3c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_48" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/cloud-gaming?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Cloud_gaming​_nav&quot;,&quot;id&quot;:&quot;n1c4c3c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c3c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox Cloud Gaming ​</a>
            
        </li>
                                                    
                                </ul>
                            </div>
                        </li>                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="c-shellmenu_49" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Games_nonnav&quot;,&quot;id&quot;:&quot;nn4c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos</button>

                                <ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Games home_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Games_home" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Games home_nav&quot;,&quot;id&quot;:&quot;n1c1c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Página inicial de jogos</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop all console games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c5c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_console_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/all-games/console?PlayWith=XboxSeriesX%7CS%2CXboxOne&amp;xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop all console games_nav&quot;,&quot;id&quot;:&quot;n1c2c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Ver todos os jogos digitais</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop all PC games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c5c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_PC_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/all-games/pc?PlayWith=PC&amp;xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop all PC games_nav&quot;,&quot;id&quot;:&quot;n1c3c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comprar todos os jogos para PC</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Cloud games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c5c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Cloud_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/play?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Cloud games_nav&quot;,&quot;id&quot;:&quot;n1c4c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Cloud Gaming</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox Play Anywhere_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c5c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_54" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/xbox-play-anywhere?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox Play Anywhere_nav&quot;,&quot;id&quot;:&quot;n1c5c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox Play Anywhere</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Free to play games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c5c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Free_play_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/free-to-play?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Free to play games_nav&quot;,&quot;id&quot;:&quot;n1c6c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos gratuitos</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Optimized games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c5c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Optimized_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/optimized?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Optimized games_nav&quot;,&quot;id&quot;:&quot;n1c7c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Otimizado para o Xbox&nbsp;Series&nbsp;X|S</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Backward compatible games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c5c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Backward_compatible_games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/backward-compatibility?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Backward compatible games_nav&quot;,&quot;id&quot;:&quot;n1c8c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos compatíveis com versões anteriores</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Sales u0026 Specials_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c5c8c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Sales_Specials" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/promotions/sales/sales-and-specials?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Sales u0026 Specials_nav&quot;,&quot;id&quot;:&quot;n1c9c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Vendas e ofertas especiais</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Redeem Code_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c10c5c8c3m1r1a1&quot;,&quot;sN&quot;:10,&quot;aN&quot;:&quot;c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Redeem_Code" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/redeem?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Redeem Code_nav&quot;,&quot;id&quot;:&quot;n1c10c5c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c10c5c8c3m1r1a1&quot;}" style="overflow-x: visible;">Resgatar código</a>
            
        </li>
                                                    
                                </ul>
                            </div>
                        </li>                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="Devices" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Devices_nonnav&quot;,&quot;id&quot;:&quot;nn6c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Dispositivos</button>

                                <ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Devices_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;All_devices_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="All_devices" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/devices?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_All_devices_nav&quot;,&quot;id&quot;:&quot;n1c1c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Explore todos os dispositivos</a>
            
        </li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;Consoles_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-Consoles-span" style="display: none; overflow-x: visible;" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Consoles_nonnav&quot;,&quot;id&quot;:&quot;nn1c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}">Consoles Xbox</span>
    <button id="uhf-navbtn-Consoles-button" type="button" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Consoles_nonnav&quot;,&quot;id&quot;:&quot;nn2c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Consoles Xbox</button>
    <ul aria-hidden="true" aria-labelledby="uhf-navspn-Consoles-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Meet_Xbox_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Meet_Xbox" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Meet_Xbox_nav&quot;,&quot;id&quot;:&quot;n1c3c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Conheça o Xbox Series X|S</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_Series_X_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_Series_X" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles/xbox-series-x?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_Series_X_nav&quot;,&quot;id&quot;:&quot;n1c4c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox Series X</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_Series_S_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_Series_S" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles/xbox-series-s?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_Series_S_nav&quot;,&quot;id&quot;:&quot;n1c5c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox Series S</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop_all_consoles_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_all_consoles" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles/all-consoles?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop_all_consoles_nav&quot;,&quot;id&quot;:&quot;n1c6c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Compre todos os consoles</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Compare_consoles_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Compare_consoles" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles/compare?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Compare_consoles_nav&quot;,&quot;id&quot;:&quot;n1c7c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Compare os consoles</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Where_to_buy_consoles_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Where_to_buy_consoles" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/where-to-buy?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Where_to_buy_consoles_nav&quot;,&quot;id&quot;:&quot;n1c8c2c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c2c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Onde comprar</a>
            
        </li>
    </ul>
    
</li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_on_PPC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c7c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_on_PC" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-on-pc?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_on_PPC_nav&quot;,&quot;id&quot;:&quot;n1c3c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox no PC</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_on_handhelds_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c7c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_on_handhelds" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-on-handhelds?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_on_handhelds_nav&quot;,&quot;id&quot;:&quot;n1c4c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox em dispositivos portáteis</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_on_mobile_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c7c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_on_mobile" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-on-mobile?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_on_mobile_nav&quot;,&quot;id&quot;:&quot;n1c5c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox em dispositivos móveis</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_on_TVs_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c7c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_on_TVs" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-on-tvs?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_on_TVs_nav&quot;,&quot;id&quot;:&quot;n1c6c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox nas TVs</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_on_VR_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c7c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox_on_VR" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-on-vr-headsets?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox_on_VR_nav&quot;,&quot;id&quot;:&quot;n1c7c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox em headsets de VR</a>
            
        </li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;Accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-Accessories-span" style="display: none; overflow-x: visible;" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Accessories_nonnav&quot;,&quot;id&quot;:&quot;nn1c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}">Acessórios Xbox</span>
    <button id="uhf-navbtn-Accessories-button" type="button" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Accessories_nonnav&quot;,&quot;id&quot;:&quot;nn2c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Acessórios Xbox</button>
    <ul aria-hidden="true" aria-labelledby="uhf-navspn-Accessories-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop_all_accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_all_accessories" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop_all_accessories_nav&quot;,&quot;id&quot;:&quot;n1c3c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Compre todos os acessórios</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Controllers_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Controllers" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav#controllers" data-m="{&quot;cN&quot;:&quot;CatNav_Controllers_nav&quot;,&quot;id&quot;:&quot;n1c4c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Controles</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Headsets_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Headsets" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav#headsets" data-m="{&quot;cN&quot;:&quot;CatNav_Headsets_nav&quot;,&quot;id&quot;:&quot;n1c5c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Fones de ouvido</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Storage_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Storage" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav#storage" data-m="{&quot;cN&quot;:&quot;CatNav_Storage_nav&quot;,&quot;id&quot;:&quot;n1c6c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Discos rígidos e armazenamento</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Mobile_accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Mobile_accessories" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav#mobile" data-m="{&quot;cN&quot;:&quot;CatNav_Mobile_accessories_nav&quot;,&quot;id&quot;:&quot;n1c7c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Acessório para jogos em dispositivos móveis</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Where_to_buy_accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Where_to_buy_accessories" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/where-to-buy?xr=shellnav#accessories" data-m="{&quot;cN&quot;:&quot;CatNav_Where_to_buy_accessories_nav&quot;,&quot;id&quot;:&quot;n1c8c8c7c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c8c7c8c3m1r1a1&quot;}" style="overflow-x: visible;">Onde comprar</a>
            
        </li>
    </ul>
    
</li>
                                                    
                                </ul>
                            </div>
                        </li>                        <li class="single-link js-nav-menu uhf-menu-item" style="overflow-x: visible;">
                            <a id="c-shellmenu_81" class="c-uhf-nav-link" href="https://www.xbox.com/pt-BR/play?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Jogar_nav&quot;,&quot;id&quot;:&quot;n8c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogar</a>
                        </li>
                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="Store" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Store_nonnav&quot;,&quot;id&quot;:&quot;nn9c8c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Loja</button>

                                <ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Store_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c10c8c3m1r1a1&quot;,&quot;sN&quot;:10,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop Games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_Games" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop Games_nav&quot;,&quot;id&quot;:&quot;n1c1c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comprar jogos</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop Game Pass_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c10c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_Game_Pass" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/xbox-game-pass?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop Game Pass_nav&quot;,&quot;id&quot;:&quot;n1c2c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comprar o Game Pass</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop Consoles_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c10c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_Consoles" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/consoles/all-consoles?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop Consoles_nav&quot;,&quot;id&quot;:&quot;n1c3c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comprar consoles</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop Accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c10c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_Accessories" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/accessories?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop Accessories_nav&quot;,&quot;id&quot;:&quot;n1c4c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">Compre acessórios</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Shop Deals_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c10c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Shop_Deals" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/promotions/sales/sales-and-specials?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Shop Deals_nav&quot;,&quot;id&quot;:&quot;n1c5c10c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c10c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comprar ofertas</a>
            
        </li>
                                                    
                                </ul>
                            </div>
                        </li>                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="c-shellmenu_88" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Community_nonnav&quot;,&quot;id&quot;:&quot;nn11c8c3m1r1a1&quot;,&quot;sN&quot;:11,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Comunidade</button>

                                <ul class="f-multi-column f-multi-column-2" data-class-idn="f-multi-column f-multi-column-2" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Community_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c12c8c3m1r1a1&quot;,&quot;sN&quot;:12,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;Community_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_89-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Community_nonnav&quot;,&quot;id&quot;:&quot;nn1c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c12c8c3m1r1a1&quot;}" role="heading" aria-level="2">Comunidade</span>
    <button id="uhf-navbtn-shellmenu_89-button" type="button" f-multi-parent="true" data-m="{&quot;cN&quot;:&quot;CatNav_Community_nonnav&quot;,&quot;id&quot;:&quot;nn2c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c1c12c8c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Comunidade</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_89-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;FanFest_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c1c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="FanFest" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/community/fanfest?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_FanFest_nav&quot;,&quot;id&quot;:&quot;n1c3c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c1c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">FanFest</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox News_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c1c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_91" class="js-subm-uhf-nav-link" href="https://news.xbox.com/pt-BR/?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox News_nav&quot;,&quot;id&quot;:&quot;n1c4c1c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c1c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Notícias do Xbox</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;For Everyone_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_92-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_For Everyone_nonnav&quot;,&quot;id&quot;:&quot;nn1c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" role="heading" aria-level="2">Para todos</span>
    <button id="uhf-navbtn-shellmenu_92-button" type="button" f-multi-parent="true" data-m="{&quot;cN&quot;:&quot;CatNav_For Everyone_nonnav&quot;,&quot;id&quot;:&quot;nn2c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Para todos</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_92-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Our philosophy_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_93" class="js-subm-uhf-nav-link" href="https://www.xbox.com/community/for-everyone?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Our philosophy_nav&quot;,&quot;id&quot;:&quot;n1c3c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Nossa filosofia</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Family hub_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_94" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/family-hub?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Family hub_nav&quot;,&quot;id&quot;:&quot;n1c4c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Family hub</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox Family Settings app_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Xbox Family Settings app" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/apps/family-settings-app?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Xbox Family Settings app_nav&quot;,&quot;id&quot;:&quot;n1c5c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Aplicativo Xbox Family Settings</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Accessible gaming_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_96" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/community/for-everyone/accessibility?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Accessible gaming_nav&quot;,&quot;id&quot;:&quot;n1c6c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos acessíveis</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Community standards_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_97" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/legal/community-standards?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Community standards_nav&quot;,&quot;id&quot;:&quot;n1c7c2c12c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c2c12c8c3m1r1a1&quot;}" style="overflow-x: visible;">Padrões da comunidade</a>
            
        </li>
    </ul>
    
</li>
                                                    
                                </ul>
                            </div>
                        </li>                        <li class="nested-menu uhf-menu-item" style="overflow-x: visible;">
                            <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                                <button type="button" id="c-shellmenu_98" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Support_nonnav&quot;,&quot;id&quot;:&quot;nn13c8c3m1r1a1&quot;,&quot;sN&quot;:13,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Suporte</button>

                                <ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Support_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c14c8c3m1r1a1&quot;,&quot;sN&quot;:14,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_SupportHome_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_99" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/" data-m="{&quot;cN&quot;:&quot;CatNav_Support_SupportHome_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c1c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Página inicial do suporte</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_XboxLiveStatus_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c14c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_100" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/xbox-live-status" data-m="{&quot;cN&quot;:&quot;CatNav_Support_XboxLiveStatus_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c2c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Status do Xbox</a>
            
        </li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;Support_HelpTopics_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-c-shellmenu_101-span" style="display: none; overflow-x: visible;" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Support_HelpTopics_MSXC_nonnav&quot;,&quot;id&quot;:&quot;nn1c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}">Tópicos da ajuda</span>
    <button id="uhf-navbtn-c-shellmenu_101-button" type="button" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Support_HelpTopics_MSXC_nonnav&quot;,&quot;id&quot;:&quot;nn2c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Tópicos da ajuda</button>
    <ul aria-hidden="true" aria-labelledby="uhf-navspn-c-shellmenu_101-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_AccountProfile_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_102" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/account-profile/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_AccountProfile_nav&quot;,&quot;id&quot;:&quot;n1c3c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Conta e perfil</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_SubscriptionsBilling_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_103" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/subscriptions-billing/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_SubscriptionsBilling_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c4c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Assinaturas e cobrança</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_HardwareNetworking_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_104" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/hardware-network/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_HardwareNetworking_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c5c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Hardware e rede</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_FamilyOnlineSafety_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_105" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/family-online-safety/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_FamilyOnlineSafety_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c6c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Família e segurança online</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_GamesApps_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_106" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/games-apps/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_GamesApps_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c7c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos e apps</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_FriendsSocialActivity_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_107" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/friends-social-activity/browse" data-m="{&quot;cN&quot;:&quot;CatNav_Support_FriendsSocialActivity_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c8c3c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c3c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Amigos e atividade social</a>
            
        </li>
    </ul>
    
</li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_AccessibleGaming_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c14c8c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_108" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/accessible-gaming" data-m="{&quot;cN&quot;:&quot;CatNav_Support_AccessibleGaming_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c4c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos acessíveis</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_XboxSystemUpdates_MSXC_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c14c8c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_109" class="js-subm-uhf-nav-link" href="https://support.xbox.com/pt-BR/help/hardware-network/settings-updates/whats-new-xbox-one-system-updates" data-m="{&quot;cN&quot;:&quot;CatNav_Support_XboxSystemUpdates_MSXC_nav&quot;,&quot;id&quot;:&quot;n1c5c14c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c14c8c3m1r1a1&quot;}" style="overflow-x: visible;">Atualizações do sistema Xbox</a>
            
        </li>
                                                    
                                </ul>
                            </div>
                        </li>                                                

                <li id="overflow-menu" class="overflow-menu uhf-menu-item" style="overflow-x: visible;">
                        <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
        <button data-m="{&quot;pid&quot;:&quot;Mais&quot;,&quot;id&quot;:&quot;nn19c8c3m1r1a1&quot;,&quot;sN&quot;:19,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" type="button" aria-label="Mais" aria-expanded="false" style="overflow-x: visible;">Mais</button>
        <ul id="overflow-menu-list" aria-hidden="true" class="overflow-menu-list" style="overflow-x: visible;"><li class="nested-menu uhf-menu-item f-sub-menu js-nav-menu" style="overflow-x: visible;">
                            
                        <button type="button" id="c-shellmenu_110" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_My_Xbox_nonnav&quot;,&quot;id&quot;:&quot;nn15c8c3m1r1a1&quot;,&quot;sN&quot;:15,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Meu Xbox</button><ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;My_Xbox_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c16c8c3m1r1a1&quot;,&quot;sN&quot;:16,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Profile_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c16c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c16c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_111" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/play/user?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Profile_nav&quot;,&quot;id&quot;:&quot;n1c1c16c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c16c8c3m1r1a1&quot;}" style="overflow-x: visible;">Perfil</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Wishlist_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c16c8c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c16c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_112" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-BR/wishlist?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Wishlist_nav&quot;,&quot;id&quot;:&quot;n1c2c16c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c16c8c3m1r1a1&quot;}" style="overflow-x: visible;">Lista de Desejos</a>
            
        </li>
                                                    
                                </ul></li><li class="nested-menu uhf-menu-item f-sub-menu js-nav-menu" style="overflow-x: visible;">
                            
                        <button type="button" id="c-shellmenu_113" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;CatNav_Developers_nonnav&quot;,&quot;id&quot;:&quot;nn17c8c3m1r1a1&quot;,&quot;sN&quot;:17,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">Desenvolvedores</button><ul class="" data-class-idn="" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;Developers_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c18c8c3m1r1a1&quot;,&quot;sN&quot;:18,&quot;aN&quot;:&quot;c8c3m1r1a1&quot;}" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Games_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c18c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c18c8c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="c-shellmenu_114" class="js-subm-uhf-nav-link" href="https://developer.microsoft.com/en-us/games?xr=shellnav" data-m="{&quot;cN&quot;:&quot;CatNav_Games_nav&quot;,&quot;id&quot;:&quot;n1c1c18c8c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c18c8c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos</a>
            
        </li>
                                                    
                                </ul></li>
        </ul>
    </div>

                </li>
                            </ul>
            
        </nav>


            <div class="c-uhfh-actions" data-m="{&quot;cN&quot;:&quot;Header actions_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c3m1r1a1&quot;}" style="overflow-x: visible;">
                <div class="wf-menu" style="overflow-x: visible;">        <nav id="uhf-c-nav" aria-label="Todo menu Microsoft" data-m="{&quot;cN&quot;:&quot;GlobalNav_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <ul class="js-paddle-items" style="overflow-x: visible;">
                <li style="overflow-x: visible;">
                    <div class="c-uhf-menu js-nav-menu" style="overflow-x: visible;">
                        <button type="button" class="c-button-logo all-ms-nav" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_nonnav&quot;,&quot;id&quot;:&quot;nn1c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}" style="overflow-x: visible;"> <span style="overflow-x: visible;">Toda a Microsoft</span></button>
                        <ul class="f-multi-column f-multi-column-6" aria-hidden="true" data-m="{&quot;cN&quot;:&quot;More_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
                                    <li class="c-w0-contr" style="overflow-x: visible;">
            <h2 class="c-uhf-sronly" style="overflow-x: visible;">Global</h2>
            <ul class="c-w0" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;M365_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_0" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-365" data-m="{&quot;cN&quot;:&quot;W0Nav_M365_nav&quot;,&quot;id&quot;:&quot;n1c1c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft 365</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Teams_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="l0_Teams" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-teams/group-chat-software" data-m="{&quot;cN&quot;:&quot;W0Nav_Teams_nav&quot;,&quot;id&quot;:&quot;n1c2c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Teams</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Copilot_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_2" class="js-subm-uhf-nav-link" href="https://copilot.microsoft.com/" data-m="{&quot;cN&quot;:&quot;W0Nav_Copilot_nav&quot;,&quot;id&quot;:&quot;n1c3c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Copilot</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Windows_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_3" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/windows/" data-m="{&quot;cN&quot;:&quot;W0Nav_Windows_nav&quot;,&quot;id&quot;:&quot;n1c4c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Windows</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Xbox_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_4" class="js-subm-uhf-nav-link" href="https://www.xbox.com/" data-m="{&quot;cN&quot;:&quot;W0Nav_Xbox_nav&quot;,&quot;id&quot;:&quot;n1c5c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;Support_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="l1_support" class="js-subm-uhf-nav-link" href="https://support.microsoft.com/pt-br" data-m="{&quot;cN&quot;:&quot;W0Nav_Support_nav&quot;,&quot;id&quot;:&quot;n1c6c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Suporte</a>
            
        </li>
            </ul>
        </li>

<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_7-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;id&quot;:&quot;nn1c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">Software</span>
    <button id="uhf-navbtn-shellmenu_7-button" type="button" f-multi-parent="true" data-m="{&quot;id&quot;:&quot;nn2c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Software</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_7-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_WindowsApps_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_8" class="js-subm-uhf-nav-link" href="https://apps.microsoft.com/home" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_WindowsApps_nav&quot;,&quot;id&quot;:&quot;n1c3c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Aplicações Windows</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_AI_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_9" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/ai" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_AI_nav&quot;,&quot;id&quot;:&quot;n1c4c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">IA</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_OneDrive_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_10" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-365/onedrive/online-cloud-storage" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_OneDrive_nav&quot;,&quot;id&quot;:&quot;n1c5c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">OneDrive</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_Outlook_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_11" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_Outlook_nav&quot;,&quot;id&quot;:&quot;n1c6c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Outlook</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_Skype_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_12" class="js-subm-uhf-nav-link" href="https://support.microsoft.com/pt-br/office/mudar-do-skype-para-o-microsoft-teams-gratuito-3c0caa26-d9db-4179-bcb3-930ae2c87570?icid=DSM_All_Skype" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_Skype_nav&quot;,&quot;id&quot;:&quot;n1c7c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Como migrar do Skype para o Teams</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_OneNote_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_13" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-365/onenote/digital-note-taking-app" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_OneNote_nav&quot;,&quot;id&quot;:&quot;n1c8c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">OneNote</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Software_Microsoft Teams_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_14" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-teams/group-chat-software" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Software_Microsoft Teams_nav&quot;,&quot;id&quot;:&quot;n1c9c7c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c7c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Teams</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cN&quot;:&quot;PCsAndDevices_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_15-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;cN&quot;:&quot;GlobalNav_PCsAndDevices_nonnav&quot;,&quot;id&quot;:&quot;nn1c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">PCs e dispositivos</span>
    <button id="uhf-navbtn-shellmenu_15-button" type="button" f-multi-parent="true" data-m="{&quot;cN&quot;:&quot;GlobalNav_PCsAndDevices_nonnav&quot;,&quot;id&quot;:&quot;nn2c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c8c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">PCs e dispositivos</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_15-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_PCsAndDevices_ShopXbox_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c8c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_16" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br?icid=DSM_All_ShopXbox" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_PCsAndDevices_ShopXbox_nav&quot;,&quot;id&quot;:&quot;n1c3c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c8c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Compre o Xbox</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_PCsAndDevices_Accessories_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c8c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_17" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/accessories" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_PCsAndDevices_Accessories_nav&quot;,&quot;id&quot;:&quot;n1c4c8c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c8c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Acessórios para PC</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_18-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;id&quot;:&quot;nn1c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">Entretenimento</span>
    <button id="uhf-navbtn-shellmenu_18-button" type="button" f-multi-parent="true" data-m="{&quot;id&quot;:&quot;nn2c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c9c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Entretenimento</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_18-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Entertainment_XboxGamePassUltimate_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_19" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/store/xbox-game-pass-ultimate/cfq7ttc0khs0?icid=DSM_All_XboxGamePassUltimate" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Entertainment_XboxGamePassUltimate_nav&quot;,&quot;id&quot;:&quot;n1c3c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox Game Pass Ultimate</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Entertainment_XboxGames_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_20" class="js-subm-uhf-nav-link" href="https://www.xbox.com/pt-br/games/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Entertainment_XboxGames_nav&quot;,&quot;id&quot;:&quot;n1c4c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Xbox e jogos</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Entertainment_PCGames_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_21" class="js-subm-uhf-nav-link" href="https://apps.microsoft.com/games" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Entertainment_PCGames_nav&quot;,&quot;id&quot;:&quot;n1c5c9c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c9c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Jogos para PC</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:10,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_22-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;id&quot;:&quot;nn1c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">Negócios
</span>
    <button id="uhf-navbtn-shellmenu_22-button" type="button" f-multi-parent="true" data-m="{&quot;id&quot;:&quot;nn2c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Negócios
</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_22-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_Microsoft_Cloud_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_23" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-cloud" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_Microsoft_Cloud_nav&quot;,&quot;id&quot;:&quot;n1c3c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Cloud</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_Microsoft Security_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_24" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/security" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_Microsoft Security_nav&quot;,&quot;id&quot;:&quot;n1c4c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Segurança da Microsoft</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_Azure_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_25" class="js-subm-uhf-nav-link" href="https://azure.microsoft.com/pt-br/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_Azure_nav&quot;,&quot;id&quot;:&quot;n1c5c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Azure</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_MicrosoftDynamics365_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_26" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/dynamics-365" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_MicrosoftDynamics365_nav&quot;,&quot;id&quot;:&quot;n1c6c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Dynamics 365</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_Microsoft365forbusiness_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_27" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/microsoft-365/business" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_Microsoft365forbusiness_nav&quot;,&quot;id&quot;:&quot;n1c7c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft 365 para empresas</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_MicrosoftIndustry_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_28" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/industry" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_MicrosoftIndustry_nav&quot;,&quot;id&quot;:&quot;n1c8c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Industry</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_MicrosoftPowerPlatform_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_29" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/power-platform" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_MicrosoftPowerPlatform_nav&quot;,&quot;id&quot;:&quot;n1c9c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Power Platform</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Business_Windows365_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c10c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:10,&quot;aN&quot;:&quot;c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_30" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/windows-365" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Business_Windows365_nav&quot;,&quot;id&quot;:&quot;n1c10c10c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c10c10c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Windows 365</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:11,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_31-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;id&quot;:&quot;nn1c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">Desenvolvedor &amp; it</span>
    <button id="uhf-navbtn-shellmenu_31-button" type="button" f-multi-parent="true" data-m="{&quot;id&quot;:&quot;nn2c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Desenvolvedor &amp; it</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_31-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_MicrosoftDeveloper_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_32" class="js-subm-uhf-nav-link" href="https://developer.microsoft.com/pt-br/?icid=DSM_All_Developper" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_MicrosoftDeveloper_nav&quot;,&quot;id&quot;:&quot;n1c3c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Desenvolvedor Microsoft</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_MicrosoftLearn_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_33" class="js-subm-uhf-nav-link" href="https://learn.microsoft.com/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_MicrosoftLearn_nav&quot;,&quot;id&quot;:&quot;n1c4c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Learn</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_ExploreISVSuccess_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_34" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/isv/isv-success?ocid=cmm3atxvn98" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_ExploreISVSuccess_nav&quot;,&quot;id&quot;:&quot;n1c5c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Suporte para aplicativos de marketplace de IA</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_MicrosoftTechCommunity_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_35" class="js-subm-uhf-nav-link" href="https://techcommunity.microsoft.com/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_MicrosoftTechCommunity_nav&quot;,&quot;id&quot;:&quot;n1c6c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Comunidade Microsoft Tech</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_Marketplace_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_36" class="js-subm-uhf-nav-link" href="https://marketplace.microsoft.com?icid=DSM_All_Marketplace&amp;ocid=cmm3atxvn98" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_Marketplace_nav&quot;,&quot;id&quot;:&quot;n1c7c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Marketplace</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_DeveloperAndIT_VisualStudio_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c8c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_37" class="js-subm-uhf-nav-link" href="https://visualstudio.microsoft.com/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_DeveloperAndIT_VisualStudio_nav&quot;,&quot;id&quot;:&quot;n1c8c11c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c8c11c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Visual Studio</a>
            
        </li>
    </ul>
    
</li>
<li class="f-sub-menu js-nav-menu nested-menu" data-m="{&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:12,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">

    <span id="uhf-navspn-shellmenu_38-span" style="display: block; overflow-x: visible;" f-multi-parent="true" aria-expanded="false" data-m="{&quot;id&quot;:&quot;nn1c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" role="heading" aria-level="2">Outros</span>
    <button id="uhf-navbtn-shellmenu_38-button" type="button" f-multi-parent="true" data-m="{&quot;id&quot;:&quot;nn2c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" tabindex="-1" style="display: none; overflow-x: visible;">Outros</button>
    <ul aria-hidden="false" aria-labelledby="uhf-navspn-shellmenu_38-span" style="overflow-x: visible;">
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Other_Microsoft Rewards_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_39" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/rewards" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Other_Microsoft Rewards_nav&quot;,&quot;id&quot;:&quot;n1c3c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Microsoft Rewards </a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Other_FreeDownloadsAndSecurity_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_40" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/download" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Other_FreeDownloadsAndSecurity_nav&quot;,&quot;id&quot;:&quot;n1c4c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Segurança e downloads gratuitos</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Other_Education_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c5c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_41" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/education?icid=CNavMSCOML0_Studentsandeducation" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Other_Education_nav&quot;,&quot;id&quot;:&quot;n1c5c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c5c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Educação</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Other_GiftCards_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="shellmenu_42" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/pt-br/p/cartao-presente-do-xbox-codigo-digital/cfq7ttc0k63g?icid=DSM_All_GiftCards" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Other_GiftCards_nav&quot;,&quot;id&quot;:&quot;n1c6c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c6c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Cartões-presente</a>
            
        </li>
        <li class="js-nav-menu single-link" data-m="{&quot;cN&quot;:&quot;More_Other_Licensing_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c7c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">
            <a id="Licensing" class="js-subm-uhf-nav-link" href="https://www.microsoft.com/licensing/" data-m="{&quot;cN&quot;:&quot;GlobalNav_More_Other_Licensing_nav&quot;,&quot;id&quot;:&quot;n1c7c12c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c7c12c2c1c9c3m1r1a1&quot;}" style="overflow-x: visible;">Licenciamento</a>
            
        </li>
    </ul>
    
</li>
                                                            <li class="f-multi-column-info" style="overflow-x: visible;">
                                    <a data-m="{&quot;id&quot;:&quot;n13c2c1c9c3m1r1a1&quot;,&quot;sN&quot;:13,&quot;aN&quot;:&quot;c2c1c9c3m1r1a1&quot;}" href="https://www.microsoft.com/pt-br/sitemap" aria-label="" class="c-glyph" style="overflow-x: visible;">Ver mapa do site</a>
                                </li>
                            
                        </ul>
                    </div>
                </li>
            </ul>
        </nav>
</div>
                            <form class="c-search" autocomplete="off" id="searchForm" name="searchForm" role="search" action="https://www.xbox.com/pt-br/Search/Results" method="GET" data-seautosuggest="{&quot;isAutosuggestDisabled&quot;:false,&quot;queryParams&quot;:{&quot;market&quot;:&quot;pt-br&quot;,&quot;clientId&quot;:&quot;7F27B536-CF6B-4C65-8638-A0F8CBDFCA65&quot;,&quot;sources&quot;:&quot;Iris-Products,xSearch-Products,Microsoft-Terms&quot;,&quot;filter&quot;:&quot;+ClientType:StoreWeb&quot;,&quot;counts&quot;:&quot;1,5,5&quot;},&quot;familyNames&quot;:{&quot;Apps&quot;:&quot;Aplicativo&quot;,&quot;Books&quot;:&quot;Livro&quot;,&quot;Bundles&quot;:&quot;Pacote&quot;,&quot;Devices&quot;:&quot;Dispositivo&quot;,&quot;Fees&quot;:&quot;Fee&quot;,&quot;Games&quot;:&quot;Jogo&quot;,&quot;MusicAlbums&quot;:&quot;Álbum&quot;,&quot;MusicTracks&quot;:&quot;Música&quot;,&quot;MusicVideos&quot;:&quot;Vídeo&quot;,&quot;MusicArtists&quot;:&quot;Artista&quot;,&quot;OperatingSystem&quot;:&quot;Sistema Operacional&quot;,&quot;Software&quot;:&quot;Software&quot;,&quot;Movies&quot;:&quot;Filme&quot;,&quot;TV&quot;:&quot;TV&quot;,&quot;CSV&quot;:&quot;Cartão-presente&quot;,&quot;VideoActor&quot;:&quot;Ator&quot;}}" data-seautosuggestapi="https://www.microsoft.com/msstoreapiprod/api/autosuggest" data-m="{&quot;cN&quot;:&quot;GlobalNav_Search_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}" aria-expanded="false" style="overflow-x: visible;"><div class="x-screen-reader" aria-live="assertive"></div>
                                <input id="cli_shellHeaderSearchInput" aria-label="Pesquisa Expandida" aria-expanded="false" aria-controls="universal-header-search-auto-suggest-transparent" aria-owns="universal-header-search-auto-suggest-ul" type="search" name="q" placeholder="Pesquisar em xbox.com" data-m="{&quot;cN&quot;:&quot;SearchBox_nav&quot;,&quot;id&quot;:&quot;n1c3c1c9c3m1r1a1&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c1c9c3m1r1a1&quot;}" data-toggle="tooltip" data-placement="right" title="Pesquisar em xbox.com" role="combobox" aria-autocomplete="list" style="overflow-x: visible;">
                                    <button id="search" aria-label="Pesquisar em xbox.com" class="c-glyph" data-m="{&quot;cN&quot;:&quot;Search_nav&quot;,&quot;id&quot;:&quot;n2c3c1c9c3m1r1a1&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c3c1c9c3m1r1a1&quot;}" data-bi-mto="true" aria-expanded="false" style="overflow-x: visible;">
                                        <span role="presentation" style="overflow-x: visible;">Pesquisar</span>
                                        <span role="tooltip" class="c-uhf-tooltip c-uhf-search-tooltip" style="overflow-x: visible;">Pesquisar em xbox.com</span>
                                    </button>
                                <div class="m-auto-suggest" id="universal-header-search-auto-suggest-transparent" role="group" style="overflow-x: visible;">
                                    <ul class="c-menu" id="universal-header-search-auto-suggest-ul" aria-label="Sugestões de Pesquisa" aria-hidden="true" data-bi-dnt="true" data-bi-mto="true" data-js-auto-suggest-position="default" role="listbox" data-tel="jsll" data-m="{&quot;cN&quot;:&quot;search suggestions_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c3c1c9c3m1r1a1&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c3c1c9c3m1r1a1&quot;}" style="overflow-x: visible;"></ul>
                                    <ul class="c-menu f-auto-suggest-no-results" aria-hidden="true" data-js-auto-suggest-postion="default" data-js-auto-suggest-position="default" role="listbox" style="overflow-x: visible;">
                                        <li class="c-menu-item" style="overflow-x: visible;"> <span tabindex="-1" style="overflow-x: visible;">Nenhum resultado</span></li>
                                    </ul>
                                </div>
                                
                            </form>
                        <button data-m="{&quot;cN&quot;:&quot;cancel-search&quot;,&quot;pid&quot;:&quot;Cancelar Pesquisar&quot;,&quot;id&quot;:&quot;nn4c1c9c3m1r1a1&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}" id="cancel-search" class="cancel-search" aria-label="Cancelar Pesquisar" style="overflow-x: visible;">
                            <span style="overflow-x: visible;">Cancelar</span>
                        </button>
                    <a id="uhf-shopping-cart" style="margin-top: 2px; overflow-x: visible;" aria-label="0 itens no carrinho de compras" class="c-action-trigger c-glyph c-uhf-nav-link glyph-shopping-cart" href="https://www.xbox.com/pt-BR/cart" data-src-dmn-chk="true" data-m="{&quot;cN&quot;:&quot;GlobalNav_Cart_nav&quot;,&quot;bhvr&quot;:82,&quot;id&quot;:&quot;n5c1c9c3m1r1a1&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}">
                        <span class="shopping-cart-amount x-hidden" aria-hidden="true" style="overflow-x: visible;">0</span>
                        <span class="c-cart-lbl c-st-lbl" style="overflow-x: visible;">Carrinho</span>
                        <span id="uhf-shopping-cart-tooltip" class="c-uhf-tooltip" role="tooltip" style="overflow-x: visible;">0 itens no carrinho de compras</span>
                    </a>
                            <iframe id="shell-cart-count" data-src="//www.microsoft.com/store/buy/cartcount" src="//www.microsoft.com/store/buy/cartcount" style="overflow-x: visible;"></iframe>
                        <div id="meControl" class="c-me" data-signinsettings="{&quot;containerId&quot;:&quot;meControl&quot;,&quot;enabled&quot;:true,&quot;headerHeight&quot;:48,&quot;debug&quot;:false,&quot;extensibleLinks&quot;:[{&quot;string&quot;:&quot;Xbox Perfil&quot;,&quot;url&quot;:&quot;https://www.xbox.com/play/user&quot;,&quot;id&quot;:&quot;&quot;},{&quot;string&quot;:&quot;Configurações do Xbox&quot;,&quot;url&quot;:&quot;/user/settings/privacy-and-safety?xr=mebarnav&quot;,&quot;id&quot;:&quot;&quot;},{&quot;string&quot;:&quot;Subscrições&quot;,&quot;url&quot;:&quot;https://account.microsoft.com/services?ref=xboxme&quot;,&quot;id&quot;:&quot;&quot;},{&quot;string&quot;:&quot;Resgatar Código&quot;,&quot;url&quot;:&quot;https://redeem.microsoft.com/enter?ref=xboxcom&quot;,&quot;id&quot;:&quot;&quot;}],&quot;userData&quot;:{&quot;idp&quot;:&quot;msa&quot;,&quot;firstName&quot;:&quot;&quot;,&quot;lastName&quot;:&quot;&quot;,&quot;memberName&quot;:&quot;&quot;,&quot;cid&quot;:&quot;&quot;,&quot;authenticatedState&quot;:&quot;3&quot;},&quot;rpData&quot;:{&quot;preferredIdp&quot;:&quot;msa&quot;,&quot;msaInfo&quot;:{&quot;signInUrl&quot;:&quot;https://account.xbox.com/Account/Signin&quot;,&quot;signOutUrl&quot;:&quot;&quot;,&quot;meUrl&quot;:&quot;https://login.live.com/me.srf?wa=wsignin1.0&quot;},&quot;aadInfo&quot;:{&quot;signOutUrl&quot;:&quot;&quot;,&quot;appId&quot;:&quot;&quot;,&quot;siteUrl&quot;:&quot;&quot;,&quot;blockMsaFed&quot;:true}}}" data-m="{&quot;cN&quot;:&quot;GlobalNav_Account_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c6c1c9c3m1r1a1&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c1c9c3m1r1a1&quot;}" style="overflow-x: visible;"><div class="mectrl_root mectrl_theme_light_header"><a id="mectrl_main_trigger" class="mectrl_resetStyle mectrl_trigger" aria-label="Entre em sua conta" href="https://www.xbox.com/pt-BR/auth/msa?action=logIn&amp;returnUrl=https%3A%2F%2Fwww.xbox.com%2Fpt-BR%2Fxbox-game-pass%2Fgames&amp;ru=https%3A%2F%2Fwww.xbox.com%2Fpt-BR%2Fxbox-game-pass%2Fgames" target="_top"><span class="mectrl_screen_reader_text">Entre em sua conta</span><div class="mectrl_topHeader" aria-hidden="true" role="presentation"><div id="mectrl_headerPicture" class="mectrl_profilepic mectrl_glyph mectrl_signIn_circle_glyph" aria-hidden="true" role="presentation"></div></div></a></div></div>
                
            </div>
        </div>
        
        
    </div>
    
</header>




    </div>
        </div>

    </div>
</div><div id="uhf-script-tags"><script src="https://wcpstatic.microsoft.com/mscc/lib/v2/wcp-consent.js"></script><script src="https://www.microsoft.com/onerfstatics/marketingsites-wcus-prod/shell/_scrf/js/themes=default/54-af9f9f/fb-2be034/21-f9d187/b0-50721e/d8-97d509/40-0bd7f9/ea-f1669e/9d-c6ea39/62-a72447/3e-a4ee50/7c-0bd6a1/17-6dfe30/db-bc0148/dc-7e9864/6d-c07ea1/6f-dafe8c/f6-aa5278/e6-5f3533/6d-1e7ed0/b7-cadaa7/62-2741f0/ca-40b7b0/4e-ee3a55/3e-f5c39b/c3-6454d7/f9-7592d3/d0-e64f3e/92-10345d/79-499886/7e-cda2d3/e7-1fe854/57-c14418/38-b93a9e/de-884374/1f-100dea/33-abe4df/2b-8e0ae6?ver=2.0&amp;_cf=02242021_3231&amp;iife=1"></script><script src="https://mem.gfx.ms/meversion?partner=XboxComUHF&amp;market=pt-br&amp;uhf=1" defer=""></script></div><div role="main" class="Shell-module__shellContainer___YmZHe" id="PageContent" tabindex="-1"><iframe name="cartMuid-sync-iframe" referrerpolicy="strict-origin" sandbox="allow-scripts allow-same-origin" src="https://www.microsoft.com/store/XboxComMsComCartMuidSync.html" width="0" height="0" class="CartMuidSync-module__muidSyncFrame___NpX0w"></iframe><link rel="stylesheet" href="https://www.xbox.com/bundles/UhfMwfOverrides" type="text/css"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" href="/en-us/xbox-game-pass/games/css/xgpcat-2025.css" type="text/css"><style class="darkreader darkreader--sync" media="screen"></style><link rel="stylesheet" href="/en-US/global-shares/templates/CSS/page-bar-dropdown.css" type="text/css"><style class="darkreader darkreader--sync" media="screen"></style><div class="mwf-v1-xbox"><div id="bodycolumn" class="catalog"><div tabindex="-1"><div id="moduleBased-shared-head-content" role="none">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="/en-US/global-shares/templates/CSS/xbox-MWF-2021.css"><style class="darkreader darkreader--cors" media="screen">html, body, div, span, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
abbr, address, cite, code,
del, dfn, em, img, ins, kbd, q, samp,
small, strong, sub, sup, var,
b, i,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, figcaption, figure,
footer, header, hgroup, menu, nav, section, summary,
time, mark, audio, video {
    margin:0;
    padding:0;
    border:0;
    outline:0;
    font-size:100%;
   
}



article,aside,details,figcaption,figure,
footer,header,hgroup,menu,nav,section {
    display:block;
}


.custom-sb-hero.green .content-div,
.custom-sb-hero.green [data-grid~="col-12"] {
    background-color: #107c10;
}

.custom-sb-hero.dark-gray .content-div,
.custom-sb-hero.dark-gray [data-grid~="col-12"] {
    background-color: #171717;
}

.custom-sb-hero.gray .content-div,
.custom-sb-hero.gray [data-grid~="col-12"] {
    background-color: #505050;
}

.custom-sb-hero.light-gray .content-div,
.custom-sb-hero.light-gray [data-grid~="col-12"] {
    background-color: #e6e6e6;
}
@media screen and (min-width: 1921px) {
.custom-sb-hero.short.green .content-div,
.custom-sb-hero.short.green [data-grid~="col-12"],
.custom-sb-hero.short.dark-gray .content-div,
.custom-sb-hero.short.dark-gray [data-grid~="col-12"],
.custom-sb-hero.short.gray .content-div,
.custom-sb-hero.short.gray [data-grid~="col-12"],
.custom-sb-hero.short.light-gray .content-div,
.custom-sb-hero.short.light-gray [data-grid~="col-12"] {
    height: 720px;
}
}
.custom-sb-hero .c-badge {
    width: 200px;
    margin: 0 auto;
}


@media screen and (min-width: 768px) {
    .custom-sb-hero .copy-left [data-grid~='col-9'] {
        float: right;
    }

    .custom-sb-hero .copy-left [data-grid~='col-3'] {
        float: left;
    }

    .custom-sb-hero .content-div>div {
        display: grid;
        width: 46vw;
    }

    .custom-sb-hero .copy-right .content-div {
        right: 0px;
    }

    .custom-sb-hero .copy-left .content-div {
        left: 0px;
    }

    .custom-sb-hero .copy-right .content-div>div {
        right: 22.85vw;
    }

    .custom-sb-hero .copy-left .content-div>div {
        left: 1.6vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 1.6vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 22.9vw;
    }

    .custom-sb-hero [data-grid~='col-9'] img {
        width: 100%;
    }

    .custom-sb-hero .content-div>div {
        position: relative;
        text-align: center;
        top: 120px;
        top: calc(55%);
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
    }

    .custom-sb-hero [data-grid~="container"] .content-div>div {
        top: 120px;
        top: calc(46%);
    }
}

@media screen and (min-width: 1084px) {
    .custom-sb-hero [data-grid~="container"] .content-div>div {
        display: grid;
        width: 35vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 4.65vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 17.4vw;
    }
}

@media screen and (min-width: 1400px) {
    .custom-sb-hero [data-grid~="container"] .content-div>div {
        display: grid;
        width: 35vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 4.9vw;
    }
}

@media screen and (min-width: 1800px) {
    .custom-sb-hero [data-grid~="container"] .content-div>div {
        display: grid;
        width: auto;
    }

    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 10.5vw;
    }

    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 10.4vw;
    }
}
@media screen and (min-width: 1921px) {
    .custom-sb-hero .copy-left .content-div>div {
        left: 1.4vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 9.5vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 9.4vw;
    }
}
@media screen and (min-width: 2021px) {
    .custom-sb-hero .copy-left .content-div>div {
        left: .5vw;
    }

}
@media screen and (min-width: 2165px) {
    .custom-sb-hero .copy-left .content-div>div {
        left: -1vw;
    }
}
@media screen and (min-width: 2325px) {
    .custom-sb-hero .copy-left .content-div>div {
        left: -2.5vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 8.5vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 8.4vw;
    }
}
@media screen and (min-width: 2500px) {
    .custom-sb-hero .copy-left .content-div>div {
        left: -4vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-left .content-div>div {
        left: 7.7vw;
    }
    .custom-sb-hero [data-grid~="container"] .copy-right .content-div>div {
        right: 7.6vw;
    }
}
@media screen and (min-width: 768px) and (max-width: 1399px) {
   .jumpgcontainer .jump-g.jump-b {
        position: relative;
        top: -6px !important;
    }
   .jumpgcontainer .c-heading-1a + .jump-g.jump-b {
     top: 4px !important;
   }
}

@media screen and (min-width: 0px) {
   .jumpgcontainer .jump-g.jump-b {
        position: relative;
        top: -6px;
    }

    .custom-sb-hero .lower-content,
    .cross-sell .lower-content {
        position: relative;
        top: -22px;
    }

    .custom-sb-hero {
        vertical-align: bottom;
    }

}

@media screen and (min-width: 768px) {
    .custom-sb-hero.tall .content-div {
        height: 53.5vw;
    }

    .custom-sb-hero.short .content-div {
        height: 42.5vw;
    }

    .custom-sb-hero .c-group {
        flex-direction: column;
        align-items: center;
    }

    .custom-sb-hero .c-group .c-call-to-action {
        max-width: 256px;
    }

    .jump-g.jump-b {
        position: relative;
        top: -8px;
    }

    .custom-sb-hero .lower-content,
    .cross-sell.subhead .lower-content {
        position: relative;
        top: 5px;
    }
}


@media screen and (min-width: 1084px) {
    .custom-sb-hero.tall .content-div {
        height: 54vw;
    }

    .custom-sb-hero.short .content-div {
        height: 36.9vw;
    }

    .custom-sb-hero.short [data-grid~='container'] .content-div {
        height: 33.2vw;
    }

    .jump-g.jump-b {
        position: relative;
        top: -8px;
    }

    .custom-sb-hero .lower-content {
        position: relative;
        top: 15px;
    }

    .cross-sell.subhead .lower-content {
        position: relative;
        top: -60px;
    }
}

@media screen and (min-width: 1400px) {
    .custom-sb-hero.tall .content-div {
        height: 55.5vw;
    }

    .custom-sb-hero.short .content-div {
        height: 37.05vw;
    }

    .custom-sb-hero.short [data-grid~='container'] .content-div {
        height: 31vw;
    }

    .jump-g.jump-b {
        position: relative;
        top: -19px;
    }
.SB-hero-banner .jump-g.jump-b {
        position: relative;
        top: -42px;
    }
    .custom-sb-hero .lower-content,
    .cross-sell .lower-content {
        position: relative;
        top: -60px;
    }

}


@media screen and (min-width: 1921px) {
    .custom-sb-hero {
        width: 1920px;
        margin: 0 auto;
    }

    .custom-sb-hero.tall section img,
    .custom-sb-hero.tall .content-div {
        height: 1080px;
    }

    .custom-sb-hero.short section img,
    .custom-sb-hero.short .content-div {
        height: 720px;
    }
.custom-sb-hero.short [data-grid~='container'] .content-div {
    height: 720px;
}
    .custom-sb-hero .copy-right .content-div {
        right: auto;
       
    }

    .custom-sb-hero .copy-left .content-div {
        left: auto;
    }
}

@media screen and (max-width: 1920px) {
    .custom-sb-hero section {
        width: 100%;
    }
}

@media screen and (max-width: 767px) {
    .custom-sb-hero picture img {
        width: 100%;
    }

    .custom-sb-hero .content-div {
        text-align: center;
        padding: 24px 0;
    }

    .custom-sb-hero .content-div .c-group {
        display: block;
    }

    .cross-sell .m-hero-item>div>div {
        top: calc(40%) !important;
    }
}



.custom-sb-hero .c-subheading {
    font-size: 24px;
    line-height: 28px;
    padding: 4px 0 8px;
    font-weight: 600;
    overflow: hidden;
    box-sizing: content-box;
    max-height: 56px;
    padding-bottom: 12px;
}

@media only screen and (max-width:1779px) {
    .custom-sb-hero.short .c-heading-1L {
        font-size: 86px;
        line-height: 82px;
    }
}

@media only screen and (max-width:1399px) {
    .custom-sb-hero .c-subheading {
        font-size: 15px;
        line-height: 20px;
        padding: 8px 0 0;
        font-weight: 600;
        max-height: 40px;
    }

    .custom-sb-hero.short .c-heading-1L {
        font-size: 62px;
        line-height: 60px;
    }
}

@media only screen and (max-width:767px) {
    .custom-sb-hero .c-subheading {
        font-size: 18px;
        line-height: 24px;
        padding: 9px 0 3px;
        font-weight: 600;
        overflow: hidden;
        box-sizing: content-box;
        max-height: 48px;
    }

    .custom-sb-hero .c-heading-3,
    .custom-sb-hero .c-subheading-1 {
        font-size: 26px;
        line-height: 32px;
    }

}

.custom-sb-hero .c-group,
.cross-sell.subhead .c-group {
    margin-top: 12px;
    padding: 12px 2px 0;
}






 .banner-background .m-banner .c-call-to-action {color: #054B16;}
 .banner-background .m-banner .c-call-to-action:hover {color: #000;}
.SB-hero-banner {
    padding-top: 96px;
}

.SB-hero-banner .m-banner {
    position: relative;
    z-index: 2;
}

.SB-hero-banner .banner-background {
    width: 100%;
    background-color: #e6e6e6;
    padding-bottom: 130px;
}


.SB-hero-banner .m-banner .c-image {
    margin: 0 auto 35px;
    width: auto;
    max-height: 77px;
}

@media screen and (min-width: 0) {
    .SB-hero-banner .banner-background {
        position: relative;
        padding-top: 74px;
        top: -120px;
        margin-bottom: -120px;
    }

    .SB-hero-banner.nojump .banner-background {
        position: relative;
        padding-top: 41px;
        top: -38px;
        margin-bottom: -37px;
    }

    .SB-hero-banner.head1a .banner-background {
        padding-top: 55px;
        top: -59px;
        margin-bottom: -59px;
    }

    .SB-hero-banner.head1a.nojump .banner-background {
        padding-top: 30px;
        top: -27px;
        margin-bottom: -27px;
    }
}

@media screen and (min-width: 768px) {
    .SB-hero-banner .banner-background {
        padding-top: 72px;
        top: -108px;
        margin-bottom: -108px;
    }

    .SB-hero-banner.head1a .banner-background {
        padding-top: 61px;
        top: -70px;
        margin-bottom: -70px;
    }

    .SB-hero-banner.head1a.nojump .banner-background {
        padding-top: 30px;
        top: -34px;
        margin-bottom: -34px;
    }
}

@media screen and (min-width: 1084px) {
    .SB-hero-banner .banner-background {
        padding-top: 83px;
        top: -131px;
        margin-bottom: -131px;
    }

    .SB-hero-banner.nojump .banner-background {
        padding-top: 45px;
        top: -44px;
        margin-bottom: -43px;
    }

    .SB-hero-banner.head1a .banner-background {
        padding-top: 60px;
        top: -70px;
        margin-bottom: -70px;
    }

    .SB-hero-banner.head1a.nojump .banner-background {
        padding-top: 30px;
        top: -34px;
        margin-bottom: -34px;
    }
}

@media screen and (min-width: 1400px) {
    .SB-hero-banner .banner-background {
        padding-top: 116px;
        top: -199px;
        margin-bottom: -199px;
    }

    .SB-hero-banner.nojump .banner-background {
        padding-top: 60px;
        top: -60px;
        margin-bottom: -62px;
    }

    .SB-hero-banner.head1a .banner-background {
        padding-top: 83px;
        top: -97px;
        margin-bottom: -97px;
    }

    .SB-hero-banner.head1a.nojump .banner-background {
        padding-top: 48px;
        top: -44px;
        margin-bottom: -44px;
    }

}





@media screen and (min-width: 1084px) {
.tall5up-container h2.c-heading-1a:before {
    content: '';
    height: 50%;
    position: absolute;
    width: 100%;
    top: 0;
    background-color: #333;
    z-index: -1;}
}

.tall5up a:not(.x-hidden-focus).c-call-to-action:focus {
    outline: 2px dashed #fff;
    border: 2px dashed #000;
}
.tall5up .m-content-placement div div {
    padding-left: 0px;
    padding-right: 0px;
}

.tall5up .m-content-placement div div picture {
    height: 55.7291vw;
}

.tall5up .m-content-placement div div div.x-type-center {
    transform: translateY(-125%)
}

.tall5up .m-content-placement div div div.x-type-center img {
    height: 50px;
    margin: 0 auto;
}

.tall5up .m-content-placement div div div section.m-content-placement-item {
    margin-top: 0px;
}

.tall5up-container .banner-background {
    padding-top: 0px !important;
    z-index: 1;
}

.tall5up-container .m-banner {
    max-width: 600px !important;
}

.tall5up-background {
    height: 81vw;
    background-color: #333;
    transform: translateY(-87vw);
    z-index: -1;
    position: absolute;
    left: 4.9vw;
    width: 89vw;
}

@media screen and (min-width: 1795px) {

    .tall5up-background {
        --widthA: 1795px;
        --widthB: calc(100vw - var(--widthA));
        --widthC: calc(var(--widthB)/2.2);
        --widthD: calc(var(--widthC) + 4.9vw);
        left: var(--widthD);
        width: 1600px;
    }
}

@media screen and (max-width: 1083px) {
    .tall5up-container .banner-background .tall5up .m-content-placement {
        padding: 0 0 0 0;
    }

    .tall5up-background {
        width: 100%;
        left: 0;
    }
}

.tall5up-container .m-content-placement-item:hover picture img {
    opacity: 1 !important;
}

@media screen and (min-width: 1700px) {
    .tall5up-background {
        height: 82vw;
        transform: translateY(-87.5vw);
    }
}

@media screen and (min-width: 1600px) and (max-width: 1699px) {
    .tall5up-background {
        height: 84vw;
        transform: translateY(-91.5vw);
    }
}

@media screen and (min-width: 1500px) and (max-width: 1599px) {
    .tall5up-background {
        height: 86vw;
        transform: translateY(-93.5vw);
    }
}

@media screen and (min-width: 1400px) and (max-width: 1499px) {
    .tall5up-background {
        height: 88vw;
        transform: translateY(-96vw);
    }
}

@media screen and (min-width: 1300px) and (max-width: 1399px) {
    .tall5up-background {
        height: 77vw;
        transform: translateY(-85vw);
    }
}

@media screen and (min-width: 1200px) and (max-width: 1299px) {
    .tall5up-background {
        height: 78vw;
        transform: translateY(-88vw);
    }
}

@media screen and (min-width: 1084px) and (max-width: 1199px) {
    .tall5up-background {
        height: 80vw;
        transform: translateY(-91vw);
    }
}

@media screen and (min-width: 1000px) and (max-width: 1083px) {
    .tall5up-background {
        height: 152vw;
        transform: translateY(-157vw);
    }
}

@media screen and (min-width: 950px) and (max-width: 999px) {
    .tall5up-background {
        height: 155vw;
        transform: translateY(-160vw);
    }
}

@media screen and (min-width: 900px) and (max-width: 949px) {
    .tall5up-background {
        height: 152vw;
        transform: translateY(-154vw);
    }
}

@media screen and (min-width: 850px) and (max-width: 899px) {
    .tall5up-background {
        height: 155vw;
        transform: translateY(-157vw);
    }
}

@media screen and (min-width: 800px) and (max-width: 849px) {
    .tall5up-background {
        height: 158vw;
        transform: translateY(-160vw);
    }
}

@media screen and (min-width: 768px) and (max-width: 799px) {
    .tall5up-background {
        height: 160vw;
        transform: translateY(-162vw);
    }
}

@media screen and (min-width: 735px) and (max-width: 767px) {
    .tall5up-background {
        height: 314vw;
        transform: translateY(-319vw);
    }
}

@media screen and (min-width: 680px) and (max-width: 734px) {
    .tall5up-background {
        height: 318vw;
        transform: translateY(-324vw);
    }
}

@media screen and (min-width: 630px) and (max-width: 679px) {
    .tall5up-background {
        height: 322vw;
        transform: translateY(-328vw);
    }
}

@media screen and (min-width: 580px) and (max-width: 629px) {
    .tall5up-background {
        height: 327vw;
        transform: translateY(-333vw);
    }
}

@media screen and (min-width: 520px) and (max-width: 579px) {
    .tall5up-background {
        height: 326vw;
        transform: translateY(-334vw);
    }
}

@media screen and (min-width: 415px) and (max-width: 519px) {
    .tall5up-background {
        height: 329vw;
        transform: translateY(-337vw);
    }
}

@media screen and (min-width: 376px) and (max-width: 414px) {
.tall5up-background {
    height: 350vw;
    transform: translateY(-365vw);}

.SB-hero-banner.head1a.tall5up-container {
    padding-top: 30px !important}
}

@media screen and (min-width: 321px) and (max-width: 375px) {
.tall5up-background {
    height: 375vw;
    transform: translateY(-395vw);}

.SB-hero-banner.head1a.tall5up-container {
    padding-top: 48px !important}
}

@media screen and (min-width: 0px) and (max-width: 320px) {
    .tall5up-background {
        height: 384vw;
        transform: translateY(-396vw);
    }

    .SB-hero-banner.head1a.tall5up-container {
        padding-top: 48px !important
    }
}

@media screen and (min-width: 415px) and (max-width: 539px) {
    .SB-hero-banner.head1a.tall5up-container {
        padding-top: 48px !important
    }
}

@media screen and (min-width: 0px) and (max-width: 1083px) {

    
    .tall5up .m-content-placement div div picture {
        height: 100%;
        padding-bottom: 0;
    }

    .tall5up .m-content-placement div div div section.m-content-placement-item {
        height: 22.6vw;
    }

    .tall5up .m-content-placement .tall5up-item {
        width: 100%
    }

    .tall5up-container {
        padding-bottom: 70px;
    }

    .SFE-copy.x-type-center {
        bottom: 0px;
    }
}

@media screen and (min-width: 768px) and (max-width: 1083px) {
    .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-15.5vw)
    }
}

@media screen and (max-width: 767px) {
    .tall5up .m-content-placement div div div section.m-content-placement-item {
        height: 54vw;
    }

    .tall5up-container .SB-hero-banner .banner-background {
        padding-bottom: 0px !important;
    }

    .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-32.8vw)
    }

}

@media screen and (min-width: 415px) and (max-width: 499px) {
    .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-35.8vw)
    }
}

@media screen and (max-width: 414px) {
    .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-37.5vw)
    }
}

@media screen and (max-width: 320px) {
    .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-39.5vw)
    }
}

.SFE-copy {
    max-width: 800px;
    margin: 0px auto 0px auto;
    position: relative;
    bottom: 160px;
}

.SFE-copy p {
    max-width: 800px;
    margin: 0px auto 0px auto;
}

@media screen and (max-width: 539px) {
    .tall5up-container.SB-hero-banner .banner-background {
        padding-bottom: 0px !important;
    }
}

@media screen and (min-width: 1921px) {
    .tall5up-container.SB-hero-banner .banner-background {
        width: 1920px;
        margin-left: auto;
        margin-right: auto;
    }

    .tall5up-background {
        height: 1574px;
        transform: translateY(-1680px);
    }

}




.four-panel-selector .m-content-placement-item:hover picture img {
    opacity: 1 !important;
}

@media screen and (max-width: 499px) {
    .four-panel-selector .tall5up .m-content-placement div div div.x-type-center {
        transform: translateY(-32.5vw)
    }
}

.four-panel-selector .m-banner {
    z-index: 2;
    position: relative;
}

@media screen and (min-width: 1084px) {
    .four-panel-selector .m-banner {
        max-width: 1000px !important;
    }
}

@media screen and (max-width: 1083px) {
    .four-panel-selector .tall5up .m-content-placement {
        margin-bottom: -6vw
    }
}

.four-panel-selector .banner-background .tall5up .m-content-placement-item picture img {
    z-index: 0;
}

@media screen and (min-width: 768px) {
    .four-panel-selector .tall5up .m-content-placement>div>div {
        width: 25% !important;
        float: left;
    }
}

@media screen and (min-width: 0px) and (max-width: 1083px) {

    
    .four-panel-selector .tall5up .m-content-placement div div div section.m-content-placement-item {
        height: 68.6vw;
    }
}

@media screen and (min-width: 0px) and (max-width: 414px) {

    
    .four-panel-selector .tall5up .m-content-placement div div div section.m-content-placement-item {
        height: 50vw;
    }
}

@media screen and (min-width: 415px) and (max-width: 767px) {

    
    .four-panel-selector .tall5up .m-content-placement div div div section.m-content-placement-item {
        height: 47vw;
    }
}

@media screen and (min-width: 768px) and (max-width: 1083px) {

    .four-panel-selector .m-banner {
        max-width: 600px !important;
    }

}

@media screen and (min-width: 1921px) {
    .tall5up .m-content-placement div div picture {
        max-height: 1070px;
    }

    .four-panel-selector {
        max-height: 1740px;
        background-color: #171717;
        max-width: 1920px;
        margin-left: auto;
        margin-right: auto;
    }

}

.four-panel-selector h2,
.four-panel-selector .c-group {
    padding-bottom: 36px;
}

@media screen and (min-width: 1400px) and (max-width: 1920px) {
    .four-panel-selector {
        background-position: bottom !important;
        background-color: #e6e6e6 !important;
    }
}

@media screen and (min-width: 1400px) and (max-width: 1430px) {
    .four-panel-selector .tall5up {
        margin-top: -5px;
    }
}

@media screen and (min-width: 1400px) {
    .four-panel-selector h2 {
        padding-top: 0px;
    }

    .four-panel-selector .tall5up {
        padding-left: 8%;
        padding-right: 8%;
    }
}

@media screen and (max-width: 1399px) {
    .four-panel-selector .tall5up {
        padding-top: 15px;
    }
}




.six-panel-selector.tall5up-container .m-banner {
    max-width: 900px !important;
}
@media screen and (min-width: 1084px) and (max-width: 1399px) {
.six-panel-selector.tall5up-container .m-banner {
    max-width: 600px !important;
}
}

@media screen and (min-width: 1084px) {
    .six-panel-selector .tall5up .m-content-placement>div>div {
        width: 16.66%;
        float: left;
    }
.six-panel-selector .SFE-copy{
    bottom:60px;
}
}
@media screen and (min-width: 1400px) and (max-width: 1599px) {
.six-panel-selector .SFE-copy{
    bottom:60px;
}
}
@media screen and (min-width: 1084px) and (max-width: 1399px) {
.six-panel-selector .SFE-copy{
    bottom:40px;
}
}

.tall6up-background {
    height: 81.5vw;
    background-color: #333;
    transform: translateY(-82vw);
    z-index: -1;
    position: absolute;
    left: 4.9vw;
    width: 89vw;
}

@media screen and (min-width: 1795px) {

    .tall6up-background {
        --widthA: 1795px;
        --widthB: calc(100vw - var(--widthA));
        --widthC: calc(var(--widthB)/2.2);
        --widthD: calc(var(--widthC) + 4.9vw);
        left: var(--widthD);
        width: 1600px;
    }
}

@media screen and (max-width: 1083px) {
.tall5up-container .banner-background .tall5up .m-content-placement {
    padding: 0 0 0 0;}

.tall5up-background {
    width: 100%;
    left: 0;}

.tall6up-background {
    width: 100%;
    left: 0;}

.six-panel-selector .SFE-copy {
    max-width: calc(1600px + 10%);
    padding-left: 5%;
    padding-right: 5%;}
}

.tall5up-container .m-content-placement-item:hover picture img {
    opacity: 1 !important;
}

@media screen and (min-width: 1600px) and (max-width: 1699px) {
    .tall6up-background {
        height: 85.5vw;
        transform: translateY(-86vw);
    }
}
@media screen and (min-width: 1500px) and (max-width: 1599px) {
    .tall6up-background {
        height: 87vw;
        transform: translateY(-88vw);
    }
}

@media screen and (min-width: 1400px) and (max-width: 1499px) {
    .tall6up-background {
        height: 89vw;
        transform: translateY(-90vw);
    }
}

@media screen and (min-width: 1300px) and (max-width: 1399px) {
    .tall6up-background {
        height: 85.5vw;
        transform: translateY(-85vw);
    }
}

@media screen and (min-width: 1200px) and (max-width: 1299px) {
    .tall6up-background {
        height: 88.5vw;
        transform: translateY(-88vw);
    }
}

@media screen and (min-width: 1084px) and (max-width: 1199px) {
    .tall6up-background {
        height: 92vw;
        transform: translateY(-91vw);
    }
}

@media screen and (min-width: 1000px) and (max-width: 1083px) {
    .tall6up-background {
        height: 178vw;
        transform: translateY(-180vw);
    }
}

@media screen and (min-width: 950px) and (max-width: 999px) {
    .tall6up-background {
        height: 180vw;
        transform: translateY(-182vw);
    }
}

@media screen and (min-width: 900px) and (max-width: 949px) {
    .tall6up-background {
        height: 182vw;
        transform: translateY(-184vw);
    }
}

@media screen and (min-width: 850px) and (max-width: 899px) {
    .tall6up-background {
        height: 184vw;
        transform: translateY(-186vw);
    }
}

@media screen and (min-width: 800px) and (max-width: 849px) {
    .tall6up-background {
        height: 185.5vw;
        transform: translateY(-188vw);
    }
}

@media screen and (min-width: 768px) and (max-width: 799px) {
    .tall6up-background {
        height: 187.5vw;
        transform: translateY(-190vw);
    }
}

@media screen and (min-width: 735px) and (max-width: 767px) {
    .tall6up-background {
        height: 374vw;
        transform: translateY(-376vw);
    }
}

@media screen and (min-width: 680px) and (max-width: 734px) {
    .tall6up-background {
        height: 377vw;
        transform: translateY(-380vw);
    }
}

@media screen and (min-width: 630px) and (max-width: 679px) {
    .tall6up-background {
        height: 381vw;
        transform: translateY(-384vw);
    }
}

@media screen and (min-width: 580px) and (max-width: 629px) {
    .tall6up-background {
        height: 389vw;
        transform: translateY(-392vw);
    }
}
@media screen and (min-width: 540px) and (max-width: 579px) {
    .tall6up-background {
        height: 396vw;
        transform: translateY(-399vw);
    }
}

@media screen and (min-width: 520px) and (max-width: 539px) {
    .tall6up-background {
        height: 391vw;
        transform: translateY(-394vw);
    }
}
@media screen and (min-width: 490px) and (max-width: 519px) {
    .tall6up-background {
        height: 393vw;
        transform: translateY(-398vw);
    }
}
@media screen and (min-width: 470px) and (max-width: 489px) {
    .tall6up-background {
        height: 398vw;
        transform: translateY(-403vw);
    }
}
@media screen and (min-width: 430px) and (max-width: 469px) {
    .tall6up-background {
        height: 406vw;
        transform: translateY(-409vw);
    }
}

@media screen and (min-width: 415px) and (max-width: 429px) {
    .tall6up-background {
        height: 418vw;
        transform: translateY(-421vw);
    }
}

@media screen and (min-width: 376px) and (max-width: 414px) {
.tall6up-background {
    height: 430vw;
    transform: translateY(-445vw);}

.SB-hero-banner.head1a.tall5up-container {
    padding-top: 30px !important}
}

@media screen and (min-width: 341px) and (max-width: 375px) {
.tall6up-background {
    height: 445vw;
    transform: translateY(-459vw);}
}

@media screen and (min-width: 321px) and (max-width: 340px) {
    .tall6up-background {
        height: 445vw;
        transform: translateY(-443vw);
    }

    .SB-hero-banner.head1a.tall5up-container {
        padding-top: 48px !important
    }
}
@media screen and (min-width: 360px) and (max-width: 375px) {
        .six-panel-selector.tall5up-container .m-banner .c-heading-1a{
        font-size: 42px;
        line-height: 44px;
    }

}
@media screen and (min-width: 0px) and (max-width: 359px) {
        .six-panel-selector.tall5up-container .m-banner .c-heading-1a{
        font-size: 36px;
        line-height: 38px;
    }
}

@media screen and (min-width: 0px) and (max-width: 320px) {
    .tall6up-background {
        height: 447vw;
        transform: translateY(-450vw);
    }

    .SB-hero-banner.head1a.tall5up-container {
        padding-top: 48px !important
    }
}

@media screen and (min-width: 1921px) {

    .tall6up-background {
        height: 1560px;
        transform: translateY(-1580px);
    }
}






a.c-call-to-action.f-image[data-app-retailer] img {
   height: 40px;
}
.app-links a.c-call-to-action.f-image[data-app-retailer] {
   padding-top: 0px !important;
}

@media screen and (min-width: 0) {
.SB-app-2up .twoForeground {
    position: relative;
    top: -10.4vw;}

.SB-app-2up .m-banner.customTwoUp {
    padding-bottom: 6%;}
}

@media screen and (min-width: 768px) {
.SB-app-2up .twoForeground {
    position: relative;
    top: -8.4vw;}

.SB-app-2up .twoForeground .m-content-placement {
    margin-bottom: -13vw;}
}

@media screen and (min-width: 1084px) {
.SB-app-4up .m-banner.customFourUp, .SB-app-3up .m-banner.customThreeup {
    padding-bottom: 6%;}

.SB-app-4up .fourForeground {
    position: relative;
    top: -7.4vw;}

.SB-app-2up .twoForeground {
    position: relative;
    top: -5.4vw;}

.SB-app-4up .fourForeground .m-content-placement, .SB-app-3up .customThreeScootup .m-content-placement, .SB-app-2up .twoForeground .m-content-placement {
    margin-bottom: -7.4vw;}
}

.SB-app-4up .fourForeground section div, .SB-app-3up .customThreeScootup section div {
    text-align: center;
}

.SB-app-4up .customFourLinks a {
    text-align: center;
    display: inline-block;
    margin: 6px 12px;
}

@media screen and (min-width: 1921px) {
.SB-app-2up .twoForeground {
    position: relative;
    top: -115px;}
}

@media screen and (min-width: 3000px) {
.SB-app-4up .zoomOutPad, .SB-app-3up .zoomOutPad {padding-top:5% !important;}
}

@media screen and (min-width: 4000px) {
.SB-app-4up .zoomOutPad, .SB-app-3up .zoomOutPad, .SB-app-2up .zoomOutPad{padding-top:10% !important;}
}

@media screen and (min-width: 5300px) {
.SB-app-4up .zoomOutPad, .SB-app-3up .zoomOutPad, .SB-app-2up .zoomOutPad{padding-top:18% !important;}
}



@media screen and (max-width: 767px) {
  .SB-app-3up .customThreeup .c-subheading-1 {
      font-size: 20px;
      line-height: 24px;
  }
}

@media (min-width: 1084px) {
  .SB-app-3up .customThreeScootup {
      position: relative;
      top: -8vw;
  }
}

.SB-app-3up .app-links {
  padding-top: 2px;
}

.SB-app-3up .app-links a {
  margin-top: 6px;
  border: 2px solid transparent;
  outline: 2px solid transparent;
}

.SB-app-3up .app-links a:focus {
  outline: 2px dashed #000;
  border: 2px dashed #fff;
}

.SB-app-4up .app-links, .SB-app-3up .app-links {
  padding-top: 24px;
}

.SB-app-3up .app-links a {
  float: none;
  display: inline-block;
  margin-left: 7px;
  margin-right: 7px;
}


@media screen and (min-width: 767px) and (max-width: 1084px) {
    .SB-app-3up .theme-lighter {
      min-height: 180px;
    }
    .SB-app-3up .customThreeScootup {
      position: relative;
      top: -100px;
    }
}

@media screen and (max-width: 767px) {
    .SB-app-3up .theme-lighter {
        min-height: 220px;
    }
    .SB-app-3up .customThreeScootup {
        position: relative;
        top: -120px;
    }
}


.c-drawer>button[aria-expanded="false"]::before, .c-drawer .f-toggle[aria-expanded="false"]::before, .c-drawer>header>button[aria-expanded="false"]::before, .c-drawer>header .f-toggle[aria-expanded="false"]::before, .c-drawer .c-drawer-toggle[aria-expanded="false"]::before {
    content: "" !important;
  }
  
  .c-paragraph-1, .c-paragraph-2 {
    font-weight: 400 !important;
  }
  .c-heading, .c-heading-1, .c-heading-2, .c-heading-3, .c-heading-4 {
  font-weight: 700 !important;
  }
  .m-content-placement-item .c-heading, .m-content-placement-item .c-heading-1,
  .m-content-placement-item .c-heading-2, .m-content-placement-item .c-heading-3,
  .m-content-placement-item .c-heading-4 {
  font-weight: 600 !important;
  }
  
  
  .c-heading-1a {
    padding: 6px 0 6px;
    font-weight: 700;
    letter-spacing: -0.01em;
    font-family: SegoeProBlack, Segoe UI,SegoeUI,Helvetica,Arial,sans-serif;
  }
  
  
  .c-heading-1L {
    padding: 6px 0 6px;
    font-weight: 700;
    letter-spacing: -0.01em;
    font-family: SegoeProBlack, Segoe UI,SegoeUI,Helvetica,Arial,sans-serif;
  }
    
  
  @media screen and (min-width: 0px) {
    .c-heading-1a + .jump-g.jump-b {
   top:4px;
   }
    .c-heading-1a {
        font-size: 46px;
        line-height: 46px;
    }
    .c-heading-1L {
        font-size: 56px;
        line-height: 56px;
    }
    .jump-g.jump-b {
        font-size: 38px;
    }
  .c-heading-1a + .jump-g.jump-b {
        font-size: 45px;
        line-height: 25px;
    }
  }
  @media screen and (min-width: 360px) {
    .c-heading-1L {
        font-size: 66px;
        line-height: 66px;
    }
  }
  @media screen and (min-width: 768px) {
    .c-heading-1a {
        font-size: 62px;
        line-height: 60px;
    }
  }
  @media screen and (min-width: 1084px) {
  
    .c-heading-1L {
        font-size: 86px;
        line-height: 82px;
    }
    .jump-g.jump-b {
        font-size: 46px;
    }
  }    
  
  
  
  @media screen and (min-width: 1400px) {
     .c-heading-1L {
      font-size: 120px;
      line-height: 118px;
  }
    .jump-g.jump-b {
        font-size: 60px;
       line-height: 108px;
    }
  .c-heading-1a + .jump-g.jump-b {
        font-size: 66px;
        line-height: 42px;
    }
  }
  
  @media screen and (min-width: 1605px) {
    .c-heading-1a {
        font-size: 86px;
        line-height: 82px;
    }
  
    .c-heading-1L {
        font-size: 120px;
        line-height: 118px;
    }
  
  }
  
  .c-glyph::before, .c-glyph::after {
    font-family: MWFMDL2-Xbox;
  }
  
  .c-glyph::after {
    margin-left: 10px !important;
  }
  
  .jump-g {
    font-family: MWFMDL2-Xbox;
    color: #9bf00b !important;
    font-size: 43px;
   
  }
  
  
  
  .jumpgoffleft {
    right: 100%;
    opacity: 0;
  }
  
  .m-hero-item .c-subheading, .c-hero .c-subheading, .c-subheading, .c-subheading-1, .c-subheading-2, .c-subheading-3, .c-subheading-4 {
    font-weight: 400;
  }
  .m-hero-item .c-group > .c-call-to-action, .c-hero .c-group > .c-call-to-action {
    margin-right: 0px;
  }
  @media only screen and (max-width:499px) {
  .m-hero-item .c-group > .c-call-to-action + .c-call-to-action, .c-hero .c-group > .c-call-to-action + .c-call-to-action {
    padding: 10px 0 7px;
  }
  .m-hero-item .c-group > .c-call-to-action, .c-hero .c-group > .c-call-to-action  {
    margin-right: 10px;
  }
  }
  
  
  
  a.c-call-to-action.lime-green-c {
    color: #9bf00b !important;
    background: none !important;
  }
  
  
  a.c-call-to-action.lime-green-c:hover {
    color: #75b308;
    background: none !important;
  }
  
  a.c-call-to-action, 
  button.c-call-to-action, 
  .c-action-trigger, 
  .c-button,
  button.c-action-trigger, 
  button.c-button {
      font-family: SegoeProBlack, Segoe UI,SegoeUI,Helvetica,Arial,sans-serif;
  }
  
  a.c-call-to-action, button.c-call-to-action, 
  button.c-button.c-call-to-action,
  button.c-call-to-action.green-brdr:hover,
  .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action {
    border: 1px solid transparent;
    outline: 1px solid transparent;
  }
  
  
  a.c-call-to-action, button.c-call-to-action,
  .theme-light a.c-call-to-action,
  .theme-dark .theme-light a.c-call-to-action,
  .theme-light button.c-call-to-action,
  .theme-dark .theme-light button.c-call-to-action,
  .theme-dark a.c-call-to-action,
  .theme-light .theme-dark a.c-call-to-action,
  .theme-dark button.c-call-to-action,
  .theme-light .theme-dark button.c-call-to-action {
    padding: 5px 20px 5px 22px;
    color: #054b16;
    font-weight: 900;
    background: #9bf00b;
  }
  
   
    a:not(.x-hidden-focus).c-call-to-action:focus,
    .theme-light a:not(.x-hidden-focus).c-call-to-action:focus,
    .theme-dark a:not(.x-hidden-focus).c-call-to-action:focus
    .theme-black a:not(.x-hidden-focus).c-call-to-action:focus,
    a.c-call-to-action:hover,
    .theme-light a.c-call-to-action:hover,
    .theme-dark a.c-call-to-action:hover,
    .theme-black a.c-call-to-action:hover {
        background: #8bd80a;
    }
    a:not(.x-hidden-focus).c-call-to-action:focus {outline: 2px dashed #000; border: 2px dashed #fff;}
  a:not(.x-hidden-focus).c-call-to-action.f-image:focus {outline: 2px dashed #000; border: 2px dashed #fff;}
  
  a.c-call-to-action.f-image:hover,
  .theme-light a.c-call-to-action.f-image:hover,
  .theme-dark a.c-call-to-action.f-image:hover,
  .theme-black a.c-call-to-action.f-image:hover {background: transparent;}
  
  .m-image-intro :not(.f-primary):not(.f-secondary):not(.f-heavyweight).c-call-to-action,
  .c-feature :not(.f-primary):not(.f-secondary):not(.f-heavyweight).c-call-to-action,
  .m-feature :not(.f-primary):not(.f-secondary):not(.f-heavyweight).c-call-to-action,
  .m-content-placement-item a:not(.f-primary):not(.f-secondary):not(.f-heavyweight).c-call-to-action,
  .c-content-placement a:not(.f-primary):not(.f-secondary):not(.f-heavyweight).c-call-to-action {
  padding:10px 3px 7px 0;
  }
  .theme-black a.c-call-to-action:focus, .theme-light .theme-black a.c-call-to-action:focus, .theme-black button.c-call-to-action:focus, .theme-light .theme-black button.c-call-to-action:focus {
    border-color: #fff;
    outline-color: rgba(0, 0, 0, 0.6);
  }
  
  .theme-light a.c-call-to-action:focus, .theme-black .theme-light a.c-call-to-action:focus, .theme-light button.c-call-to-action:focus, .theme-black .theme-light button.c-call-to-action:focus {
    border-color: rgba(0, 0, 0, 0.6);
    outline-color: #fff;
  }
  .m-feature .c-call-to-action:not(.f-heavyweight):not(.f-primary):not(.f-secondary):focus:not(.x-hidden-focus) {
     border: 2px dashed #000;
     outline: 2px dashed #fff;
  }
  @media screen and (-ms-high-contrast: active) {
  .m-feature .c-call-to-action:not(.f-heavyweight):not(.f-primary):not(.f-secondary):focus:not(.x-hidden-focus) {
     border: 2px dashed #000 !important;
     outline: 2px dashed #fff !important;
  }
  }
  
  
  button.c-button {
    font-weight: 900;
  }
  
    button.c-button:hover {
        text-decoration: underline;
    }
  .c-group button.c-action-trigger {padding: 10px 3px 7px 0; margin: 0 2px; vertical-align: middle; }
  
  
  button.c-button,
  .theme-light button.c-button,
  a.c-button,
  .theme-light a.c-button {
    background-color: transparent;
    background: #505050;
    color: #fff;
    border: none;
  }
  
    button.c-button:hover,
    .theme-light button.c-button:hover,
    a.c-button:hover,
    .theme-light a.c-button:hover {
        background-color: transparent;
        background: #171717;
        color: #fff;
        border: none;
    }
  
    button.c-button:focus,
    .theme-light button.c-button:focus,
    a.c-button:focus,
    .theme-light a.c-button:focus,
    button:not(.x-hidden-focus).c-button:focus,
    .theme-light button:not(.x-hidden-focus).c-button:focus,
    a:not(.x-hidden-focus).c-button:focus,
    .theme-light a:not(.x-hidden-focus).c-button:focus {
        background-color: transparent;
        background: #171717;
        color: #fff;
        border: 1px solid #000;
        outline: 1px solid #fff;
    }
  
  
  .theme-black button.c-button,
  .theme-dark button.c-button,
  .theme-black a.c-button,
  .theme-dark a.c-button {
    background-color: transparent;
    background: #e6e6e6;
    color: #171717;
    border: none;
  }
  
    .theme-black button.c-button:hover,
    .theme-dark button.c-button:hover,
    .theme-black a.c-button:hover,
    .theme-dark a.c-button:hover {
        background-color: transparent;
        background: #9d9d9d;
        color: #171717;
        border: none;
    }
  
    .theme-black button.c-button:focus,
    .theme-dark button.c-button:focus,
    .theme-black a.c-button:focus,
    .theme-dark a.c-button:focus,
    .theme-black button:not(.x-hidden-focus).c-button:focus,
    .theme-dark button:not(.x-hidden-focus).c-button:focus,
    .theme-black a:not(.x-hidden-focus).c-button:focus,
    .theme-dark a:not(.x-hidden-focus).c-button:focus {
        background-color: transparent;
        background: #9d9d9d;
        color: #171717;
        border: 1px solid #000;
        outline: 1px solid #fff;
    }
  
    
    button.c-button.f-primary,
    .theme-light button.c-button.f-primary,
    a.c-button.f-primary,
    .theme-light a.c-button.f-primary,
    button[type='submit'].c-button,
    .theme-light button[type='submit'].c-button,
    .theme-black button.c-button.f-primary,
    .theme-dark button.c-button.f-primary,
    .theme-black a.c-button.f-primary,
    .theme-dark a.c-button.f-primary,
    .theme-black button[type='submit'].c-button,
    .theme-dark button[type='submit'].c-button {
        color: #054b16;
        background-color: #9bf00b;
        border: none;
    }
  
        button.c-button.f-primary:hover,
        .theme-light button.c-button.f-primary:hover,
        a.c-button.f-primary:hover,
        .theme-light a.c-button.f-primary:hover,
        button[type='submit'].c-button:hover,
        .theme-light button[type='submit'].c-button:hover,
        .theme-black button.c-button.f-primary:hover,
        .theme-dark button.c-button.f-primary:hover,
        .theme-black a.c-button.f-primary:hover,
        .theme-dark a.c-button.f-primary:hover,
        .theme-black button[type='submit'].c-button:hover,
        .theme-dark button[type='submit'].c-button:hover {
            color: #054b16;
            background-color: #8bd80a;
        }
  
        button.c-button.f-primary:focus,
        .theme-light button.c-button.f-primary:focus,
        a.c-button.f-primary:focus,
        .theme-light a.c-button.f-primary:focus,
        button[type='submit'].c-button:focus,
        .theme-light button[type='submit'].c-button:focus,
        .theme-black button.c-button.f-primary:focus,
        .theme-dark button.c-button.f-primary:focus,
        .theme-black a.c-button.f-primary:focus,
        .theme-dark a.c-button.f-primary:focus,
        .theme-black button[type='submit'].c-button:focus,
        .theme-dark button[type='submit'].c-button:focus,
        button:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-light button:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-dark button:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-black button:not(.x-hidden-focus).c-button.f-primary:focus,
        a:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-light a:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-dark a:not(.x-hidden-focus).c-button.f-primary:focus,
        .theme-black a:not(.x-hidden-focus).c-button.f-primary:focus,
        button[type='submit']:not(.x-hidden-focus).c-button:focus,
        .theme-light button[type='submit']:not(.x-hidden-focus).c-button:focus,
        .theme-dark button[type='submit']:not(.x-hidden-focus).c-button:focus,
        .theme-black button[type='submit']:not(.x-hidden-focus).c-button:focus {
            color: #054b16;
            background-color: #8bd80a;
            border: 2px solid #107c10;
            outline: 1px solid #000;
        }
  
  
  div:not(.c-group) > a.c-call-to-action ~ .f-lightweight {padding-left: 24px !important;}
  .c-group > a.c-call-to-action ~ .f-lightweight {padding-left: 0px !important;}
  .c-group > .f-lightweight {padding-left: 0px !important;}
  .c-group > a.c-call-to-action ~ a.c-call-to-action {margin-right: 0px !important;}
  .m-hero-item > .f-lightweight {padding-left: 0px !important;}
  
  a.c-call-to-action.f-lightweight,
  .theme-light a.c-call-to-action.f-lightweight,
  .theme-dark a.c-call-to-action.f-lightweight,
  button.c-call-to-action.f-lightweight,
  .theme-dark button.c-call-to-action.f-lightweight,
  .theme-light button.c-call-to-action.f-lightweight {
    padding: 10px 3px 7px 0;
  }
  
  
  
  .c-select-menu > a, .c-select-menu > button,
  .theme-light .c-select-menu > a, .theme-light .c-select-menu > button,
  .m-highlight-feature > div .c-call-to-action,
  .theme-light .m-highlight-feature > div .c-call-to-action,
  .theme-white .m-highlight-feature > div .c-call-to-action,
  .c-feature.f-background-neutral-00 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature.f-background-neutral-10 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature.f-background-neutral-20 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature.f-background-neutral-30 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.f-background-neutral-00 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.f-background-neutral-10 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.f-background-neutral-20 :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.f-background-neutral-30 :not(.f-primary):not(.f-secondary).c-call-to-action,
  button.c-button.f-lightweight,
  a.c-button.f-lightweight,
  .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action {
    color: #107c10;
    background: transparent;
    border: none;
  }
  
    .theme-light button.c-button.f-lightweight,
    .theme-light a.c-button.f-lightweight,
    .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action .theme-light {
        color: #054b16;
        background: transparent;
        border: none;
    }
    .c-select-menu > a:hover, .c-select-menu > button:hover,
     .theme-light .c-select-menu > a:hover, .theme-light .c-select-menu > button:hover,
        button.c-button.f-lightweight:hover,
        .theme-light button.c-button.f-lightweight:hover,
        a.c-button.f-lightweight:hover,
        .theme-light a.c-button.f-lightweight:hover {
            color: #054b16;
            background: transparent;
            border: none;
        }
  
  
  .theme-black .c-select-menu > a,.theme-black .c-select-menu > button,
  .theme-dark .c-select-menu > a, .theme-dark .c-select-menu > button,
  .theme-black button.c-button.f-lightweight,
  .theme-dark button.c-button.f-lightweight,
  .theme-black a.c-button.f-lightweight,
  .theme-dark a.c-button.f-lightweight {
    color: #9bf00b;
    background: transparent;
    border: none;
  }
         .theme-black .c-select-menu > a:hover, .theme-black .c-select-menu > button:hover,
     .theme-dark .c-select-menu > a:hover, .theme-dark .c-select-menu > button:hover,
    .theme-black button.c-button.f-lightweight:hover,
    .theme-dark button.c-button.f-lightweight:hover,
    .theme-black a.c-button.f-lightweight:hover,
    .theme-dark a.c-button.f-lightweight:hover {
        color: #75b308;
        background: transparent;
        border: none;
    }
  
  
  
  
  
  .m-panes-product-placement-item .c-call-to-action.green-brdr, a.c-call-to-action.green-brdr {padding:5px 20px 5px 22px !important;}
  a.c-action-trigger.green-brdr, button.c-action-trigger.green-brdr {padding:5px 20px 5px 10px !important;} 
  
  
  a.c-action-trigger.green-brdr,
  a.c-call-to-action.green-brdr,
  button.c-call-to-action.green-brdr,
  button.c-action-trigger.green-brdr{
    color: #107c10;
    background: rgba(255,255,255,0);
    border-color: #107c10;
  }
  .theme-light a.c-action-trigger.green-brdr,
  a.c-call-to-action.green-brdr,
  button.c-call-to-action.green-brdr,
  .theme-light a.c-call-to-action.green-brdr,
  .theme-light button.c-call-to-action.green-brdr,
  .theme-light button.c-action-trigger.green-brdr{
    color: #054b16;
    background: rgba(255,255,255,0);
    border-color: #107c10;
  }
    a.c-action-trigger.green-brdr:hover, button.c-action-trigger.green-brdr:hover,
    .theme-light a.c-action-trigger.green-brdr:hover, .theme-light button.c-action-trigger.green-brdr:hover,
    a:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, a.c-call-to-action.green-brdr:hover,
    button:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, 
    button.c-call-to-action.green-brdr:hover,
    .theme-light a:not(.x-hidden-focus).c-call-to-action.green-brdr:focus,
    .theme-light a.c-call-to-action.green-brdr:hover, .theme-dark .theme-light a:not(.x-hidden-focus).c-call-to-action.green-brdr:focus,
    .theme-dark .theme-light a.c-call-to-action.green-brdr:hover, .theme-light button:not(.x-hidden-focus).c-call-to-action.green-brdr:focus,
    .theme-light button.c-call-to-action.green-brdr:hover, .theme-dark .theme-light button:not(.x-hidden-focus).c-call-to-action.green-brdr:focus,
    .theme-dark .theme-light button.c-call-to-action.green-brdr:hover {
        color: #054b16;
        background: rgba(255,255,255,0.15) !important;
        border-color: #054b16;
    }
  
    a.c-call-to-action.green-brdr:focus, button.c-call-to-action.green-brdr:focus, .theme-light a.c-call-to-action.green-brdr:focus, .theme-light button.c-call-to-action.green-brdr:focus {
        border: 2px dashed #107c10;
        outline: 2px dashed #000;
    }
  
  .theme-dark a.c-action-trigger.green-brdr,
  .theme-black a.c-action-trigger.green-brdr,
  .theme-dark a.c-call-to-action.green-brdr, .theme-dark a.c-call-to-action.green-brdr, .theme-dark button.c-call-to-action.green-brdr, .theme-dark button.c-call-to-action.green-brdr,
  .theme-black a.c-call-to-action.green-brdr, .theme-black a.c-call-to-action.green-brdr, .theme-black button.c-call-to-action.green-brdr, .theme-black button.c-call-to-action.green-brdr,
  a.c-call-to-action.green-brdr.dark, button.c-call-to-action.green-brdr.dark
  .theme-dark button.c-action-trigger.green-brdr,
  .theme-black button.c-action-trigger.green-brdr,
  button.c-action-trigger.green-brdr.dark {
    background: none;
    color: #9bf00b !important;
    border-color: #9bf00b;
  }
  .theme-dark a.c-action-trigger.green-brdr:hover,
  .theme-black a.c-action-trigger.green-brdr:hover,
  .theme-dark a.c-action-trigger.green-brdr:focus,
  .theme-black a.c-action-trigger.green-brdr:focus,
  .theme-black a:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, .theme-black a.c-call-to-action.green-brdr:hover, 
  .theme-black button:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, 
  .theme-black button.c-call-to-action.green-brdr:hover,
  .theme-dark a:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, 
  .theme-dark a.c-call-to-action.green-brdr:hover, 
  .theme-dark button:not(.x-hidden-focus).c-call-to-action.green-brdr:focus, 
  .theme-dark button.c-call-to-action.green-brdr:hover,
  a:not(.x-hidden-focus).c-call-to-action.green-brdr.dark:focus, 
  a.c-call-to-action.green-brdr.dark:hover,
  .theme-dark button.c-action-trigger.green-brdr:hover,
  .theme-black button.c-action-trigger.green-brdr:hover,
  button.c-action-trigger.green-brdr.dark:hover,
  .theme-dark button.c-action-trigger.green-brdr:focus,
  .theme-black button.c-action-trigger.green-brdr:focus  {
        background: rgba(0,0,0,0.15) !important;
        color: #9bf00b;
        border-color: #9bf00b;
    }
  
    .theme-black a.c-call-to-action.green-brdr:focus, .theme-black button.c-call-to-action.green-brdr:focus, .theme-dark a.c-call-to-action.green-brdr:focus, .theme-dark button.c-call-to-action.green-brdr:focus,
    a.c-call-to-action.green-brdr.dark:focus, button.c-call-to-action.green-brdr.dark:focus{
        border: 2px solid #9bf00b;
        outline: 1px solid #fff;
    }
  
  
  
  .theme-light a.c-call-to-action.f-secondary, .theme-light button.c-call-to-action.f-secondary, a.c-call-to-action.f-secondary, button.c-call-to-action.f-secondary {
    color: #fff;
    background: #505050;
    border: none;
  }
  
    a.c-call-to-action.f-secondary:hover,
    button.c-call-to-action.f-secondary:hover,
    .theme-light a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,.theme-white a.c-call-to-action.f-secondary:focus:not(.x-hidden-focus), a.c-call-to-action.f-secondary:focus:not(.x-hidden-focus),  
    .theme-light a.c-call-to-action.f-secondary:hover,
    .theme-light a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, 
    .theme-light button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,
    .theme-light button.c-call-to-action.f-secondary:hover,
    .theme-light button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,
    .theme-light button.c-call-to-action.f-secondary:hover {
        background: #171717;
    }
   
      .theme-light a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-light a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,
    .theme-light button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,  .theme-light button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus{
        border: 2px dashed #000;
        outline: 2px dashed #fff;
    }
  
  .theme-black a.c-call-to-action.f-secondary, .theme-black a.c-call-to-action.f-secondary, .theme-black button.c-call-to-action.f-secondary, .theme-black button.c-call-to-action.f-secondary, .theme-dark a.c-call-to-action.f-secondary, .theme-dark a.c-call-to-action.f-secondary,
  .theme-dark button.c-call-to-action.f-secondary, .theme-dark button.c-call-to-action.f-secondary {
    background: #e6e6e6;
    color: #171717;
    border: none
  }
  
    .theme-black a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-black a.c-call-to-action.f-secondary:hover, .theme-black a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-black a.c-call-to-action.f-secondary:hover, .theme-black button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,
    .theme-black button.c-call-to-action.f-secondary:hover, .theme-black button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-black button.c-call-to-action.f-secondary:hover, .theme-dark a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-dark a.c-call-to-action.f-secondary:hover, .theme-dark a:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-dark a.c-call-to-action.f-secondary:hover, .theme-dark button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus,
    .theme-dark button.c-call-to-action.f-secondary:hover, .theme-dark button:not(.x-hidden-focus).c-call-to-action.f-secondary:focus, .theme-dark button.c-call-to-action.f-secondary:hover {
        background: #9d9d9d;
        color: #171717;
        border: 2px dashed #000;
        outline: 2px dashed #fff;
    }
  
    
  
  .m-content-placement-item .c-call-to-action.f-heavyweight,
  .c-content-placement .c-call-to-action.f-heavyweight,
  .m-content-placement-item .c-call-to-action.f-heavyweight,
  .c-content-placement .c-call-to-action.f-heavyweight,
  a.c-call-to-action.f-heavyweight {
    padding: 5px 20px 5px 22px;
    color: #054b16;
    font-weight: 900;
    background: #9bf00b;
  }
  .m-content-placement-item .c-call-to-action.f-heavyweight:hover,
  .c-content-placement .c-call-to-action.f-heavyweight:hover,
  .m-content-placement-item .c-call-to-action.f-heavyweight:hover,
  .c-content-placement .c-call-to-action.f-heavyweight:hover,
  a.c-call-to-action.f-heavyweight:hover {
    background: #8bd80a;
  }
    
  
  
  
  a.c-call-to-action.f-lightweight,
  button.c-call-to-action.f-lightweight,
  .m-panes-product-placement-item :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-light .m-panes-product-placement-item :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-content-placement-item .c-call-to-action,
  .c-content-placement .c-call-to-action,
  .theme-white a.c-call-to-action.f-lightweight,
  .theme-white button.c-call-to-action.f-lightweight,
  .c-feature.theme-white :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.theme-white :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-content-placement-item.theme-white .c-call-to-action,
  .c-content-placement.theme-white .c-call-to-action {
    color: #107c10;
  }
  
  
  .theme-light .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-dark .theme-light .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-light .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-dark .theme-light .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-light .m-banner .c-call-to-action, .theme-dark .theme-light .m-banner .c-call-to-action,
  .theme-light .m-content-placement-item .c-call-to-action,
    .theme-light .c-content-placement .c-call-to-action,
  .theme-light a.c-call-to-action.f-lightweight,
  .theme-light button.c-call-to-action.f-lightweight,
  .c-feature.theme-light :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.theme-light :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-content-placement-item.theme-light .c-call-to-action,
  .c-content-placement.theme-light .c-call-to-action {
    color: #054b16;
  }
  .theme-white .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action, 
  .theme-dark .theme-white .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-white .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-dark .theme-white .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-white .m-banner .c-call-to-action, .theme-dark .theme-white .m-banner .c-call-to-action,
  .theme-white .m-content-placement-item .c-call-to-action, .theme-white .c-content-placement .c-call-to-action,
  .theme-white a.c-call-to-action.f-lightweight, .theme-white button.c-call-to-action.f-lightweight,
  .c-feature.theme-white :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.theme-white :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-content-placement-item.theme-white .c-call-to-action, .c-content-placement.theme-white .c-call-to-action {
    color: #107c10;
  }
  .pregamelist a.c-call-to-action.f-lightweight,
  .gameSelector a.c-call-to-action.f-lightweight,
  .faq-mwf a.c-call-to-action.f-lightweight,
  .m-rich-heading a.c-call-to-action.f-lightweight,
  .m-panes-product-placement-item :not(.f-primary):not(.f-secondary):not(.f-heavyweight):not(.customize-button).c-call-to-action,
  .m-content-placement-item :not(.f-primary):not(.f-secondary):not(.f-heavyweight):not(.customize-button).c-call-to-action,
    .c-content-placement :not(.f-primary):not(.f-secondary):not(.f-heavyweight):not(.customize-button).c-call-to-action {
    padding: 10px 3px 7px 0;
  }
  
     .m-content-placement-item a.c-call-to-action:hover {background: none;}
  
    .theme-light a:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-light a.c-call-to-action.f-lightweight:hover,
    .theme-light a:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-light a.c-call-to-action.f-lightweight:hover,
    .theme-light button:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-light button.c-call-to-action.f-lightweight:hover,
    .theme-light button:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-light button.c-call-to-action.f-lightweight:hover,
    .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .c-feature.theme-light :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .m-feature.theme-light :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .m-content-placement-item .c-call-to-action:hover,
    .c-content-placement .c-call-to-action:hover,
    .m-content-placement-item.theme-light .c-call-to-action:hover,
    .c-content-placement.theme-light .c-call-to-action:hover {
        color: #054b16;
    }
  
  a.c-call-to-action.f-lightweight:hover span, button.c-call-to-action.f-lightweight:hover span {
    text-decoration: none;
  }
  
  .theme-light a.c-call-to-action.f-lightweight:focus,
  a.c-call-to-action.f-lightweight:focus,
  .theme-light button.c-call-to-action.f-lightweight:focus,
  button.c-call-to-action.f-lightweight:focus,
  a:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
  button:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus {
    border: 2px dashed #000;
    outline: 2px dashed #fff;
  }
  
  
  .theme-dark a.c-call-to-action.f-lightweight,
  .theme-dark a.c-call-to-action.f-lightweight,
  .theme-dark button.c-call-to-action.f-lightweight,
  .theme-dark button.c-call-to-action.f-lightweight,
  .theme-black a.c-call-to-action.f-lightweight,
  .theme-black a.c-call-to-action.f-lightweight,
  .theme-black button.c-call-to-action.f-lightweight,
  .theme-black button.c-call-to-action.f-lightweight,
  .m-feature.theme-black :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature.theme-black :not(.f-primary):not(.f-secondary).c-call-to-action,
  .c-feature.theme-dark :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-feature.theme-dark :not(.f-primary):not(.f-secondary).c-call-to-action,
  
  .theme-black .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-black .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-dark .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .theme-dark .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action,
  .m-content-placement-item.theme-black .c-call-to-action, .c-content-placement.theme-black .c-call-to-action,
  .m-content-placement-item.theme-dark .c-call-to-action, .c-content-placement.theme-dark .c-call-to-action,
  .m-feature.theme-dark .c-call-to-action:not(.f-primary):not(.f-secondary):focus:not(.x-hidden-focus),
  .m-feature.theme-black .c-call-to-action:not(.f-primary):not(.f-secondary):focus:not(.x-hidden-focus),
  .theme-black .m-content-placement-item :not(.f-heavyweight).c-call-to-action, .theme-black .c-content-placement :not(.f-heavyweight).c-call-to-action{
    color: #9bf00b;
  }
  .theme-black .m-content-placement-item .f-heavyweight.c-call-to-action:focus:not(.x-hidden-focus),
  .theme-dark .m-content-placement-item .f-heavyweight.c-call-to-action:focus:not(.x-hidden-focus) {
  color:#8bd80a;
  }
  
    .theme-dark a.c-call-to-action.f-lightweight:hover,
    .theme-dark a.c-call-to-action.f-lightweight.white-c:hover,
    .theme-black a.c-call-to-action.f-lightweight:hover,
    .theme-dark button.c-call-to-action.f-lightweight:hover,
    .theme-black button.c-call-to-action.f-lightweight:hover
    .theme-dark a:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-black a:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-dark button:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .theme-black button:not(.x-hidden-focus).c-call-to-action.f-lightweight:focus,
    .c-feature.theme-black :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .m-feature.theme-black :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .c-feature.theme-dark :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .m-feature.theme-dark :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
    .theme-black .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
  .theme-black .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
  .theme-dark .c-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover,
  .theme-dark .m-feature :not(.f-primary):not(.f-secondary).c-call-to-action:hover{
        color: #75b308;
        background: none;
    }
  
    .theme-dark a.c-call-to-action.f-lightweight:focus,
    .theme-black a.c-call-to-action.f-lightweight:focus,
    .theme-dark button.c-call-to-action.f-lightweight:focus,
    .theme-black button.c-call-to-action.f-lightweight:focus {
        border-color: #fff;
        outline-color: rgba(0, 0, 0, 0.6);
    }
  
  
  
  
  a.c-hyperlink{
    text-decoration: underline;
    color: #107c10;
  }
  a.c-hyperlink:focus {
    border: 2px dashed #000;
    outline: 2px dashed #fff;
  
  }
  
  .theme-light a.c-hyperlink {
    text-decoration: underline;
    color: #054b16;
  }
  
   
    .theme-light a.c-hyperlink:hover,   
    .theme-light a:not(.f-image):not(.x-hidden-focus).c-hyperlink:focus,  
    .theme-light a:not(.f-image).c-hyperlink:hover {     
        color: #000;     
    }
  
    a.c-hyperlink:hover,
    a:not(.f-image):not(.x-hidden-focus).c-hyperlink:focus,   
    a:not(.f-image).c-hyperlink:hover {     
        color: #054b16; 
    }
  
  
  .theme-black a.c-hyperlink,
  .theme-dark a.c-hyperlink {
    text-decoration: underline;
    color: #9bf00b;
  }
  
  .theme-black a.c-hyperlink:hover,
  .theme-dark a.c-hyperlink:hover,
  .theme-black a:not(.f-image):not(.x-hidden-focus).c-hyperlink:focus,
  .theme-dark a:not(.f-image):not(.x-hidden-focus).c-hyperlink:focus,
  .theme-black a:not(.f-image).c-hyperlink:hover,
  .theme-dark a:not(.f-image).c-hyperlink:hover {    
    color: #75b308;   
  }
  
  
  button.c-action-trigger.c-glyph, a.c-action-trigger.c-glyph {
    font-weight: 900;
  }
  
  button.c-action-trigger,
  a.c-action-trigger,.m-banner .c-call-to-action {
    color: #107c10;
  }
  
  .theme-light button.c-action-trigger,
  .theme-light a.c-action-trigger {
    color: #054b16;
  }
  
  button.c-action-trigger:hover,
  .theme-light button.c-action-trigger:hover,
  a.c-action-trigger:hover,
  .theme-light a.c-action-trigger:hover {
    color: #054b16;
  }
  
  
  .theme-black button.c-action-trigger,
  .theme-dark button.c-action-trigger,
  .theme-black a.c-action-trigger,
  .theme-dark a.c-action-trigger,
  .theme-black a.c-action-trigger:focus,
  .theme-black button.c-action-trigger:focus {
    color: #9bf00b;
  }
  
  .theme-black button.c-action-trigger:hover,
  .theme-dark button.c-action-trigger:hover,
  .theme-black a.c-action-trigger:hover,
  .theme-dark a.c-action-trigger:hover {
    color: #75b308;
  }
  
  
  @media screen and (-ms-high-contrast: black-on-white) {
  [class*="m-"]:not(.m-in-page-navigation) button:not(.c-select-button):not(.c-sequence-indicator):hover:not(:disabled):not(.vidPlayPause):not(.c-action-toggle), 
  [class*="m-"]:not(.m-in-page-navigation) button:not(.c-select-button):not(.c-sequence-indicator):focus:not(:disabled):not(.c-flipper):not(.vidPlayPause):not(.c-action-toggle) {
    color: #000 !important;
    background-color: transparent !important;}
  }
  
  @media screen and (-ms-high-contrast: white-on-black) {
  [class*="m-"]:not(.m-in-page-navigation) button:not(.c-select-button):not(.c-sequence-indicator):hover:not(:disabled):not(.vidPlayPause):not(.c-action-toggle), 
  [class*="m-"]:not(.m-in-page-navigation) button:not(.c-select-button):not(.c-sequence-indicator):focus:not(:disabled):not(.c-flipper):not(.vidPlayPause):not(.c-action-toggle) {
      color: #FFF !important;
      background-color: transparent !important;}
  }
  
  
  
  
  
  
  
  .m-content-placement-item .c-paragraph-1, .c-paragraph-2 {
    font-weight: 400 !important;
  }
  
  .m-highlight-feature > div .c-heading {
    font-weight: 700 !important;
  }
.SegoeProBlack {
    font-family: 'SegoeProBlack';
}

.MWFMDL2-Xbox {
    font-family: 'MWFMDL2-Xbox';
}

a {
    color: inherit;
}

.theme-dark .c-mosaic-placement picture::after,
.theme-light .theme-dark .c-mosaic-placement picture::after {
    background: none;
}

.clear {
    display: none;
}




.qlButton.popupShow {
    display: none !important;
}

a.gameDivLink.eappgame {
    pointer-events: none !important;
    cursor: auto !important;
}







sup,
sub {
    font-size: 75%;
}




body hr {
    width: auto;
    background-color: transparent;
}




.c-uhf-menu button:after {
    padding-top: 5px;
}

div[data-module-id] {
    min-height: 0px;
}

.c-uhff {
    margin-top: 0px;
}

.c-uhfh-actions a.c-call-to-action,
.c-uhfh-actions button.c-call-to-action,
.c-uhfh-actions .c-action-trigger,
.c-button {
    font-family: Segoe UI, SegoeUI, "Helvetica Neue", Helvetica, Arial, sans-serif;
}

a.c-hyperlink:link,
a.c-hyperlink:focus,
a.c-hyperlink:hover,
a.c-hyperlink:active,
a.c-hyperlink:visited {
    text-decoration: underline !important;
}

.c-feature picture img,
.m-feature picture img {
    min-height: 0 !important;
}

@media only screen and (min-width:540px) {
    .c-feature.f-align-left,
    .m-feature.f-align-left,
    .c-feature.f-align-right,
    .m-feature.f-align-right {
        min-height: initial;
    }
}

@media only screen and (min-width:768px) {
    .c-feature.f-align-left,
    .m-feature.f-align-left,
    .c-feature.f-align-right,
    .m-feature.f-align-right {
        min-height: initial;
    }
}

@media only screen and (min-width:1084px) {
    .c-feature.f-align-center>div,
    .m-feature.f-align-center>div {
        max-width: 100%;
    }
}

@media only screen and (min-width:1921px) {
    section.m-hero-item,
    div.m-hero,
    .legal, 
    .characterRotate {
        max-width: 1920px;
        margin: 0 auto;
    }
}

.m-product-placement-item .c-paragraph {
    white-space: normal;
}




.m-hero-item .c-paragraph,
.c-hero .c-paragraph,
.m-multi-feature [role="tabpanel"] .c-paragraph,
.c-feature>div .c-paragraph,
.m-feature>div .c-paragraph,
.c-paragraph {
    font-size: 15px;
    line-height: 23px;
    max-height: 100%;
}

@media screen and (min-width:1084px) {
    .m-content-placement {
        margin-left: 0px;
        margin-right: 0px;
    }
}

@media screen and (-ms-high-contrast: active), screen and (forced-colors: active) {
    .m-content-placement-item .c-call-to-action:focus,
    .c-content-placement .c-call-to-action:focus,
    button.c-action-trigger:focus,
    a.c-action-trigger:focus,
    a.c-hyperlink:focus,
    a.c-call-to-action.f-lightweight:focus,
    button.c-call-to-action.f-lightweight:focus {
        border: 2px dashed #fff !important;
        outline: 2px dashed #000 !important;
    }
}

@media screen and (-ms-high-contrast: active), screen and (forced-colors: active) {
    [class^="m-"] a:not(.c-action-trigger):focus:not(.x-hidden-focus),
    [class*=" m-"] a:not(.c-action-trigger):focus:not(.x-hidden-focus),
    [class^="c-"] a:not(.c-action-trigger):focus:not(.x-hidden-focus),
    [class*=" c-"] a:not(.c-action-trigger):focus:not(.x-hidden-focus) {
        outline: 2px dashed #000 !important;
        border: 2px dashed #FFF !important;
    }
}

.m-page-bar {
    display: block;
}

@media screen and (max-width: 768px) {
    .m-page-bar>div>div {
        top: 0px;
        position: absolute;
    }
    .m-highlight-feature {
        display: block;
    }
    .onePointFive .m-highlight-feature {
        display: flex;
    }
}







.m-multi-feature>section .c-carousel {
    height: 100%;
    
}







.c-age-rating .c-content-toggle .c-list {
    overflow: visible;
}

fieldset.c-checkbox label.c-label {
    float: none;
}

@media (min-width: 1400px) and (max-width: 1600px) {
    .triptych [data-grid~=container] {
        padding: 0 !important;
    }
}




@media screen and (max-width: 1084px) {
    .v-hidden.h-divider {
        border-right: 0px solid rgba(0, 0, 0, .2);
    }
}

@media only screen and (min-width:768px) {
    a.m-back-to-top,
    a.c-back-to-top {
        background: #9bf00b !important;
    }
    a.m-back-to-top:hover,
    a.m-back-to-top:focus,
    a.c-back-to-top:hover,
    a.c-back-to-top:focus {
        background: #107c10 !important;
    }
}




a[data-app-retailer]:focus {
    border: 2px dashed #000;
    outline: 2px dashed #fff;
}

@media screen and (min-width: 1921px) {
    .hero-center {
        max-width: 1920px;
        margin: 0 auto;
    }
}




.theme-dark button.c-action-toggle:hover,
.theme-light .theme-dark button.c-action-toggle:hover {
    color: #ccc;
}

button[aria-label].c-action-toggle.c-glyph {
    font-weight: 700;
    font-size: 18px;
}




@media screen and (min-width: 1084px) {
    
    .c-carousel>.c-group {
        width: 86%;
        margin-left: 7%;
        margin-right: 7%;
    }
}

.c-sequence-indicator,
.c-action-toggle {
    background-color: rgba(0, 0, 0, 0.3) !important;
}

.c-sequence-indicator button::before,
.c-sequence-indicator a::before {
    border: 1px solid rgb(0, 0, 0);
}

.c-sequence-indicator button:focus,
.c-sequence-indicator a:focus,
.high-contrast-mode .c-sequence-indicator button[aria-selected="true"] {
    outline: 2px dashed #fff !important;
    border: 2px dashed #000 !important;
}

.c-sequence-indicator button,
.c-sequence-indicator a {
    width: 22px;
    height: 20px;
}

@media only screen and (max-width:539px) {
    .box-shots .c-content-placement>a:first-child>picture img,
    .box-shots .m-content-placement-item>a:first-child>picture img {
        padding: 0 60px 0 30px;
    }
    .c-hero .c-paragraph,
    .c-hero .c-price,
    .c-hero .c-rating,
    .m-hero-item .c-paragraph,
    .m-hero-item .c-price,
    .m-hero-item .c-rating {
        display: block
    }
    .c-pivot>header>a {
        display: table-caption;
    }
    .c-pivot>header>a:first-child,
    .c-pivot>header>a {
        padding-left: 16vw;
    }
    .c-pivot>header {
        display: table-header-group !important;
    }
}

.c-pivot>[role="tablist"]>[role="tab"] {
    font-weight: 600;
}

.theme-black .c-pivot>header>[role='tab'],
.theme-black .c-pivot>header a,
.theme-black .c-pivot>div>[role='tab'],
.theme-black .c-pivot>div a,
.theme-black .c-pivot>[role='tablist']>[role='tab'],
.theme-black .c-pivot>[role='tablist'] a,
.theme-dark .c-pivot>header>[role='tab'],
.theme-dark .c-pivot>header a,
.theme-dark .c-pivot>div>[role='tab'],
.theme-dark .c-pivot>div a,
.theme-dark .c-pivot>[role='tablist']>[role='tab'],
.theme-dark .c-pivot>[role='tablist'] a {
    color: #e6e6e6;
}

.theme-black :not(.f-disabled).c-pivot>header>[role='tab'].f-active,
.theme-black :not(.f-disabled).c-pivot>header a.f-active,
.theme-black :not(.f-disabled).c-pivot>div>[role='tab'].f-active,
.theme-black :not(.f-disabled).c-pivot>div a.f-active,
.theme-black :not(.f-disabled).c-pivot>[role='tablist']>[role='tab'].f-active,
.theme-black :not(.f-disabled).c-pivot>[role='tablist'] a.f-active,
.theme-dark :not(.f-disabled).c-pivot>header>[role='tab'].f-active,
.theme-dark :not(.f-disabled).c-pivot>header a.f-active,
.theme-dark :not(.f-disabled).c-pivot>div>[role='tab'].f-active,
.theme-dark :not(.f-disabled).c-pivot>div a.f-active,
.theme-dark :not(.f-disabled).c-pivot>[role='tablist']>[role='tab'].f-active,
.theme-dark :not(.f-disabled).c-pivot>[role='tablist'] a.f-active {
    color: #fff;
    font-weight: 600;
}

.theme-black .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action,
.theme-dark .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action {
    color: #9bf00b;
}

.theme-black .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:hover,
.theme-dark .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:hover {
    color: #75b308;
    background: none;
}

.theme-black .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:focus,
.theme-dark .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:focus {
    border-color: #fff;
    outline-color: rgba(0, 0, 0, 0.6);
    color: #fff;
}

.m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action,
.theme-light .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action {
    color: #107c10;
}

.m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:hover,
.theme-light .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:hover {
    color: #094709;
    background: none;
}

.m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:focus,
.theme-light .m-multi-feature:not(.f-console) [role="tabpanel"] .c-call-to-action:focus {
    border-color: #000;
    outline-color: rgba(0, 0, 0, 0.6);
}

@media only screen and (max-width:767px) {
    nav.c-link-navigation li a.c-hyperlink {
        text-decoration: underline;
    }
    .accessories-blade .c-heading {
        text-align: left;
    }
    .acc-small img {
        margin: 0 auto !important;
    }
    .m-rich-heading>picture.c-image+div .c-heading {
        bottom: 120px !important;
    }
    .m-rich-heading>picture.c-image+div>div {
        position: absolute;
        bottom: 30px;
        z-index: 1;
    }
    .h-divider {
        border-right: none !important;
    }
    [class*=f-x][class*=f-y].c-hero>div>div,
    [class*=f-x][class*=f-y].m-hero-item>div>div {
        top: calc(35%);
    }
}

.m-rich-heading .c-heading {
    max-height: 95px;
}

.m-product-placement-item>a:hover .c-heading,
.m-product-placement-item>a:hover .c-subheading,
.c-product-placement>a:hover .c-heading,
.c-product-placement>a:hover .c-subheading,
.m-product-placement-item>a:hover .c-paragraph,
.m-product-placement-item>a:focus .c-heading,
.m-product-placement-item>a:focus .c-subheading,
.c-product-placement>a:focus .c-heading,
.c-product-placement>a:focus .c-subheading,
.m-product-placement-item>a:focus .c-paragraph {
    text-decoration: underline;
}

.m-content-placement-item .xpa {
    margin-top: 20px;
}

.m-content-placement-item .c-paragraph {
    line-height: 1.35;
}

.c-badge.f-small {
    line-height: normal;
}
.c-badge.f-highlight {font-weight: 700;}

.link-marg-left {
    margin-left: 15px !important;
}

.zmt {
    margin-top: 0px !important;
}

.zpt {
    padding-top: 0px !important;
}

.zpl {
    padding-left: 0px !important;
}

.zpb {
    padding-bottom: 0px !important;
}

.btn-def-marg {
    margin-left: -24px !important;
}

.bottom-def-margin {
    margin-bottom: 48px !important;
}

.context-control-appearance>[class^='m-'] {
    margin-top: 0px;
    padding: 0;
}

@media screen and (max-width: 540px) {
    .zpl {
        padding-left: 24px !important;
    }
}

.pad48 {
    padding-top: 48px !important;
}

.pad96 {
    padding-top: 96px !important;
}

@media screen and (max-width: 768px) {
    .pad48,
    .pad96 {
        padding-top: 0px !important;
    }
}

.static48 {
    padding-top: 48px !important;
}

.static96 {
    padding-top: 96px !important;
}




.white-c {
    color: #fff !important;
}

a.white-c:hover {
    color: #9bf00b !important;
}

.darkGrey-c {
    color: #505050 !important;
}

.black-c {
    color: #000 !important;
}

.green-c {
    color: #107c10 !important;
}

.lime-green-c {
    color: #9bf00b !important;
}

.dark-green-c {
    color: #054b16 !important;
}

.noClick {
    cursor: default;
    text-decoration: none;
}

.noClick img {
    opacity: 1 !important;
}

.noClick:hover {
    text-decoration: none;
}

.c-content-placement.noClick:hover>div .c-heading,
.c-content-placement.noClick:hover>div>.c-call-to-action span,
.c-content-placement.noClick:hover>div>.c-group> :first-child.c-call-to-action span,
.c-content-placement.noClick:hover>div>.c-group> :first-child.c-hyperlink,
.c-content-placement.noClick:hover>div>.c-hyperlink,
.c-content-placement.noClick>a:first-child :not(.x-hidden-focus).c-call-to-action:focus span,
.c-content-placement.noClick>a:first-child .c-call-to-action:hover span,
.m-content-placement-item.noClick:hover>div .c-heading,
.m-content-placement-item.noClick:hover>div>.c-call-to-action span,
.m-content-placement-item.noClick:hover>div>.c-group> :first-child.c-call-to-action span,
.m-content-placement-item.noClick:hover>div>.c-group> :first-child.c-hyperlink,
.m-content-placement-item.noClick:hover>div>.c-hyperlink,
.m-content-placement-item.noClick>a:first-child :not(.x-hidden-focus).c-call-to-action:focus span,
.m-content-placement-item.noClick>a:first-child .c-call-to-action:hover span {
    cursor: default;
}

.c-age-rating .c-content-toggle button {
    display: none !important;
}




@media (min-width: 541px) and (max-width: 767px) {
    .accessories-blade .acc-small {
        float: left;
        padding: 0 25px;
    }
    .c-feature.f-align-left>div,
    .c-feature.f-align-right>div {
        width: auto !important;
    }
}

a.c-call-to-action.customize-button {
    color: #fff !important;
}

.m-panes-product-placement-item a.c-call-to-action.customize-button,
a.c-call-to-action.customize-button {
    padding: 5px 10px 5px 45px !important
}

a.customize-button::before,
button.customize-button::before,
div.customize-button::before {
    content: "";
    background-image: url('https://assets.xboxservices.com/assets/e0/0d/e00dab0b-2727-449d-8b9f-f563bb3491fa.png?n=xdl-icon.png');
    position: absolute;
    top: 2px;
    left: 2px;
    width: 25px;
    height: 25px;
    background-size: 100% 100%;
}

a.customize-button,
button.customize-button,
div.customize-button {
    padding-left: 50px !important;
    padding-right: 25px !important;
    box-sizing: border-box;
    display: inline-block;
    white-space: nowrap;
    width: auto;
    min-width: 110px;
    text-decoration: none;
    position: relative;
}

a.customize-button:hover {
    color: #ccc !important;
}

a:not(.x-hidden-focus).c-call-to-action.customize-button:focus {
    border: 2px dashed #fff !important;
    outline: 2px dashed #000 !important;
    color: #ccc !important;
}

.accessories-blade .c-price {
    margin-top: 1vw;
}

.c-call-to-action.cta-btn-dark:active,
.c-call-to-action.cta-btn-dark:focus {
    background: #000 !important;
}

a.c-call-to-action.cta-btn-dark {
    background: #000;
    color: #fff;
    margin-left: 0px;
}

a.c-call-to-action.cta-btn-dark:hover {
    background: #464646;
}







@media only screen and (max-width: 1399px) {
    .m-panes-product-placement-item {
        width: 100%
    }
}

a.c-call-to-action.cta-btn {
    background: #107c10;
    color: #fff;
    margin-left: 0px;
    padding-left: 10px;
    padding-right: 25px;
}

.c-call-to-action.cta-btn:focus,
.c-call-to-action.cta-btn:hover {
    background: #0e6c0e !important;
    border-color: rgba(0, 0, 0, .4) !important;
    color: #fff;
    text-decoration: none !important;
}

.c-call-to-action.cta-btn:focus span,
.c-call-to-action.cta-btn:hover span {
    text-decoration: none !important;
    color: #fff;
}

.cta-btn.c-glyph:hover::after,
.cta-btn.c-glyph:hover::before {
    color: #fff;
}

a.c-call-to-action.cta-btn-dark {
    margin-top: 10px;
}







@media only screen and (min-width: 1084px) {
    .m-banner {
        max-width: 1000px !important;
    }
}

.m-area-heading .c-call-to-action {
    margin-top: 14px;
}

.m-area-heading {
    padding-top: 48px !important;
}

.m-banner .c-caption-1 {
    line-height: 1.3
}




.m-banner.banner-leaner {
    padding-top: 20px;
}




.greenBar {
    padding-bottom: 48px;
}

.greenBar .m- {
    text-align: center;
}

.greenBar p {
    padding: 24px 0;
}

.greenBar .c-image.winLogos {
    max-width: 446px;
    margin: 0 auto;
    padding: 0 10px;
    width: 100%;
}

.greenBar h3,
.greenBar a {
    display: inline-table !important;
    margin: 0 10px;
}




.theme-white {
    color: #000;
    background-color: rgba(255, 255, 255, 1);
}

.theme-lighter {
    color: #000;
    background-color: rgba(238, 238, 238, 1);
}

.theme-f2 {
    color: #000;
    background-color: #f2f2f2 !important;
}

.theme-e3 {
    color: #000;
    background-color: #e3e3e3 !important;
}

.theme-2f {
    color: #fff;
    background-color: #2f2f2f !important;
}

.theme-black {
    color: #fff;
    background-color: #000 !important;
}

.theme-dkgray {
    background-color: #201f24;
    color: #fff;
}

.theme-green {
    color: #fff;
    background-color: #107c10 !important;
}

.theme-madden-blue {
    color: #fff;
    background-color: #091937 !important;
}

body .theme-transparent {
    background-color: transparent !important;
}

.badge-silver {
    background-color: #C8C8C8 !important;
}

.theme-dark .m-panes section {
    border-left: 1px solid #fff;
}

.theme-dark .m-panes section:first-child {
    border-left: 0px;
}

@media only screen and (max-width:1399px) {
    .theme-dark .m-panes section {
        border-bottom: 1px solid #fff;
        border-left: 0;
    }
}

@media screen and (min-width: 1400px) {
    .dark-gray-bg .m-panes section.f-stacked {
        border-left: 1px solid #FFFFFF;
    }
    .dark-gray-bg .m-panes section.f-stacked>div+div:last-of-type {
        border-top: 1px solid #FFFFFF;
    }
}

@media screen and (max-width: 1399px) and (min-width: 768px) {
    .dark-gray-bg .m-panes section.f-align-middle {
        border-bottom: 1px solid #FFFFFF;
    }
    .dark-gray-bg .m-panes section.f-stacked>div+div:last-of-type {
        border-left: 1px solid #FFFFFF;
    }
}

@media screen and (max-width: 767px) and (min-width: 540px) {
    .dark-gray-bg .m-panes section.f-align-middle {
        border-bottom: 1px solid #FFFFFF;
    }
    .dark-gray-bg .m-panes section.f-stacked>div+div:last-of-type {
        border-left: 1px solid #FFFFFF;
    }
}

@media screen and (max-width: 539px) {
    .dark-gray-bg .m-panes section.f-align-middle {
        border-bottom: 1px solid #FFFFFF;
    }
    .m-panes section.f-stacked>div+div:last-of-type {
        border-top: 1px solid #FFFFFF;
    }
}




.infinite .m-product-placement-item {
    display: inline-block;
}

.infinite .c-product-placement picture,
.infinite .c-product-placement picture .c-image,
.infinite .c-product-placement picture img,
.infinite .m-product-placement-item picture,
.infinite .m-product-placement-item picture .c-image,
.infinite .m-product-placement-item picture img {
    display: block !important;
}

.infinite.boxShots-gallery {
    padding: 84px 0;
    text-align: center;
}

.infinite .gameDiv {
    text-align: left;
}

.infinite .m-product-placement-item {
    margin-top: 0px !important;
    padding-top: 14px;
}

.gameDivsWrapper {
    overflow: hidden;
}




.legal {
    background-color: #000;
    padding: 42px 0;
    color: #fff;
}

.legal img {
    padding-bottom: 25px;
    max-width: 10%;
}

.legal p {
    margin-bottom: 10px;
    line-height: 1.5;
}

.legal a {
    color: #fff;
    text-decoration: underline;
}

.legal a:hover {
    color: #9bf00b;
}

@media screen and (max-width: 1084px) {
    .legal {
        padding: 20px;
    }
}

.legal a.c-hyperlink:not(.f-image):focus,
.legal a.c-hyperlink:not(.f-image):hover {
    color: #9bf00b;
}

.magenta {
    background-color: #ff00ff;
}




.c-carousel.f-multi-slide.theme-light .c-flipper {
    background: #000;
    color: #fff;
}

.c-hero .c-subheading,
.m-hero-item .c-subheading,
.m-hero-item .c-heading,
.c-hero .c-heading {
    max-height: 100%;
}

@media only screen and (max-width:767px) {
    .c-hero>div,
    .m-hero-item>div {
        height: 400px;
        overflow: visible
    }
}

.c-hero.f-transparent:before,
.m-hero-item.f-transparent:before {
    padding-bottom: 60.2% !important;
    padding-top: 0px;
}

.c-hero>picture,
.m-hero-item>picture {
    -ms-transform: none !important;
    transform: none !important;
}

@media only screen and (min-width:768px) {
    .nineTeenTwenty.m-image {
        padding-top: 0px;
    }
}




.h-divider {
    border-right: 1px solid rgba(0, 0, 0, .2)
}




.m-global-promotion {
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    overflow: hidden;
    padding: 12px;
    text-align: center;
    min-height: 120px;
}

.m-global-promotion>.c-image img {
    margin: 0 auto;
    height: 100%;
    width: auto;
    max-width: none;
}

.m-global-promotion .c-call-to-action {
    background: transparent;
    color: #0078D7;
    border-color: transparent;
    border-width: 2px;
    padding: 10px 44px 7px 24px;
    margin-left: 0px;
    margin-right: 0px;
}

.m-global-promotion .c-call-to-action:focus,
.m-global-promotion .c-call-to-action:hover {
    background: transparent;
    border-color: transparent;
}

.m-global-promotion .c-call-to-action:active {
    background: transparent;
    text-decoration: none;
}

.theme-light .m-global-promotion .c-call-to-action,
.theme-dark .theme-light .m-global-promotion .c-call-to-action {
    color: #000;
    background: transparent;
    border-color: transparent;
}

.theme-light .m-global-promotion .c-call-to-action:active,
.theme-dark .theme-light .m-global-promotion .c-call-to-action:active {
    color: rgba(0, 0, 0, 0.6);
}

.theme-light .m-global-promotion .c-call-to-action:focus,
.theme-dark .theme-light .m-global-promotion .c-call-to-action:focus {
    outline-color: #000;
}

.theme-dark .m-global-promotion .c-call-to-action,
.theme-light .theme-dark .m-global-promotion .c-call-to-action {
    color: #FFF;
    background: transparent;
    border-color: transparent;
}

.theme-dark .m-global-promotion .c-call-to-action:active,
.theme-light .theme-dark .m-global-promotion .c-call-to-action:active {
    color: rgba(255, 255, 255, 0.6);
}

.theme-dark .m-global-promotion .c-call-to-action:focus,
.theme-light .theme-dark .m-global-promotion .c-call-to-action:focus {
    outline-color: #FFF;
}

.m-global-promotion>div {
    padding-left: 12px;
    padding-right: 12px;
    width: 100%;
}

@media only screen and (min-width: 540px) {
    .m-global-promotion>div {
        padding-left: 24px;
        padding-right: 24px;
    }
}

@media only screen and (min-width: 768px) {
    .m-global-promotion>div {
        padding-left: 0;
        padding-right: 0;
    }
}

.m-global-promotion>div>div .c-heading {
    font-size: 20px;
    line-height: 24px;
    padding: 35px 0 5px;
    font-weight: 200;
    padding-top: 8px;
}

.m-global-promotion>div>div .c-paragraph {
    font-size: 15px;
    line-height: 20px;
    padding: 24px 0 0;
    font-weight: 400;
    padding-top: 8px;
}

@media only screen and (min-width: 768px) {
    .m-global-promotion>div>div {
        max-width: 70%;
        margin: 0 auto;
    }
}

@media only screen and (min-width: 1084px) {
    .m-global-promotion>div>div {
        max-width: 50%;
    }
}

.m-global-promotion>div>.c-group {
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
}

@media only screen and (min-width: 540px) {
    .m-global-promotion>div>.c-group {
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row;
        -webkit-justify-content: center;
        -ms-flex-pack: center;
        justify-content: center;
    }
    .m-global-promotion>div>.c-group .c-call-to-action {
        margin: 0;
    }
}

@media only screen and (min-width: 768px) {
    .m-global-promotion.f-image {
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row;
        text-align: left;
        padding: 0;
    }
    .m-global-promotion.f-image>div {
        display: -webkit-flex;
        display: -ms-flexbox;
        display: flex;
        -webkit-flex-direction: row;
        -ms-flex-direction: row;
        flex-direction: row;
        -webkit-justify-content: space-between;
        -ms-flex-pack: justify;
        justify-content: space-between;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        min-width: calc(100% - 320px);
        padding: 12px 35px 12px 12px;
        width: auto;
    }
    .m-global-promotion.f-image>div>div {
        margin: 0;
    }
}

@media only screen and (min-width: 768px) and (min-width: 768px) {
    .m-global-promotion.f-image>div>div {
        max-width: none;
    }
    .m-global-promotion.f-image>div>div .c-heading {
        padding-top: 0;
    }
}

@media only screen and (min-width: 768px) and (min-width: 1084px) {
    .m-global-promotion.f-image>div>div {
        max-width: none;
    }
}

@media only screen and (min-width: 768px) {
    .m-global-promotion.f-image>div>div+div {
        text-align: right;
        min-width: 250px;
    }
}

@media only screen and (min-width: 768px) and (min-width: 1084px) {
    .m-global-promotion.f-image>div {
        min-width: calc(100% - 440px);
    }
}

@media only screen and (max-width: 539px) {
    .m-global-promotion>div {
        padding-bottom: 22px;
    }
    .m-global-promotion .c-call-to-action {
        margin-left: 0px;
        margin-right: 0px;
    }
}

@media only screen and (min-width: 767px) {
    .hero-preorder-banner.ie10 .text-container {
        width: 60%;
        display: table;
    }
    .hero-preorder-banner.ie10 .header-container {
        width: 80%;
        display: table-cell;
        vertical-align: middle;
    }
    .hero-preorder-banner.ie10 .cta-container {
        width: 20%;
        display: table-cell;
        vertical-align: middle;
    }
}

.promos .theme-dark {
    background: none;
}

.c-carousel li.f-animate-next picture img,
.c-carousel li.f-animate-next picture img,
.c-carousel li.f-animate-next .text-container {
    -webkit-animation: hero-content-next 0.667s cubic-bezier(0.16, 1, 0.29, 0.99) both;
    animation: hero-content-next 0.667s cubic-bezier(0.16, 1, 0.29, 0.99) both;
}

.c-carousel li.f-animate-previous .text-container,
.c-carousel li.f-animate-previous picture img {
    -webkit-animation: hero-content-previous cubic-bezier(0.16, 1, 0.29, 0.99) 0.667s both;
    animation: hero-content-previous cubic-bezier(0.16, 1, 0.29, 0.99) 0.667s both;
}

.theme-dark .m-global-promotion a.c-call-to-action:hover,
.theme-dark .m-global-promotion a.c-call-to-action:active,
.theme-dark .m-global-promotion a.c-call-to-action:visited,
.theme-dark .m-global-promotion a.c-call-to-action:focus {
    background: none;
}

.promos {
    overflow: hidden;
}

.promos .c-carousel .c-sequence-indicator {
    bottom: 10px;
}

.promos .c-group {
    position: static;
}




.svg-container svg {
    width: 23px;
    height: 23px;
    fill: #fff;
    vertical-align: sub;
    margin-bottom: -4px;
    padding-left: 5px;
}

svg:not(:root) {
    overflow: hidden;
}

.hide {
    display: none !important;
}







.m-hero-item h1.c-heading {
    max-height: 212px;
}




[data-grid*="col-12"].three-across {
    padding: 24px 15%;
}

@media screen and (min-width: 1084px) {
    .xbox-live-table p.c-paragraph-1 {
        width: 80%;
        margin-top: 29px;
    }
}

@media (min-width: 1489px) {
    [data-grid*="col-12"].three-across .three-across-item {
        height: 36vw;
    }
}

@media (min-width: 1080px) and (max-width: 1488px) {
    [data-grid*="col-12"].three-across .three-across-item {
        height: 46vw;
    }
}

@media (min-width: 768px) and (max-width: 1079px) {
    [data-grid*="col-12"].three-across {
        padding: 24px 6%;
    }
    [data-grid*="col-12"].three-across .three-across-item {
        height: 66vw;
    }
}




.gameDivsWrapper.gameList-6-2 {
    width: 922px;
    padding: 24px 6px;
}

@media (min-width: 640px) and (max-width: 941px) {
    .gameDivsWrapper.gameList-6-2 {
        width: 618px;
    }
}

@media (max-width: 639px) {
    .gameDivsWrapper.gameList-6-2 {
        width: 302px;
        padding: 0px 0px;
    }
}

.gameList-6-2 .m-product-placement-item {
    margin-right: 12px !important;
    margin-left: 12px !important;
    width: 124px !important;
}




.xbox-live-table {
    padding: 0 2% 4vw;
}

.xbox-live-table.c-table td {
    padding: 20px 12px;
}

.xbox-live-table h3.c-heading-3,
.xbox-live-table h4.c-heading-4 {
    padding: 0;
}

@media (min-width: 1080px) {
    .xbox-live-table p.c-paragraph-1 {
        width: 80%;
    }
}

@media (max-width: 508px) {
    .xbox-live-table h4.c-heading-4 {
        font-size: 14px;
    }
    .xbox-live-table p.c-paragraph-1 {
        font-size: 12px;
    }
    .xbox-live-table td.f-numerical.f-sub-categorical {
        width: 26%;
    }
    .xbox-live-table img {
        width: 100%;
    }
}







.consoleList .consoleItem {
    float: none !important;
    display: inline-block;
    margin-bottom: 24px;
    vertical-align: top;
}

.itemCat .item {
    display: inline-block;
    float: none;
    vertical-align: top;
    margin-top: 24px;
}

.itemCat.catHidden {
    display: none;
}

.hiLo.priceSelected,
.loHi.priceSelected {
    text-decoration: underline;
}

.c-feature a:focus picture {
    outline: 1px dashed !important;
}

.c-dialog.f-lightbox>[role=presentation]+.c-glyph,
.c-dialog.f-lightbox:hover>[role=presentation]+.c-glyph {
    color: #9bf00b;
    z-index: 1001;
}







.c-mosaic-placement>div {
    justify-content: flex-end;
    padding-bottom: 50px;
}

.c-mosaic-placement .firstItem {
    justify-content: center;
}

.c-mosaic-placement .c-subheading {
    padding-top: 5px !important;
}




.mosaic-container {
    margin: 0 auto;
}

.mosaic-container a:focus img {
    outline: dashed !important;
}

.m-scale-mosaic {
    padding-left: 0px;
    padding-right: 0px;
}

.m-scale-mosaic .square div img {
    width: 100%;
}

.m-scale-mosaic .rect img {
    width: 100%;
}

.m-scale-mosaic .c-group span {
    color: #fff;
    font-size: 18px;
    font-weight: 700;
}

.m-scale-mosaic .c-group {
    position: relative;
    display: block;
    max-height: 60px;
}

.m-scale-mosaic .c-group.first span {
    color: #fff;
    font-size: 44px;
    font-weight: 100;
}

@media screen and (min-width: 0px) {
    .mosaic-container .dsk {
        display: none;
    }
    .mosaic-container .mob {
        display: block;
    }
    .mosaic-container {
        width: 100%;
    }
    .m-scale-mosaic .square div,
    .m-scale-mosaic .rect {
        width: 320px;
        text-align: center;
    }
    .m-scale-mosaic .btmTouts .square {
        position: relative;
        top: -150px;
    }
    .m-scale-mosaic .btmTouts .rect {
        position: relative;
        bottom: -640px;
        height: 150px;
    }
    .m-scale-mosaic .square div {
        height: 320px;
    }
    .m-scale-mosaic .tpTouts,
    .m-scale-mosaic .btmTouts {
        height: 960px;
    }
    .m-scale-mosaic .c-group {
        padding: 0 10px;
        bottom: 75px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 200px;
    }
}

@media screen and (min-width: 320px) {
    .mosaic-container {
        width: 320px;
    }
}

@media screen and (min-width: 540px) {
    .mosaic-container .dsk {
        display: block;
    }
    .mosaic-container .mob {
        display: none;
    }
    .mosaic-container {
        width: 496px;
    }
    .m-scale-mosaic .square div {
        display: inline-block;
        float: left;
        width: 248px;
    }
    .m-scale-mosaic .rect {
        width: 496px;
    }
    .m-scale-mosaic .btmTouts .square {
        top: -248px;
    }
    .m-scale-mosaic .btmTouts .rect {
        bottom: -248px;
        height: 248px;
    }
    .m-scale-mosaic .square div {
        height: 248px;
    }
    .m-scale-mosaic .tpTouts {
        height: 496px;
    }
    .m-scale-mosaic .btmTouts {
        height: auto;
    }
    .m-scale-mosaic .c-group {
        bottom: 80px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 180px;
    }
}

@media screen and (min-width: 768px) {
    .mosaic-container {
        width: 688px;
    }
    .m-scale-mosaic .square div {
        display: inline-block;
        float: left;
        width: 344px;
    }
    .m-scale-mosaic .rect {
        width: 688px;
    }
    .m-scale-mosaic .btmTouts .square {
        top: -344px;
    }
    .m-scale-mosaic .btmTouts .rect {
        bottom: -344px;
        height: 344px;
    }
    .m-scale-mosaic .square div {
        height: 344px;
    }
    .m-scale-mosaic .tpTouts {
        height: 688px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 230px;
    }
}

@media screen and (min-width: 1084px) {
    .mosaic-container {
        width: 960px;
    }
    .m-scale-mosaic .square div {
        display: inline-block;
        float: left;
        width: 240px;
        height: 240px;
    }
    .m-scale-mosaic .tpTouts {
        height: 240px;
    }
    .m-scale-mosaic .tpTouts .rect {
        display: inline-block;
        width: 480px;
    }
    .m-scale-mosaic .btmTouts .square {
        top: 0px;
    }
    .m-scale-mosaic .btmTouts .rect {
        display: inline-block;
        float: left;
        width: 480px;
    }
    .m-scale-mosaic .c-group span {
        font-size: 14px;
    }
    .m-scale-mosaic .btmTouts .rect {
        bottom: 0px;
        height: 240px;
    }
    .m-scale-mosaic .c-group {
        bottom: 80px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 170px;
    }
}

@media screen and (min-width: 1400px) {
    .mosaic-container {
        width: 1260px;
    }
    .m-scale-mosaic .tpTouts {
        height: 315px;
    }
    .m-scale-mosaic .square div {
        width: 315px;
        height: 315px;
    }
    .m-scale-mosaic .btmTouts .rect,
    .m-scale-mosaic .tpTouts .rect {
        width: 630px;
    }
    .m-scale-mosaic .c-group span {
        font-size: 18px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 200px;
    }
}

@media screen and (min-width: 1600px) {
    .mosaic-container {
        width: 1420px;
    }
    .m-scale-mosaic .tpTouts {
        height: 355px;
    }
    .m-scale-mosaic .square div {
        width: 355px;
        height: 355px;
    }
    .m-scale-mosaic .btmTouts .rect,
    .m-scale-mosaic .tpTouts .rect {
        width: 710px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 230px;
    }
}

@media screen and (min-width: 1800px) {
    .mosaic-container {
        width: 1600px;
    }
    .m-scale-mosaic .tpTouts {
        height: 400px;
    }
    .m-scale-mosaic .square div {
        width: 400px;
        height: 400px;
    }
    .m-scale-mosaic .btmTouts .rect,
    .m-scale-mosaic .tpTouts .rect {
        width: 800px;
    }
    .m-scale-mosaic .c-group.first {
        bottom: 230px;
    }
}




@media only screen and (max-width: 1084px) {
    .faq-mwf {
        padding-left: 36px !important;
        padding-right: 36px !important;
    }
}

.faq-mwf .c-drawer button:focus {
    outline: 2px dashed #fff;
    border: 2px dashed #000;
}

.faq-mwf hr.c-divider.f-pad-top-3x {
    margin-top: 36px;
}

.faq-mwf hr {
    margin-top: 0;
    margin-bottom: 0;
    background-color: transparent;
}

.faq-mwf button p,
.faq-mwf button h3,
.faq-mwf button h4 {
    padding: 10px 0;
    color: #107c10;
}

.faq-mwf .c-paragraph-2 {
    padding: 32px;
}

.faq-mwf .m-banner {
    max-width: 1600px;
    padding: 8px 0;
    text-align: right;
}




.faq-mwf .c-drawer {
    background-color: #fbfbfb;
}

.faq-mwf .c-drawer>button {
    background-color: #f4f4f4;
}

.faq-mwf .c-drawer>button>p,
.faq-mwf .c-drawer>button>h3,
.faq-mwf .c-drawer>button>h4 {
    font-size: 16px;
    color: #0a4f0a;
}

.faq-mwf a.c-hyperlink {
    color: #0a4f0a;
}


.theme-dark .faq-mwf {
    background-color: #171717 !important;
    color: white;
    padding-bottom: 48px;
}

.theme-dark .faq-mwf hr.c-divider {
    border-bottom: 1px solid rgba(255, 255, 255, .2);
}

.theme-dark .faq-mwf .c-drawer {
    background: transparent;
    border-bottom: 1px solid rgba(255, 255, 255, .2);
}

.theme-dark .faq-mwf button.c-glyph {
    color: white;
    background-color: #171717 !important;
}

.theme-dark .faq-mwf button.c-glyph:hover,
.theme-dark .faq-mwf button.c-glyph:focus,
.theme-dark .faq-mwf button.c-glyph:active {
    color: white !important;
}

.theme-dark .faq-mwf p {
    color: white !important;
}




.priceFrom {
    margin: 12px 20px 0 0;
    float: none;
    font-weight: 700;
}




.eaAccess {
    padding: 10px 0;
}

.eaAccess img {
    max-width: 100%;
}

.eaAccess p {
    padding: 38px 0px 2px 20px;
}

@media screen and (max-width: 539px) {
    .eaAccess img {
        padding-left: 25vw;
    }
}

@media screen and (min-width: 540px) {
    .eaAccess .tall {
        height: 225px;
        line-height: 225px;
    }
    .eaAccess .short {
        height: 150px;
        line-height: 150px;
    }
}

@media screen and (min-width: 768px) {
    .eaAccess .tall {
        height: 205px;
        line-height: 205px;
    }
    .eaAccess .short {
        height: 150px;
        line-height: 150px;
    }
}

@media screen and (min-width: 1084px) {
    .eaAccess .tall {
        height: 200px;
        line-height: 200px;
    }
    .eaAccess .short {
        height: 150px;
        line-height: 150px;
    }
}

@media screen and (min-width: 1400px) {
    .eaAccess .tall {
        height: 150px;
        line-height: 150px;
    }
    .eaAccess .short {
        height: 100px;
        line-height: 100px;
    }
}







.win10games .gameDivCTA {
    text-align: center;
}

.win10games .gameDivsWrapper {
    text-align: center;
    width: 100%;
}

.win10games .gameDivsWrapper .gameDiv {
    text-align: left;
    display: inline-block;
    margin: 24px 10px 16px;
    vertical-align: top;
    min-width: 220px;
    max-width: 497px;
    width: 30% !important;
}

.win10games .m-heading-4+[class*=m-] {
    padding-top: 0;
}

.win10games .containerIMG {
    position: relative;
}

.win10games .containerIMG .c-image {
    width: 100%;
    max-width: 497px;
}




.cookieBannerWrapper {
    background-color: #646464;
    display: none;
    height: 26px;
    min-width: 960px;
}

.cookieBanner {
    width: 960px;
    margin: 0 auto;
    position: relative;
}

.cookieBanner .learnMore {
    height: 26px;
    float: right;
}

.cookieBanner .alertDescription {
    float: left;
    color: #fff;
    text-align: left;
    font: 12px/26px "Segoe UI", Arial, Sans-Serif;
    max-width: 810px;
}

.cookieBanner .learnMore a,
.cookieBanner .learnMore a:visited {
    display: block;
    float: left;
    color: #fff;
    font: 12px/26px "Segoe UI Semibold", Arial, Sans-Serif;
}

.cookieBanner .learnMore img {
    margin-top: 5px;
    margin-left: 20px;
    cursor: pointer;
}

.price-spider {
    max-width: 400px;
}




.newXGPshared .spLogo {
    width: 345px;
    height: 48px;
}

@media screen and (min-width: 768px) {
    .newXGPshared .m-hero-item h2 {
        padding-top: 24px;
    }
}

.newFavoriteGame .m-hero-item h2 {
    padding-top: 24px;
}

@media only screen and (max-width: 767px) {
    .tallMob .spLogo {
        width: 172px;
        height: 24px;
    }
    .tallMob .m-hero-item>div {
        height: 89vw;
    }
    .tallMob [class*=f-x][class*=f-y].m-hero-item>div>div {
        top: calc(45%);
    }
    .tallMob .m-hero-item>div picture {
        display: block;
        padding-bottom: 24px;
    }
    .tallMob .m-hero-item>div picture+h2.c-heading-2 {
        padding-top: 0;
    }
}

.dark-gray-bg {
    background-color: #171717;
}

.appStoreBadges {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
}




.xboxSocial span {
    color: black;
}

.xboxSocial ul {
    margin-bottom: 4px;
}

@media screen and (max-width: 1083px) {
    .sharedIcons .twoIcons {
        float: none !important;
        display: inline-block !important;
    }
    .sharedIcons .emptyColumns {
        display: none !important;
    }
}

.sharedIcons .m-content-placement-item>picture {
    padding-bottom: 0 !important;
}

.sharedIcons .m-content-placement-item>picture img {
    position: relative !important;
}




@media (min-width: 768px) and (max-width: 1400px) {
    .legal img {
        padding-bottom: 60px;
    }
}

@media only screen and (max-width:767px) {
    .legal img {
        max-width: 25%;
        padding-bottom: 10px;
    }
}




@media screen and (min-width: 1500px) {
    .newXGPshared .m-hero-item.f-x-center>div>div {
        min-width: 60%;
    }
}




@media screen and (min-width: 767px) and (max-width: 900px) {
    .xpgHeroPC .m-hero-item.f-x-center>div>div {
        min-width: 60% !important;
    }
}

@media screen and (min-width: 767px) and (max-width: 1084px) {
    .xpgHeroPC .svgLogo {
        height: 40px;
    }
}

.xpgHeroPC .svgLogo {
    width: 345px;
    height: 48px;
}




.xgpTouchControl .svgLogo {
    max-width: 279px;
}

@media screen and (max-width: 340px) {
    .xgpTouchControl p.c-subheading:has(~div .appStoreBadges) {
        font-size: 16px;
        line-height: 22px;
    }
}




@media screen and (max-width: 767px) {
    .heroCrossSell .m-hero-item>div {
        height: 250px !important;
    }
    .heroCrossSell [class*=f-x][class*=f-y].m-hero-item>div>div {
        top: calc(43%) !important;
    }
}

@media screen and (min-width: 1084px) {
    .heroCrossSell .m-hero-item {
        max-height: 600px;
        height: 30.7vw;
    }
}

.heroCrossSell a.c-call-to-action {
    color: #9bf00b !important;
}

@media only screen and (max-width:1921px) {
    .heroCrossSell {
        background-color: #171717;
    }
}







@media screen and (min-width: 1084px) {
    .familyCrossSell .m-hero-item {
        max-height: 600px !important;
        height: 30.7vw !important;
    }
}

@media only screen and (max-width: 767px) {
    .familyCrossSell .m-hero-item>div {
        height: 200px !important;
    }
    .familyCrossSell [class*=f-x][class*=f-y].m-hero-item>div>div {
        top: calc(35%) !important;
    }
    .familyCrossSell .m-hero-item .c-subheading,
    .familyCrossSell .m-hero-item>div picture,
    .familyCrossSell .m-hero-item[class*=f-x][class*=f-y]>picture:after {
        display: block !important;
    }
    .familyCrossSell .m-hero-item>div>div picture img {
        max-width: 255px;
    }
    .familyCrossSell .c-heading-3 {
        padding-top: 10px !important;
    }
}







.m-page-bar {
    max-width: 100%;
}

@media screen and (max-width: 767px) {
    .m-page-bar span {
        font-size: 10px !important;
    }
}




@media screen and (max-width: 540px) {
    .tg-svgHeroLogos {
        width: 100%;
    }
}

.tg-svgHeroLogos {
    height: 34px !important;
}

.tg-svgPurchaseLogos {
    height: 23px !important;
}

.tg-svgXPALogo {
    height: 60px !important;
}

.tg-svgEAAccessLogo {
    height: 57px !important;
}

.winPC .spLogo {
    height: 5vw;
    width: 5vw;
}







@-moz-document url-prefix() {
    .high-contrast-mode .high-contrast {
        background-color: #000;
        color: #fff !important;
    }
}

@media screen and (-ms-high-contrast: active), screen and (-ms-hight-contrast:white-on-black), 
screen and (forced-colors: active) and (prefers-color-scheme: dark) {
    .faq-mwf button:not(.c-select-button):not(.c-sequence-indicator):hover:not(:disabled),
    .faq-mwf button:not(.c-select-button):not(.c-sequence-indicator):focus:not(:disabled),
    .faq-mwf button:not(.c-select-button):not(.c-sequence-indicator):active:not(:disabled) {
        color: #000 !important;
        background-color: transparent !important;
        -ms-high-contrast-adjust: auto !important;
    }
}

@media screen and (-ms-high-contrast:white-on-black), 
screen and (forced-colors: active) and (prefers-color-scheme: dark) {
    .high-contrast {
        background-color: #000;
        color: #fff !important;
    }
    .high-contrast-svg-white {
        background-color: #fff;
    }
    .faq-mwf p {
        color: #fff;
    }
}

@media screen and (-ms-high-contrast:black-on-white), 
screen and (forced-colors: active) and (prefers-color-scheme: light) {
    .high-contrast {
        background-color: #fff;
        color: #000 !important;
    }
    .high-contrast-svg-black {
        background-color: #000;
    }
}










.m-product-placement-item.context-video picture,
.m-product-placement-item.context-video img,
.c-product-placement.context-video picture,
.c-product-placement.context-video img {
    width: 330px !important;
}

.m-product-placement-item.f-size-large.context-video picture,
.c-product-placement.f-size-large.context-video picture {
    width: 330px !important;
}

.m-product-placement-item.f-size-large.context-video,
.c-product-placement.f-size-large.context-video {
    width: 336px !important;
    margin-right: 12px !important;
}

.m-product-placement-item.context-video .c-action-trigger,
.c-product-placement.context-video .c-action-trigger {
    top: calc(94.5px - 24px) !important;
    left: calc(168px - 24px) !important;
}




.m-product-placement-item.f-size-large.context-video img:hover {
    opacity: .7 !important;
}

.media-gallery-black {
    background-color: #000 !important;
}




.media-gallery-black .c-flipper.x-hidden-focus {
    background-color: #ccc;
}

.c-video-player .f-core-player video,
.c-video-player .f-core-player object {
    background-color: none !important;
}

@media screen and (min-width: 0px) {
    .oneFrame {
        width: 91%;
        height: 49.5vw;
        margin: 0 auto;
    }
    .oneFrame iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
}

@media screen and (min-width: 540px) {
    .oneFrame {
        height: 49.5vw;
        width: 90%;
    }
}

@media screen and (min-width: 768px) {
    .oneFrame {
        width: 63.9vw;
        height: 36vw;
    }
}

.BGtransplay button.c-action-trigger.x-hidden-focus {
    background: rgba(0, 0, 0, .6) !important;
}

.m-media-gallery {
    padding-top: 52px;
}







.m-product-placement-item.f-size-medium.gameDiv a picture {
    width: auto !important;
    height: 100% !important;
}

.m-product-placement-item.f-size-medium.gameDiv a picture img {
    position: static;
    transform: none;
}

.m-product-placement-item.gameDiv>a {
    position: static;
    border: 0 !important;
    outline: 0;
    display: block;
    overflow: visible;
    padding: 0 !important;
    width: 100%;
    height: 100%;
    white-space: normal;
}

.m-product-placement-item.gameDiv>a:focus {
    outline: 2px dashed #000;
}

.m-product-placement-item.gameDiv>a>picture {
    border: none;
}







.poprotator div.c-group {
    bottom: 80px !important;
}

.m-product-placement-item.f-size-medium .poprotator picture {
    width: 100% !important;
    height: 100% !important;
    position: absolute !important;
}

.m-product-placement-item.f-size-medium .gameMoreInfo .c-carousel.carfullimage picture {
    width: 58% !important;
    margin-left: 20.9%;
    margin-top: -2%;
}

.gameDiv .ratingstars,
.popinfo .ratingstars,
.popinfo .reviewtotal {
    display: none;
}

.gameMoreInfo {
    height: 76%;
    max-height: 685px;
    overflow-y: auto;
}







@media screen and (max-width: 1499px) {
    .gameList .popupShow .poprotator,
    .gameList .popupShow .poprotator .m-hero-item {
        height: auto !important;
    }
}

.gameList .popupShow .c-carousel>div:last-of-type {
    position: relative;
}

.gameList .popupShow .c-carousel>div:last-of-type:before {
    content: '';
    display: block;
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 56%; 
    top: 0;
    z-index: -2;
}

.gameList .popupShow .c-carousel>div:last-of-type>ul {
    position: absolute;
    top: 0;
    height: auto;
    width: 100%;
}

.gameList .popupShow .c-carousel .m-hero-item:before {
    padding-bottom: 56% !important; 
}


.gameList .gameMoreInfo.popupShow {
    overflow: auto;
}

.gameList .popupShow .c-carousel .popinfo .popprice {
    margin-right: 0px;
}





html[dir="ltr"] .c-search button {
    left: auto;
}



.c-refine-menu .c-drawer>button {
    font-size: 15px !important;
}




.x1Help .m-banner {
    padding-bottom: 48px !important;
}

.xboxSocial .m-social {
    margin: 18px 0;
}

.m-social>a:focus,
.m-social>ul>li>a:focus,
.c-social>a:focus,
.c-social>ul>li>a:focus {
    border: 2px dashed #000;
    outline: 2px dashed #fff;
}

@media screen and (max-width: 1083px) {
    .xboxSocial .m-social {
        margin: 18px 20px;
        flex-wrap: wrap;
    }
}







.buybox {
    position: relative;
    margin-top: 20px;
    
}

.buybox__main {
    border: 6px solid #000;
    padding: 5.25% 1.25% 5% 1.25%;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.buybox__glyph img {
    max-width: 40px;
}

.buybox__main img {
    max-width: 100%;
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 254px;
}

.buybox__content {
    position: relative;
    width: 22.5%;
    text-align: center;
    justify-content: center;
    padding-bottom: 16px;
}

.buybox.three-up .buybox__content {
    width: 30%;
}

.buybox__glyph {
    position: relative;
    width: 3.5%;
    text-align: center;
}

.buybox.three-up .buybox__glyph {
    width: 4.66%;
}

@media screen and (min-width: 540px) {
    .buybox .buybox__content [class^=c-heading] {
        font-size: 26px;
        line-height: 1.15em;
    }
}

@media screen and (min-width: 1084px) {
    .buybox .buybox__content [class^=c-heading] {
        font-size: 34px;
        line-height: 1.15em;
    }
}

.buybox .buybox__content [class^=c-heading] strong {
    font-weight: 600 !important;
}

@media screen and (max-width: 1083px) {
    .buybox {
        padding-left: 5%;
        padding-right: 5%;
    }
}

@media screen and (max-width: 767px) {
    .buybox__main {
        flex-wrap: wrap;
        padding-top: 60px;
        padding-bottom: 50px;
    }
    .buybox.three-up .buybox__content,
    .buybox__content {
        width: 45.5%;
    }
    .buybox__glyph {
        position: relative;
        width: 7%;
        text-align: center;
    }
    .buybox.three-up .buybox__glyph,
    .buybox__glyph.stack {
        display: none;
    }
}

@media screen and (max-width: 539px) {
    .buybox__content {
        width: 50%;
    }
    .buybox__glyph {
        display: none;
    }
}







.c-glyph.glyph-pause:before {
    content: "" / "" !important;
}

.c-glyph.glyph-play:before {
    content: "" / "" !important;
}

.c-select-menu>button:after {
    content: "" / "" !important;
}

.m-ambient-video {
    position: relative;
}

.m-ambient-video div button:focus {
    outline: 2px dashed #000 !important;
    border: 2px dashed #fff !important;
}

@media screen and (-ms-high-contrast: active), screen and (forced-colors: active) {
    .m-ambient-video div button:focus {
        outline: 2px dashed #000 !important;
        border: 2px dashed #fff !important;
    }
}

@media screen and (-ms-high-contrast:white-on-black), 
screen and (forced-colors: active) and (prefers-color-scheme: dark) {
    .m-ambient-video.pp-button > div button {
        background-color: black;
    }
    
}
.high-contrast-mode.white-on-black  .m-ambient-video.pp-button > div button.vidPlayPause {
    background-color: black;
}


@media screen and (-ms-high-contrast:black-on-white), 
screen and (forced-colors: active) and (prefers-color-scheme: light) {
    .m-ambient-video.pp-button > div button.vidPlayPause {
        background-color: white;
    }
}
.high-contrast-mode.black-on-white .m-ambient-video.pp-button > div button.vidPlayPause  {
    background-color: white;
}


.m-ambient-video div button {
    height: 36px !important;
    width: 36px;
    position: absolute;
    color: white;
    background-color: rgba(0, 0, 0, 0.60);
    border: 1px solid white !important;
    bottom: 24px;
    display: block;
    padding: 2px 0px 0px 0px;
    margin-left: 24px;
}







.mod-feature .m-multi-feature img.c-image {
    max-width: 200px;
}

.mod-feature .m-multi-feature [role='tablist'] li {
    background: #000;
}

.mod-feature .m-multi-feature [role='tablist'] li>a {
    display: block;
    opacity: .6;
}

.mod-feature .m-multi-feature [role='tablist'] li>a.f-active {
    outline: 2px solid #9bf00b !important;
    border: none !important;
    opacity: 1;
}

@media screen and (min-width: 1018px) {
    .mod-feature .copyList {
        width: 1000px;
    }
}

@media only screen and (min-width:1084px) {
    .m-multi-feature [role='tabpanel']>.c-heading,
    .m-multi-feature [role='tabpanel']>div>.c-heading {
        font-size: 34px;
        line-height: 40px;
        padding: 38px 0 2px;
        font-weight: 600;
        padding-top: 24px;
    }
}

@media screen and (max-width: 1017px) {
    .mod-feature .copyList {
        max-width: 1000px;
    }
}

@media screen and (min-width: 768px) {
    .mod-feature .m-multi-feature.f-align-center>section>[role='tablist'],
    .mod-feature .m-multi-feature.f-align-center>section>.c-pivot {
        margin-top: -50px;
        z-index: 100;
    }
}

.mod-feature .m-multi-feature section ul li>a {
    overflow: hidden;
}

@media screen and (max-width: 900px) {
    .mod-feature .availability div p span.available-text {
        display: none;
    }
}

@media screen and (max-width: 475px) {
    .mod-feature .availability div {
        display: none;
    }
}

@media screen and (max-width: 767px) {
    .mod-feature .availability div p span.available-text {
        display: none;
    }
}

.mod-feature .availability {
    position: absolute;
    bottom: 0;
    left: 0;
    
}

.mod-feature .availability>div {
    bottom: 0;
    right: 0;
    background-color: #fff;
    display: inline-block;
    transform: translateX(-15px) skewX(32deg);
}

.mod-feature .availability p {
    height: 32px;
    line-height: 30px;
    padding: 0 16px 0 22px;
    color: #000;
    display: inline-block;
    text-align: top;
    transform: skewX(-32deg);
}

.mod-feature .availability p span.c-glyph {
    font-family: "MWF-MDL2";
    display: inline-block;
    font-weight: 400;
    font-size: 1.2em;
    vertical-align: middle;
    margin-left: 5px;
}




.characterRotate div .c-pivot li[aria-posinset='1'] {
    padding-left: 0 !important;
}

.characterRotate div .c-carousel {
    background-color: transparent !important;
}

.characterRotate div .c-pivot:not(.f-disabled)>ul li.f-active:after {
    border-bottom: 2px solid #9bf00b !important;
    bottom: 1px !important;
}

.characterRotate div .c-pivot:not(.f-disabled)>ul li[aria-posinset='1']:after {
    left: -1px !important;
}

.characterRotate .c-pivot:not(.f-disabled)>[role=tablist] li.c-subheading:not(.f-active) {
    color: #FFF !important;
}

.characterRotate .c-pivot:not(.f-disabled)>[role=tablist] li.c-subheading {
    font-size: 18px;
    line-height: 24px;
    font-weight: 700;
    border: none;
}

.characterRotate div .c-pivot li.c-subheading.f-active {
    color: #9bf00b !important;
}

.characterRotate div .m-multi-feature {
    padding-top: 0px;
}

.characterRotate div .m-multi-feature [role=tablist] + [role=tabpanel] .c-heading {
    padding-top: 24px !important;
}

@media screen and (min-width: 1084px) and (max-width: 1399px) {
.characterRotate div .c-pivot .c-heading-2 {
    font-size: 34px;
    line-height: 40px;}  
}

@media screen and (min-width: 1084px) {
.characterRotate div .m-multi-feature.f-align-center > section > section {
    width: 55vw;}
}

@media screen and (min-width: 1400px) {
.characterRotate div .m-multi-feature.f-align-center > section > section {
    width: 45vw;}
}

@media screen and (min-width: 1084px) {
.characterRotate div .m-multi-feature.f-align-center > section > .c-pivot > section {
    width: 100%;
    text-align: left;}

.characterRotate div .m-multi-feature [role='tablist'] {
    justify-content:left !important;}

.characterRotate div .c-pivot h2 {
    margin-left:-5px !important;}

.characterRotate div .c-pivot > ul > li {font-size:20px !important;}
.characterRotate div .m-multi-feature.f-align-center > section > section {
    position: absolute;
    left: 7.1vw;
    z-index: 100;
    padding-top: 30px;}

.characterRotate div .c-pivot h3, .characterRotate div .c-pivot p, .characterRotate div .c-pivot .c-heading-2 {
    text-align: left;}

.characterRotate div .c-pivot h2 {
    width:43vw !important; padding-bottom: 24px;}

.characterRotate div .c-pivot > ul > a {
    font-size: 35px;}
}

@media screen and (max-width: 1084px) {
.characterRotate {
    background-color: #171717 !important;}

.characterRotate div .c-pivot h2 {
    padding-bottom: 38px;}

.characterRotate div .m-multi-feature {
    padding-bottom: 96px;}

.characterRotate div .m-multi-feature {
    background-color: #171717 !important;}
}


@media screen and (max-width: 1250px) and (min-width: 1084px) {
.characterRotate div .c-pivot h3 {
    padding-top: 24px !important;}
}

@media screen and (max-width: 1084px) and (min-width: 768px) {
.characterRotate .m-hero-item > div > div {
    max-width: 440px !important;}
}

.characterRotate li:focus {
    outline: 2px dotted #000 !important;
    border: 2px dotted #FFF !important;
}

.characterRotate .c-pivot:not(.f-disabled)>ul>[role=tab].f-active:focus:not(.x-hidden-focus) {
    background-color: transparent !important;
}

@media screen and (max-width: 539px) {
.characterRotate .m-multi-feature .c-pivot>ul {
    display: flex !important;}
}




.m-hero-item .c-group>.c-call-to-action+.c-call-to-action:focus {
    border: 2px dotted #000 !important;
    outline: 2px dotted #FFF !important;
}

.m-multi-feature ul>li:focus,
.m-multi-feature a.c-call-to-action:focus {
    border: 2px dotted #000 !important;
    outline: 2px dotted #FFF !important;
}

[class^=c-heading-]:after,
[class^=c-heading-]:before {
    content: "" / "";
}

.mod-feature .m-multi-feature .c-pivot>ul li {
    padding: 0px !important;
    margin: 0 10px 0 0 !important;
    border: none;
    outline: none;
    overflow: hidden;
}

.mod-feature .m-multi-feature .c-pivot>ul li {
    background: #000;
}

.mod-feature .c-pivot:not(.f-disabled)>ul>li.f-active:after {
    border-bottom: none !important;
}

.mod-feature .c-pivot:not(.f-disabled)>ul>li.f-active {
    border: 2px solid #000;
    outline: 2px solid #9bf00b !important;
}

.mod-feature .m-multi-feature .c-pivot>ul li img {
    margin: 0px !important;
    opacity: 0.6;
}

.mod-feature .m-multi-feature .c-pivot>ul li.f-active img {
    opacity: 1;
}







.backgroundWhite {
    background-color: #fff !important;
}

@media screen and (min-width:768px) {
    .backgroundWhite {
        color: #fff !Important;
    }
}

@media screen and (max-width:768px) {
    .backgroundWhite a {
        color: #0a4f0a !Important;
    }
}




.paginateprevious.pag-disabled,
.paginatenext.pag-disabled {
    display: none !important;
}




.border-banner .m-banner,
.tune-in .m-banner {
    max-width: 100% !important;
    padding-bottom: 25px;
    padding-left: 5%;
    padding-right: 5%;
    border: 2px solid #107c10;
}

.border-banner .m-banner:has(p),
.tune-in .m-banner:has(p) {
    padding-bottom: 32px;
}


.border-banner.theme-black .m-banner,
.border-banner.theme-dark .m-banner,
.border-banner.theme-dkgray .m-banner,
.tune-in.theme-black .m-banner,
.tune-in.theme-dark .m-banner,
.tune-in.theme-dkgray .m-banner {
    border-color: #9bf00b;
}

@media screen and (max-width: 1084px) {
    .border-banner,
    .tune-in {
        padding-left: 36px;
        padding-right: 36px;
    }
}

.upgradeToUltimate .gamePassLogo,
.newFavoriteGame .gamePassLogo {
    max-width: 278px !important;
}

@media only screen and (max-width:767px) {
    .upgradeToUltimate .gamePassLogo,
    .newFavoriteGame .gamePassLogo {
        margin: 0 auto;
    }
}

@media screen and (min-width:1400px) {
    .newFavoriteGame p {
        width: 600px !important;
    }
}




div.icon-list-hero section.m-hero-item h3.c-subheading-3 {
    font-weight: 700;
}

@media only screen and (min-width: 1400px) {
    
    div.icon-list-hero section.m-hero-item {
        height: 63vw;
    }
}

@media only screen and (min-width: 768px) and (max-width: 1083px) {
    div.icon-list-hero section.m-hero-item {
        height: 80vw;
    }
}




div.icon-list-hero .c-paragraph-4 {
    padding-bottom: 2px;
}

div.icon-list-hero section.m-hero-item div.pwd-copy-section {
    top: 0px;
}

@media only screen and (min-width: 1084px) and (max-width: 1399px) {
    
}

@media only screen and (min-width: 540px) and (max-width: 626px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 5vw;
    }
}

@media only screen and (min-width: 520px) and (max-width: 539px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 167vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 344vw;
    }
}

@media only screen and (min-width: 500px) and (max-width: 519px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 173vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 354vw;
    }
}

@media only screen and (min-width: 480px) and (max-width: 499px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 179vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 368vw;
    }
}

@media only screen and (min-width: 460px) and (max-width: 479px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 183vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 377vw;
    }
}

@media only screen and (min-width: 440px) and (max-width: 459px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 192vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 392vw;
    }
}

@media only screen and (min-width: 420px) and (max-width: 439px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 203vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 412vw;
    }
}

@media only screen and (min-width: 414px) and (max-width: 419px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 206vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 418vw;
    }
}

@media only screen and (min-width: 375px) and (max-width: 413px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 229vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 467vw;
    }
}

@media only screen and (min-width: 340px) and (max-width: 374px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 252vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 515vw;
    }
}

@media only screen and (min-width: 320px) and (max-width: 339px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 266vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 561vw;
    }
}

@media only screen and (max-width: 319px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        top: 276vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 494vw;
    }
}

div.icon-list-hero section.m-hero-item div.pwd-copy-section .icons>div {
    margin-top: 24px;
}

@media only screen and (max-width: 539px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section .icons>div[data-grid*="col-4"] {
        margin-top: 50px;
    }
}

@media only screen and (min-width: 1400px) {
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        max-width: 625px;
    }
    div.icon-list-hero .c-heading-1a {
        padding-bottom: 48px
    }
}

@media only screen and (min-width: 1800px) {
    div.icon-list-hero .m-hero-item>div {
        max-width: 1600px;
    }
}

@media only screen and (min-width: 1600px) and (max-width: 1799px) {
    div.icon-list-hero .m-hero-item>div {
        max-width: 1600px;
        margin-left: 5%;
    }
}

@media only screen and (max-width: 1599px) {
    div.icon-list-hero .m-hero-item>div {
        max-width: calc(1600px + 10%);
        margin-left: 5%;
    }
}

@media only screen and (min-width: 1084px) and (max-width: 1399px) {
    div.icon-list-hero section.m-hero-item>picture {
        height: 109%;
        width: 109%;
        top: -1vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 83vw;
    }
    div.icon-list-hero section.m-hero-item div.pwd-copy-section {
        max-width: 525px;
    }
}

@media only screen and (min-width: 950px) and (max-width: 1083px) {
    div.icon-list-hero section.m-hero-item>picture {
        top: -23vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 103vw;
    }
    div.icon-list-hero section.m-hero-item .pwd-copy-section {
        max-width: 520px;
    }
}

@media only screen and (min-width: 768px) and (max-width: 949px) {
    div.icon-list-hero section.m-hero-item>picture {
        top: -21vw;
    }
    div.icon-list-hero section.m-hero-item {
        height: 105vw;
    }
    div.icon-list-hero section.m-hero-item .pwd-copy-section {
        max-width: 430px;
    }
}

@media only screen and (min-width: 540px) and (max-width: 767px) {
    .icon-list-hero .m-hero-item.f-transparent:before {
        padding-bottom: 124.2% !important;
    }
}

@media only screen and (max-width: 539px) {
    .icon-list-hero [data-grid*="col-1"] {
        margin-top: 0px !important;
    }
}

@media only screen and (min-width: 1921px) {
    div.icon-list-hero section.m-hero-item {
        height: 1210px;
    }
}




.icon-list-svg-1 {
    width: 82px;
    margin-left: auto;
    margin-right: auto;
}

.icon-list-svg-1 img {
    width: 82px;
}

.icon-list-svg-2 {
    width: 119px;
    margin-left: auto;
    margin-right: auto;
}

.icon-list-svg-2 img {
    width: 119px;
}

.icon-list-svg-3 {
    width: 172px;
    margin-left: auto;
    margin-right: auto;
}

.icon-list-svg-3 img {
    width: 172px;
}

@media only screen and (min-width: 768px) and (max-width: 1083px) {
    .icon-list-svg-3 {
        width: 142px;
    }
    .icon-list-svg-3 img {
        width: 142px;
    }
    .m-hero-item .c-group>.c-call-to-action+.c-call-to-action {
        padding: 10px 43px 7px 20px;
    }
}

.icon-list-svg-4 {
    width: 84px;
    margin-left: auto;
    margin-right: auto;
}

.icon-list-svg-4 img {
    width: 84px;
}




.eaPlay .eaPlayLogo {
    max-width: 392px !important;
}

@media screen and (min-width: 1100px) {
    .eaPlay .eaPlayLogo {
        width: 62% !important;
    }
}

@media screen and (min-width: 1084px) {
    .eaPlay .eaPlayLogo {
        width: 50% !important;
    }
}

@media screen and (max-width: 1083px) {
    .eaPlay .eaPlayLogo {
        width: 68% !important;
    }
}

@media screen and (min-width: 850px) and (max-width: 1300px) {
    .eaPlayHeading {
        font-size: 28px;
        line-height: 32px;
    }
}

@media screen and (min-width: 768px) and (max-width: 849px) {
    .eaPlayHeading {
        font-size: 24px;
        line-height: 28px;
    }
}

@media screen and (max-width:1399px) and (min-width:768px) {
    .eaPlay .m-hero-item .c-paragraph-1 {
        font-size: 15px !important;
    }
}

@media screen and (min-width: 1084px) {
    .eaPlayWidth {
        width: 70%;
    }
}

@media screen and (min-width: 940px) {
    .eaPlayWidth {
        width: 100%;
    }
}

@media screen and (max-width: 939px) and (min-width: 768px) {
    .eaPlayWidth {
        width: 85%;
    }
}

@media screen and (max-width: 440px){
    .eaPlay .m-hero-item > div {
        height: 280px;
    }
    .eaPlay .m-hero-item .eaPlayWidth {
        margin-top: 18px;
    }
    .eaPlay .m-hero-item .eaPlayWidth .eaPlayHeading {
        font-size: 24px;
        line-height: 30px;
    }
    .eaPlay .m-hero-item .eaPlayWidth .c-paragraph-1 {
        font-size: 16px;
        line-height: 20px;
    }
}

@media screen and (max-width: 400px) {
.ctaWrap .m-hero-item .c-group a.c-call-to-action {
    text-wrap: auto;
    text-align: left;}

.ctaWrap .m-hero-item .c-group a.c-call-to-action span {
   display: inline;}

.eaPlay .m-hero-item .eaPlayWidth {
    margin-top: 20px;}
.eaPlay .m-hero-item .eaPlayWidth .eaPlayHeading {
    font-size: 22px;
    line-height: 28px;}
.eaPlay .m-hero-item .eaPlayWidth .c-paragraph-1 {
    font-size: 14px;
    line-height: 18px;}
}







.lightboxcontent .c-glyph.glyph-cancel:before {
    z-index: -1;
}




.high-contrast-test {
    font-size: 10px;
    line-height: 1em;
}</style><style class="darkreader darkreader--sync" media="screen"></style>
    
    <script>
        $('link[rel=stylesheet][href*="/bundles/xboxsplash"]').remove();
        $('link[rel=stylesheet][href*="/bundles/xboxstyles"]').remove();
        $('link[rel=stylesheet][href*="/bundles/xboxonemobile"]').remove();
        $('link[rel=stylesheet][href*="/bundles/xboxonecommon"]').remove();
        $('link[rel=stylesheet][href*="/bundles/xboxonemobile"]').remove();
        $('link[rel=stylesheet][href*="/Shell/css/contentBlocks.mobile.css"]').remove();
        
        $('link[rel=stylesheet][href~="/en-us/global-shares/Picchu-Grid/CSS/mscom-grid-mixed.css"]').remove();
        $('link[rel=stylesheet][href~="/en-us/global-shares/Picchu-Grid/CSS/Picchu.css"]').remove();
    </script>

    <!--<div id="btt"></div>-->
    
<script>
    $(document).ready(function() {
        $("body").append('<div class="high-contrast-test" style="color:#999; width:0px; height: 0px;"></div>');
        var rgb = $('.high-contrast-test').css('color').match(/+/g);
        if (rgb[0] > 153) {$('html').addClass('high-contrast-mode white-on-black');}
        if (rgb[0] < 153) {$('html').addClass('high-contrast-mode black-on-white');}
    });
</script></div><div id="Page Bar - Xbox Game Pass Games" class="pageBar" role="none"><div class="m-in-page-navigation">
    <div data-js-in-page-navigation-wrapper="true">
        <nav class="c-in-page-navigation" aria-label="vá para uma seção na página">

            <div class="c-navigation-menu">
                <button aria-controls="divMenuA" aria-haspopup="true" aria-expanded="false" class="c-heading-6">Jogos do Xbox Game Pass</button>
                <ul id="divMenuA" aria-hidden="true">
                    <li>
                        <a href="#all-games" class="c-hyperlink">Navegar todos os jogos</a>
                    </li>
                    <li>
                        <a href="#benefits" class="c-hyperlink">Benefícios</a>
                    </li>
                    <li>
                        <a href="#xbox-apps" class="c-hyperlink">Aplicativos</a>
                    </li>
                    <li>
                        <a href="https://account.microsoft.com/account" class="c-hyperlink" data-cta="internal" target="_blank" aria-label="Gerenciar assinatura">Gerenciar a assinatura</a>
                    </li>
                </ul>
            </div>

            <p class="c-heading-6 zpt desktopHeadline">Jogos do Xbox Game Pass&nbsp;&nbsp;&nbsp;</p>
            <ul>
                <li>
                        <a href="#all-games" class="c-hyperlink">Navegar todos os jogos</a>
                    </li>
                    <li>
                        <a href="#benefits" class="c-hyperlink">Benefícios</a>
                    </li>
                    <li>
                        <a href="#xbox-apps" class="c-hyperlink">Aplicativos</a>
                    </li>
                    <li>
                        <a href="https://account.microsoft.com/account" class="c-hyperlink" data-cta="internal" target="_blank" aria-label="Gerenciar assinatura">Gerenciar a assinatura</a>
                    </li>
            </ul>
            <div class="CTAdiv">
                <!-- add c-call-to-action c-glyph, and add role='link' when this needs to function as a link, but don't remove c-button f-primary --> <button data-cta-href="" data-target="" class="cta_internal c-button f-primary hidden" aria-label="" tabindex="0" data-loc-cta-href="keyCtahrefpagebarcta" data-loc-aria="keyAriapagebarcta"><span data-loc-copy="keyCopypagebarcta"></span></button> <button role="link" data-cta-href="" data-target="" class="cta_external c-button f-primary c-call-to-action c-glyph hidden" aria-label="" tabindex="0" data-loc-cta-href="keyCtahrefpagebarcta" data-loc-aria="keyAriapagebarcta"><span data-loc-copy="keyCopypagebarcta"></span></button>
            </div>
        </nav>
    </div>
</div></div><div id="Hero - Xbox Game Pass Games" class="SB-hero-banner head1a" role="none"><div class="" data-grid="container"></div>

<div data-grid="col-12" class="m-banner zpt jumpgcontainer">
    <h1 class="c-heading-1a green-c">JOGOS DO XBOX GAME PASS</h1>
     <span class="jump-g jump-b jumpganimate" aria-hidden="true"></span>   
</div>

<div class="banner-background">
    <div data-grid="col-12" class="m-banner zpt">
        <p class="c-subheading-2" data-loc-copy="keyCopyherosubheading"></p>
        <div class="x-type-center c-group">
            <a href="" class="c-call-to-action c-glyph f-heavyweight" aria-label="" data-cta="internal" data-loc-link="keyLinkherocta1" data-loc-aria="keyAriaherocta1"> <span data-loc-copy="keyCopyherocta1"></span> </a> <a href="" class="optionalEl c-call-to-action c-glyph f-lightweight" aria-label="" data-loc-link="keyLinkherocta2" data-loc-aria="keyAriaherocta2"> <span data-loc-copy="keyCopyherocta2"></span> </a>
        </div>
    </div>
</div>

<div class="" data-grid="container"></div></div><div id="GameCarouselFeatured2025" role="none"><div class="gamesSection" data-grid="container">
<h2 class="x-screen-reader" data-loc-copy="keyCopytitle">Jogos em destaque</h2>
    <div class="featured-games specialFeatured" data-games-filter="avail-download">

        <div class="gamesCarousel">
          <div class="c-carousel f-single-slide f-scrollable-next" role="region" aria-label="featured game carousel" style="touch-action: pan-y;">
              <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
              <div itemscope="" itemtype="http://schema.org/ItemList">
                  <ul class="c-group f-active">
                    <li>
                      <section class="m-product-placement-item context-software f-size-large" itemscope="" itemtype="http://schema.org/Product">
                        <a target="_blank" tabindex="-1" href="https://www.xbox.com/games/store/keeper/9NCJWHHMVHR0" data-retailer="ms store" data-loc-link="keyLinkgame1">
                          <div class="f-default-image"> 
                            <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/0c/77/0c776e33-3351-4f2b-b4f5-34b57d157db3.jpg?n=XGP-Catalog_Product-Placement-0_0994443029666_780x1170.jpg" src="https://assets.xboxservices.com/assets/74/a1/74a10e81-d565-4939-b085-e35657b1f39c.png?n=image_small_40x40_blank.png" alt="Um pássaro está pousado no topo de um farol, a luz lança um raio com uma imagem de terras misteriosas " data-loc-image="keyImagegame1" data-loc-alt="keyAltgame1"> </picture>
                          </div>
                          </a><div class="slide-content high-contrast"><a tabindex="-1" target="_blank" href="https://www.xbox.com/games/store/keeper/9NCJWHHMVHR0" data-retailer="ms store" data-loc-link="keyLinkgame1"> 
                            <strong class="c-badge f-small f-highlight badge-green c-caption-2 featbadgePlans" data-loc-copy="keyCopybadge1">ULTIMATE · PC</strong>
                            <strong class="c-badge f-small f-highlight badge-silver c-caption-2 featbadgePlats" data-loc-copy="keyCopybadge1signedin-ult">CONSOLE · PC · NUVEM</strong>
                            <h3 class="c-heading-3 f-lean high-contrast" itemprop="game name" data-loc-copy="keyCopygame1title">Keeper</h3>
                            <p class="c-subheading-2 high-contrast" data-loc-copy="keyCopygame1subheading">Uma história contada sem palavras.</p>
                            </a><a href="https://www.xbox.com/games/store/keeper/9NCJWHHMVHR0" class="c-call-to-action f-lightweight c-glyph sfLink lime-green-c" data-loc-link="keyLinkgame1" data-loc-aria="keyAriagame1" data-loc-retailer="keyRetailergame1" aria-label="Explorar, explorar Keeper" data-retailer="MS Store"> <span data-loc-copy="keyCopygame1cta">EXPLORE</span> </a>
                          </div>
                        
                      </section>
                    </li>

                    <li>
                      <section class="m-product-placement-item context-software f-size-large" itemscope="" itemtype="http://schema.org/Product">
                        <a target="_blank" tabindex="-1" href="https://www.xbox.com/games/store/hogwarts-legacy-xbox-series-x-s-version/9mt5nj5w7b8z" data-retailer="ms store" data-loc-link="keyLinkgame2">
                          <div class="f-default-image"> 
                            <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/12/0d/120dee96-0e25-43b2-863e-93b2be884765.jpg?n=944198_Product-Placement-0_Hogwarts-Legacy_780x1170.jpg" src="https://assets.xboxservices.com/assets/74/a1/74a10e81-d565-4939-b085-e35657b1f39c.png?n=image_small_40x40_blank.png" alt="Portkey Games Hogwarts Legacy: um feiticeiro segurando uma varinha mágica cavalga em uma majestosa ave observando Hogwarts ao longe." data-loc-image="keyImagegame2" data-loc-alt="keyAltgame2"> </picture>
                          </div>
                          </a><div class="slide-content high-contrast"><a tabindex="-1" target="_blank" href="https://www.xbox.com/games/store/hogwarts-legacy-xbox-series-x-s-version/9mt5nj5w7b8z" data-retailer="ms store" data-loc-link="keyLinkgame2"> 
                            <strong class="c-badge f-small f-highlight badge-green c-caption-2 featbadgePlans" data-loc-copy="keyCopybadge2">ULTIMATE · PREMIUM · PC</strong>
                            <strong class="c-badge f-small f-highlight badge-silver c-caption-2 featbadgePlats" data-loc-copy="keyCopybadge2signedin-ult">CONSOLE · PC · NUVEM</strong> 
                            <h3 class="c-heading-3 f-lean high-contrast" itemprop="game name" data-loc-copy="keyCopygame2title">Hogwarts Legacy</h3>
                            <p class="c-subheading-2 high-contrast" data-loc-copy="keyCopygame2subheading">Viva o inesperado</p>
                            </a><a href="https://www.xbox.com/games/store/hogwarts-legacy-xbox-series-x-s-version/9mt5nj5w7b8z" class="c-call-to-action f-lightweight c-glyph sfLink lime-green-c" data-loc-link="keyLinkgame2" data-loc-aria="keyAriagame2" data-loc-retailer="keyRetailergame2" aria-label="Explorar, explorar Hogwarts Legacy" data-retailer="MS Store"> <span data-loc-copy="keyCopygame2cta">EXPLORE</span> </a>
                          </div>
                        
                      </section>
                    </li>

                    <li>
                      <section class="m-product-placement-item context-software f-size-large" itemscope="" itemtype="http://schema.org/Product">
                        <a target="_blank" tabindex="-1" href="https://www.xbox.com/games/store/hollow-knight-silksong/9n116v0599hb" data-retailer="ms store" data-loc-link="keyLinkgame3">
                          <div class="f-default-image"> 
                            <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/8c/f2/8cf20ea2-5a4b-42f9-a9b1-d08dc3f35a34.jpg?n=944198_Product-Placement-0_Hollow-Knight-Silksong_780x1170.jpg" src="https://assets.xboxservices.com/assets/74/a1/74a10e81-d565-4939-b085-e35657b1f39c.png?n=image_small_40x40_blank.png" alt="Hollow Knight: Silksong: um personagem com uma máscara branca e capa vermelha salta no ar empunhando uma espada. " data-loc-image="keyImagegame3" data-loc-alt="keyAltgame3"> </picture>
                          </div>
                          </a><div class="slide-content high-contrast"><a tabindex="-1" target="_blank" href="https://www.xbox.com/games/store/hollow-knight-silksong/9n116v0599hb" data-retailer="ms store" data-loc-link="keyLinkgame3"> 
                            <strong class="c-badge f-small f-highlight badge-green c-caption-2 featbadgePlans" data-loc-copy="keyCopybadge3">ULTIMATE · PC</strong>
                            <strong class="c-badge f-small f-highlight badge-silver c-caption-2 featbadgePlats" data-loc-copy="keyCopybadge3signedin-ult">CONSOLE · PC · NUVEM</strong>
                            <h3 class="c-heading-3 f-lean high-contrast" itemprop="game name" data-loc-copy="keyCopygame3title">Hollow Knight: Silksong</h3>
                            <p class="c-subheading-2 high-contrast" data-loc-copy="keyCopygame3subheading">Lute pelo destino de uma terra assombrada</p>
                            </a><a href="https://www.xbox.com/games/store/hollow-knight-silksong/9n116v0599hb" class="c-call-to-action f-lightweight c-glyph sfLink lime-green-c" data-loc-link="keyLinkgame3" data-loc-aria="keyAriagame3" data-loc-retailer="keyRetailergame3" aria-label="Explorar, explorar Hollow Knight: Silksong" data-retailer="MS Store"> <span data-loc-copy="keyCopygame3cta">EXPLORE</span> </a>
                          </div>
                        
                      </section>
                    </li>
                  </ul>
              </div>
          </div>
        </div>

    </div>
  </div></div><div id="Product Placement - GameCarousel1/2" class="f2pRecoCarousel" role="none"><div class="gamesSection" id="GameCarousel1and2" data-grid="container">
<div class="featured-games" data-games-filter="avail-download">

    <div class="rotator-heading">
        <div>
            <h2 class="c-heading-3 zpt"></h2>
            <p class="c-subheading-4"></p>
        </div>
    </div>

<div class="c-pivot zmt" style="touch-action: pan-y;">
    <span class="f-pivot-accessibility-text">use as teclas de seta para navegar pelos pivôs e tab para focar no conteúdo em uma seção dinâmica</span> <button class="c-flipper f-previous" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <ul role="tablist" class="carouselselection">
        <li class="f-active" role="tab" tabindex="0" aria-controls="consoleGamesOne" aria-label="Mudar para a versão de console desta lista" aria-setsize="2" aria-posinset="1" aria-selected="true">Jogos de console</li>
        <li role="tab" aria-controls="pcGamesOne" aria-label="selecionar jogos para PC" data-loc-aria="keyAriaxgppivotpc" data-loc-copy="keyCopyxgppivotpc" tabindex="-1" aria-setsize="2" aria-posinset="2" aria-selected="false">Jogos para PC</li>
    </ul>

    <button class="c-flipper f-next" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <section id="consoleGamesOne" role="tabpanel" aria-hidden="false">

            <div class="spinnerHold">
              <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
                <span></span> <span></span> <span></span> <span></span> <span></span>
              </div>
            </div>

            <div class="gamesCarousel gcConsole">
              <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para console nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
              <div class="c-carousel f-single-slide" role="region" aria-label="jogos de console nesta categoria" style="touch-action: pan-y;">
                  <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
                  <div itemscope="" itemtype="http://schema.org/ItemList">
                      <ul class="c-group ">
                      </ul>
                  </div>
              </div>
            </div>


    </section>

    <section id="pcGamesOne" role="tabpanel" aria-hidden="true" class="loading">
            <div class="spinnerHold">
              <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
                <span></span> <span></span> <span></span> <span></span> <span></span>
              </div>
            </div>

            <div class="gamesCarousel gcPc">
              <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para PC nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
              <div class="c-carousel f-single-slide" role="region" aria-label="Jogos para PC nesta categoria" style="touch-action: pan-y;">
                  <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
                  <div itemscope="" itemtype="http://schema.org/ItemList">
                      <ul class="c-group ">
                      </ul>
                  </div>
              </div>
            </div>
    </section>

</div>

</div>
</div>

<div class="gamesSection" data-grid="container">
    <div class="featured-games" data-games-filter="avail-download">
        <div class="rotator-heading">
            <div>
                <h2 class="c-heading-3 zpt"></h2>
                <p class="c-subheading-4"></p>
            </div>
        </div>

<div class="c-pivot zmt" style="touch-action: pan-y;">
    <span class="f-pivot-accessibility-text">use as teclas de seta para navegar pelos pivôs e tab para focar no conteúdo em uma seção dinâmica</span> <button class="c-flipper f-previous" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <ul role="tablist" class="carouselselection">
        <li class="f-active" role="tab" tabindex="0" aria-controls="consoleGamesTwo" aria-label="Mudar para a versão de console desta lista" aria-setsize="2" aria-posinset="1" aria-selected="true">Jogos de console</li>
        <li role="tab" aria-controls="pcGamesTwo" aria-label="Mudar para a versão de PC desta lista" tabindex="-1" aria-setsize="2" aria-posinset="2" aria-selected="false">Jogos para PC</li>
    </ul>

    <button class="c-flipper f-next" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <section id="consoleGamesTwo" role="tabpanel" aria-hidden="false">

        <div class="spinnerHold">
           <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
             <span></span> <span></span> <span></span> <span></span> <span></span>
           </div>
        </div>

        <div class="gamesCarousel gcConsole">
          <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para console nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
          <div class="c-carousel f-single-slide" role="region" aria-label="jogos de console nesta categoria" style="touch-action: pan-y;">
              <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
              <div itemscope="" itemtype="http://schema.org/ItemList">
                  <ul class="c-group ">
                  </ul>
              </div>
          </div>
        </div>

    </section>


    <section id="pcGamesTwo" role="tabpanel" aria-hidden="true" class="loading">
        <div class="spinnerHold">
           <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
             <span></span> <span></span> <span></span> <span></span> <span></span>
           </div>
        </div>


        <div class="gamesCarousel gcPc">
          <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para PC nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
          <div class="c-carousel f-single-slide" role="region" aria-label="Jogos para PC nesta categoria" style="touch-action: pan-y;">
              <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
              <div itemscope="" itemtype="http://schema.org/ItemList">
                  <ul class="c-group ">
                  </ul>
              </div>
          </div>
        </div>
    </section>

</div>

    </div>
</div>
</div><div id="Benefits" class="cat-benefits" role="none"><div class="" id="benefits">
    <div class="gamesSection" data-grid="container">
        <div class="featured-games specialFeatured">
            <div class="rotator-heading">
                <div>
                    <h2 class="c-heading-3 zpt">Benefícios do Xbox Game Pass</h2>
                </div>
            </div>
            <div class="gamesCarousel">
                <div class="c-carousel f-single-slide f-scrollable-next" aria-label="carrossel de campanhas anteriores" style="touch-action: pan-y;">
                    <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
                    <div>
                        <ul class="c-group benefitsCardList f-active">

                            <!-- Card 1 --><li data-benefitscard="1">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/a8/7d/a87dd7bc-827f-4d2e-9bf7-ad3d88508b16.jpg?n=944198-Card-Rotator-0_PDO_520x600_02.jpg" src="https://cms-assets.xboxservices.com/assets/a8/7d/a87dd7bc-827f-4d2e-9bf7-ad3d88508b16.jpg?n=944198-Card-Rotator-0_PDO_520x600_02.jpg" alt="Painéis de jogos exibindo artes de Hollow Knight: Silksong, The Outer Worlds 2 e Call of Duty: Black Ops 7"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">ULTIMATE</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">PC</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Jogos no primeiro dia</h3>
                                        <p class="c-paragraph">Jogue novos jogos no primeiro dia.</p>
                                        <div class="">
                                            <a href="#playdayone" class="c-call-to-action f-lightweight c-glyph lime-green-c catLink" target="_blank" aria-label="Explorar jogos, explorar os jogos do Game Pass disponíveis no lançamento"> <span>EXPLORE JOGOS</span> </a> <a href="https://www.xbox.com/xbox-game-pass#join" class="c-call-to-action f-lightweight c-glyph lime-green-c benefitsUpgradeCta upgCore" data-cta="internal" target="_blank" aria-label="Atualizar para o Ultimate, assinar o Xbox Game Pass Ultimate para obter benefícios adicionais"> <span>ATUALIZE PARA O ULTIMATE</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                 <!-- Card 2 --> <!-- PT-BR -->
                            <li data-benefitscard="2">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture>
                                            <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/b3/9f/b39f64d3-08ea-47a8-b9eb-16d263bce674.jpg?n=944198-Card-Rotator-0_br_520x600.jpg" src="https://cms-assets.xboxservices.com/assets/b3/9f/b39f64d3-08ea-47a8-b9eb-16d263bce674.jpg?n=944198-Card-Rotator-0_br_520x600.jpg" alt="Logotipo do Clube Fortnite">
                                        </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">DISPONÍVEL EM NOVEMBRO NO ULTIMATE</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Clube Fortnite</h3>
                                        <p class="c-paragraph">Obtenha acesso ao Passe de Batalha do Fortnite, 1.000 V-Bucks a cada mês e mais.
                                            <a class="c-hyperlink lime-green-c" aria-label="**, vá para a seção jurídica" href="#fortniteinfo-PT-BR">*</a>
                                        </p>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 3 --><li data-benefitscard="3">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/38/d4/38d49b62-42f7-4aa0-92d3-235e08f45c95.jpg?n=944198-Card-Rotator-0_EA-Play_520x600_03.jpg" src="https://cms-assets.xboxservices.com/assets/38/d4/38d49b62-42f7-4aa0-92d3-235e08f45c95.jpg?n=944198-Card-Rotator-0_EA-Play_520x600_03.jpg" alt="Uma coleção de jogos publicados pela EA, incluindo EA SPORTS FC™ 25, Madden NFL 25 e muitos outros"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">ULTIMATE</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">PC</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">EA Play</h3>
                                        <p class="c-paragraph">Tenha acesso a uma coleção das séries favoritas da EA.</p>
                                        <div class="">
                                            <a href="https://www.xbox.com/games/ea-play" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Explorar o EA Play, saber mais sobre o EA Play"> <span>EXPLORE O EA PLAY</span> </a> <a href="https://www.xbox.com/xbox-game-pass#join" class="c-call-to-action f-lightweight c-glyph lime-green-c benefitsUpgradeCta upgCore" data-cta="internal" target="_blank" aria-label="Atualizar para o Ultimate, assinar o Xbox Game Pass Ultimate para obter benefícios adicionais"> <span>ATUALIZE PARA O ULTIMATE</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 4 --><li data-benefitscard="4">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/02/aa/02aabad6-a34c-4405-8cb3-316dd29b84d4.jpg?n=944198-Card-Rotator-0_02_520x600.jpg" src="https://cms-assets.xboxservices.com/assets/02/aa/02aabad6-a34c-4405-8cb3-316dd29b84d4.jpg?n=944198-Card-Rotator-0_02_520x600.jpg" alt="Ubisoft plus Classics, três painéis mostrando artes dos jogos Far Cry 6, Assassin's Creed Valhalla e Rainbow Six Siege"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">ULTIMATE</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Ubisoft+ Classics</h3>
                                        <p class="c-paragraph">Descubra mais de 50 jogos icônicos, incluindo o Ubisoft+ Classics.</p>
                                        <div class="">
                                            <a href="#ubisoftclassics" class="c-call-to-action f-lightweight c-glyph lime-green-c catLink" target="_blank" aria-label="Explorar os clássicos da Ubisoft Plus, ver os jogos da Ubisoft incluídos"> <span>EXPLORE O UBISOFT+ CLASSICS</span> </a> <a href="https://www.xbox.com/xbox-game-pass#join" class="c-call-to-action f-lightweight c-glyph lime-green-c benefitsUpgradeCta upgCons upgCore" data-cta="internal" target="_blank" aria-label="Atualizar para o Ultimate, assinar o Xbox Game Pass Ultimate para obter benefícios adicionais"> <span>ATUALIZE PARA O ULTIMATE</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 5 --><li data-benefitscard="5">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/61/de/61de8564-9da8-438a-9445-7d4b6846f4eb.jpg?n=944198-Card-Rotator-0_Cloud_520x600_03.jpg" src="https://cms-assets.xboxservices.com/assets/61/de/61de8564-9da8-438a-9445-7d4b6846f4eb.jpg?n=944198-Card-Rotator-0_Cloud_520x600_03.jpg" alt="Imagens de jogo do Microsoft Flight Simulator aparecendo nas telas de vários dispositivos, incluindo laptop, TV, telefone e tablet"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">ULTIMATE</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">PREMIUM</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">ESSENTIAL</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Jogos na nuvem</h3>
                                        <p class="c-paragraph">Transmita jogos da nuvem em celulares, tablets, TVs e headsets VR.</p>
                                        <div class="">
                                            <a href="https://www.xbox.com/cloud-gaming" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Explorar o Cloud Gaming, saber mais sobre o Cloud Gaming com o Xbox"> <span>EXPLORE O CLOUD GAMING</span> </a> <a href="https://www.xbox.com/xbox-game-pass#join" class="c-call-to-action f-lightweight c-glyph lime-green-c benefitsUpgradeCta upgPcgp upgCons" data-cta="internal" target="_blank" aria-label="Atualizar para o Ultimate, assinar o Xbox Game Pass Ultimate para obter benefícios adicionais"> <span>ATUALIZE PARA O ULTIMATE</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 6 --><li data-benefitscard="6">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/eb/26/eb269621-5200-49c6-906d-81ab7712d793.jpg?n=944198-Card-Rotator-0_Rewards_520x600_02.jpg" src="https://cms-assets.xboxservices.com/assets/eb/26/eb269621-5200-49c6-906d-81ab7712d793.jpg?n=944198-Card-Rotator-0_Rewards_520x600_02.jpg" alt="Ícone de fita de premiação iluminada"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">TODOS OS PLANOS</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Jogue e ganhe recompensas</h3>
                                        <p class="c-paragraph copyDefault">Ganhe ainda mais recompensas com o Xbox Game Pass.</p>
                                        <p class="c-paragraph copyUlt hidden">Ganhe até 100.000 pontos do Rewards por ano na Loja<a class="c-hyperlink lime-green-c" aria-label="†, acessar a seção jurídica para obter mais informações sobre as recompensas" href="#rewardsinfo">†</a></p>
                                        <p class="c-paragraph copyPcgp hidden">Ganhe até 50.000 pontos do Rewards por ano na Loja<a class="c-hyperlink lime-green-c" aria-label="†, acessar a seção jurídica para obter mais informações sobre as recompensas" href="#rewardsinfo">†</a></p>
                                        <p class="c-paragraph copyCore hidden">Ganhe até 25.000 pontos do Rewards por ano na Loja<a class="c-hyperlink lime-green-c" aria-label="†, acessar a seção jurídica para obter mais informações sobre as recompensas" href="#rewardsinfo">†</a></p>
                                        <div class="">
                                            <a href="https://www.xbox.com/rewards" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Explorar Rewards, saber mais sobre as recompensas com o Xbox"> <span>EXPLORE O REWARDS</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 7 --><li data-benefitscard="7">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/e3/0c/e30c06b9-a187-4874-a5be-148eab796d11.jpg?n=944198-Card-Rotator-0_In-Game-Benefits_520x600_02.jpg" src="https://cms-assets.xboxservices.com/assets/e3/0c/e30c06b9-a187-4874-a5be-148eab796d11.jpg?n=944198-Card-Rotator-0_In-Game-Benefits_520x600_02.jpg" alt="Arte de diversos jogos gratuitos, incluindo League of Legends, Call of Duty: Warzone e Overwatch 2"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">TODOS OS PLANOS</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Benefícios in-game</h3>
                                        <p class="c-paragraph">Desbloqueie itens para melhorar sua experiência de jogo.</p>
                                        <div class="">
                                            <a href="https://www.xbox.com/xbox-game-pass/in-game-benefits" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Explorar benefícios no jogo, saber mais sobre benefícios no jogo com o Game Pass"><span>EXPLORE BENEFÍCIOS NO JOGO</span></a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 8 --><li data-benefitscard="8">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/3f/1d/3f1dbe21-3e0d-499d-b546-7c9249dd90f4.jpg?n=944198-Card-Rotator-0_Multiplayer_520x600_02.jpg" src="https://cms-assets.xboxservices.com/assets/3f/1d/3f1dbe21-3e0d-499d-b546-7c9249dd90f4.jpg?n=944198-Card-Rotator-0_Multiplayer_520x600_02.jpg" alt="Duas pessoas usando headsets jogando juntas no Xbox em um sofá"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">ULTIMATE</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">PREMIUM</strong> <strong class="c-badge f-small f-highlight f-greenhighlight">ESSENTIAL</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Jogos multijogador</h3>
                                        <p class="c-paragraph">Jogue junto com o modo multijogador online no console.</p>
                                        <div class="">
                                            <a href="https://www.xbox.com/games/all-games/console?xr=shellnav&amp;Multiplayer=OnlineMultiplayerWithGold" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Pesquisar por jogos, pesquisar todos os jogos multijogador online"> <span> EXPLORAR JOGOS MULTIJOGADOR</span> </a> <a href="https://www.xbox.com/xbox-game-pass#join" class="c-call-to-action f-lightweight c-glyph lime-green-c benefitsUpgradeCta upgPcgp upgCons" data-cta="internal" target="_blank" aria-label="Atualizar para o Ultimate, assinar o Xbox Game Pass Ultimate para obter benefícios adicionais"> <span>ATUALIZAR PARA O ULTIMATE</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>

                            <!-- Card 9 --><li data-benefitscard="9">
                                <section class="m-product-placement-item context-software f-size-large">
                                    <div class="f-default-image">
                                        <picture> <img class="c-image" aria-hidden="false" srcset="https://cms-assets.xboxservices.com/assets/4f/52/4f52a74c-3c1d-4bfe-8d5e-eec975de4bb0.jpg?n=944198-Card-Rotator-0_Deals_520x600.jpg6.jpg" src="https://cms-assets.xboxservices.com/assets/4f/52/4f52a74c-3c1d-4bfe-8d5e-eec975de4bb0.jpg?n=944198-Card-Rotator-0_Deals_520x600.jpg6.jpg" alt="Ícone de uma etiqueta de desconto"> </picture>
                                    </div>
                                    <div class="slide-content high-contrast">
                                        <div class="badge-group">
                                            <strong class="c-badge f-small f-highlight f-greenhighlight">TODOS OS PLANOS</strong>
                                        </div>
                                        <h3 class="c-heading-3 f-lean">Ofertas e descontos</h3>
                                        <p class="c-paragraph">Desbloqueie descontos em jogos, benefícios de parceiros e muito mais.</p>
                                        <div class="">
                                            <a href="https://www.xbox.com/xbox-game-pass/deals" class="c-call-to-action f-lightweight c-glyph lime-green-c" data-cta="learn" target="_blank" aria-label="Explorar ofertas, explorar quais ofertas você recebe com sua assinatura do Game Pass"> <span>EXPLORE OFERTAS</span> </a>
                                        </div>
                                    </div>
                                </section>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div></div><div id="Product Placement - GameCarousel3/4" class="f2pRecoCarousel" role="none"><div class="gamesSection" id="GameCarousel3and4" data-grid="container">
<div class="featured-games" data-games-filter="avail-download">

    <div class="rotator-heading">
        <div>
            <h2 class="c-heading-3 zpt"></h2>
            <p class="c-subheading-4"></p>
        </div>
    </div>

<div class="c-pivot zmt" style="touch-action: pan-y;">
    <span class="f-pivot-accessibility-text">use as teclas de seta para navegar pelos pivôs e tab para focar no conteúdo em uma seção dinâmica</span> <button class="c-flipper f-previous" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <ul role="tablist" class="carouselselection">
        <li class="f-active" role="tab" tabindex="0" aria-controls="consoleGamesThree" aria-label="Mudar para a versão de console desta lista" aria-setsize="2" aria-posinset="1" aria-selected="true">Jogos de console</li>
        <li role="tab" aria-controls="pcGamesThree" aria-label="selecionar jogos para PC" data-loc-aria="keyAriaxgppivotpc" data-loc-copy="keyCopyxgppivotpc" tabindex="-1" aria-setsize="2" aria-posinset="2" aria-selected="false">Jogos para PC</li>
    </ul>

    <button class="c-flipper f-next" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <section id="consoleGamesThree" role="tabpanel" aria-hidden="false">

            <div class="spinnerHold">
              <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
                <span></span> <span></span> <span></span> <span></span> <span></span>
              </div>
            </div>

            <div class="gamesCarousel gcConsole">
              <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para console nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
              <div class="c-carousel f-single-slide" role="region" aria-label="jogos de console nesta categoria" style="touch-action: pan-y;">
                  <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
                  <div itemscope="" itemtype="http://schema.org/ItemList">
                      <ul class="c-group ">
                      </ul>
                  </div>
              </div>
            </div>


    </section>

    <section id="pcGamesThree" role="tabpanel" aria-hidden="true" class="loading">
            <div class="spinnerHold">
              <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
                <span></span> <span></span> <span></span> <span></span> <span></span>
              </div>
            </div>

            <div class="gamesCarousel gcPc">
              <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para PC nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
              <div class="c-carousel f-single-slide" role="region" aria-label="Jogos para PC nesta categoria" style="touch-action: pan-y;">
                  <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
                  <div itemscope="" itemtype="http://schema.org/ItemList">
                      <ul class="c-group ">
                      </ul>
                  </div>
              </div>
            </div>
    </section>

</div>

</div>
</div>

<div class="gamesSection" data-grid="container">
    <div class="featured-games" data-games-filter="avail-download">
        <div class="rotator-heading">
            <div>
                <h2 class="c-heading-3 zpt"></h2>
                <p class="c-subheading-4"></p>
            </div>
        </div>

<div class="c-pivot zmt" style="touch-action: pan-y;">
    <span class="f-pivot-accessibility-text">use as teclas de seta para navegar pelos pivôs e tab para focar no conteúdo em uma seção dinâmica</span> <button class="c-flipper f-previous" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <ul role="tablist" class="carouselselection">
        <li class="f-active" role="tab" tabindex="0" aria-controls="consoleGamesFour" aria-label="Mudar para a versão de console desta lista" aria-setsize="2" aria-posinset="1" aria-selected="true">Jogos de console</li>
        <li role="tab" aria-controls="pcGamesFour" aria-label="Mudar para a versão de PC desta lista" tabindex="-1" aria-setsize="2" aria-posinset="2" aria-selected="false">Jogos para PC</li>
    </ul>

    <button class="c-flipper f-next" role="presentation" aria-hidden="true" tabindex="-1"></button>

    <section id="consoleGamesFour" role="tabpanel" aria-hidden="false">

        <div class="spinnerHold">
           <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
             <span></span> <span></span> <span></span> <span></span> <span></span>
           </div>
        </div>

        <div class="gamesCarousel gcConsole">
          <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para console nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
          <div class="c-carousel f-single-slide" role="region" aria-label="jogos de console nesta categoria" style="touch-action: pan-y;">
              <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
              <div itemscope="" itemtype="http://schema.org/ItemList">
                  <ul class="c-group ">
                  </ul>
              </div>
          </div>
        </div>

    </section>


    <section id="pcGamesFour" role="tabpanel" aria-hidden="true" class="loading">
        <div class="spinnerHold">
           <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
             <span></span> <span></span> <span></span> <span></span> <span></span>
           </div>
        </div>


        <div class="gamesCarousel gcPc">
          <a href="#" class="carShopAll c-call-to-action c-glyph f-lightweight" aria-label="EXPLORE MAIS jogos do Xbox Game Pass para PC nesta categoria" data-cta="internal"> <span>EXPLORE MAIS</span> </a>
          <div class="c-carousel f-single-slide" role="region" aria-label="Jogos para PC nesta categoria" style="touch-action: pan-y;">
              <button class="c-flipper f-previous" aria-hidden="true" tabindex="-1"></button> <button class="c-flipper f-next" aria-hidden="true" tabindex="-1"></button>
              <div itemscope="" itemtype="http://schema.org/ItemList">
                  <ul class="c-group ">
                  </ul>
              </div>
          </div>
        </div>
    </section>

</div>

    </div>
</div>
</div><div id="Custom Filter/Catalog" role="none"><section id="thecatalog" class="thecatalog" data-grid="container">
 <div class="ui" id="all-games">

  <h2 class="c-heading-3 accHeading">Jogos<span class="collectionLabel"></span> (<span class="gamesTotal">0</span>)</h2>

  <!-- <div class="platformselection" data-platselected="xbox" data-platclicked = "false" role="region" aria-label="Use estes links para filtrar entre jogos de PC e Console">
      <a href="#" class="platselectbutton platxb platselected" data-theplat="xbox"><span>Console&nbsp;games</span></a>
      <a href="#" class="platselectbutton platpc" data-theplat="pc"><span>PC&nbsp;games</span></a>
    </div> --><div class="searchgroup">
   <div class="c-label">Pesquisar título do jogo</div>
      <form class="c-search gamesearch xghsearch" autocomplete="off" name="form1" target="_self" role="search" aria-label="pesquisar todos os jogos">
        <input aria-label="Pesquisar por jogos" type="search" name="search-field"> <button class="c-glyph high-contrast" name="search-button"> <span class="x-screen-reader">Pesquisar jogos</span> </button> <span class="searcherrormessage"></span>
      </form> 
      <div class="mobFilterButton">
    <button name="openFilters" class="c-button f-primary openFilters">FILTRO</button>
   </div>
    </div>

    <div class="uiDrawers">

     <div class="filterSummary theme-dark">
      <div class="filterNumber c-subheading-5">(<span class="filterCount">0</span>) Filtros aplicados</div>
      <button name="clearFilters" class="c-button green-brdr clearFilters f-disabled">LIMPAR FILTROS</button>
      <ul class="filterSelections c-group f-wrap-items">
        </ul>
     </div>

     <div class="sortUi"></div>

   <div class="refineFilters mobileHidden">

    <div class="c-drawer radioDrawer" aria-label="Classificação do jogo">
       <button class="c-glyph sortDrawer" aria-label="Classificar" aria-expanded="false" aria-controls="gamesort"> Classificar por: <span class="currentSort">Adicionados recentemente</span> </button>

       <div id="gamesort" class="height200" aria-label="Use estes botões de opção para classificar os resultados com base nestes parâmetros para esta página." data-sort="newest" hidden="" style="display: none; height: 0px; overflow: hidden;">
        <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para classificação de jogos">
         <div>
             <div>
              <label class="c-label"> <input aria-posinset="1" aria-setsize="3" id="default1-1" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="default" value="newest" checked="checked"> <span>Adicionados recentemente</span> </label> <label class="c-label"> <input aria-posinset="2" aria-setsize="3" id="default1-2" type="radio" aria-label="Filtrar jogos por título: A-Z" name="default" value="az"> <span>Título (A-Z)</span> </label> <label class="c-label"> <input aria-posinset="3" aria-setsize="3" id="default1-3" type="radio" aria-label="Filtrar jogos por título: Z-A" name="default" value="za"> <span>Título (Z-A)</span> </label>
             </div>
          </div>
      </fieldset>
         
       </div>
    </div>

    <div class="c-drawer radioDrawer membershipsFilter" aria-label="Filtro de assinaturas">
       <button class="c-glyph sortDrawer" aria-label="Filtro de assinaturas" aria-expanded="true" aria-controls="consmemberfilt"> Assinaturas <span class="c-glyph chevron"></span></button>

       <div id="consmemberfilt" class="height200 selectSet" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-membership="allgames" style="display: block; height: auto; overflow: visible;">
        <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de assinaturas">
         <div>
             <div>
              <label class="c-label"> <input aria-posinset="1" aria-setsize="5" id="default2-1" type="radio" aria-label="Filtrar jogos por Game Pass Ultimate" name="default2" value="allgames" checked="checked"> <span>Xbox Game Pass Ultimate</span> </label> <label class="c-label"> <input aria-posinset="2" aria-setsize="5" id="default2-2" type="radio" aria-label="Filtrar jogos por Game Pass Premium" name="default2" value="allgamespremium"> <span>Xbox Game Pass Premium</span> </label> <label class="c-label"> <input aria-posinset="3" aria-setsize="5" id="default2-3" type="radio" aria-label="Filtrar jogos por Game Pass Essential" name="default2" value="allgamesessential"> <span>Xbox Game Pass Essential</span> </label> <label class="c-label"> <input aria-posinset="4" aria-setsize="5" id="default2-4" type="radio" aria-label="Filtrar jogos por Game Pass para Console" name="default2" value="allgamesconsole"> <span>Xbox Game Pass para Console</span> </label> <label class="c-label"> <input aria-posinset="5" aria-setsize="5" id="default2-5" type="radio" aria-label="Filtrar jogos por PC Game Pass" name="default2" value="allgamespc"> <span>Game Pass para PC</span> </label>
             </div>
          </div>
      </fieldset>
         
       </div>
    </div>

  <div class="c-drawer f-checkbox playsonFilter" aria-label="Filtro Jogar em">
       <button class="c-glyph" aria-label="Filtro Jogar em" aria-expanded="true" aria-controls="playsonFilterMult">Continue jogando<span class="c-glyph chevron"></span></button>
       <ul id="playsonFilterMult" class="height200" data-js-select-type="multi-select" aria-label="Use estes links para refinar os resultados com base na plataforma para esta página." style="display: block; height: auto; overflow: visible;">
         <li class="onlyUltimate onlyStandard onlyCore onlyCons">
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos do Xbox&nbsp;Series&nbsp;X|S" data-filt="xboxseries" aria-checked="false"> <span>Xbox Series&nbsp;X|S</span> </a>
          </li>
          <li class="onlyUltimate onlyStandard onlyCore onlyCons">
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos do Xbox One" data-filt="xboxone" aria-checked="false"> <span>Xbox One</span> </a>
          </li>
          <li class="onlyUltimate onlyStandard onlyCore onlyPcgp">
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de PC com Windows" data-filt="pc" aria-checked="false"> <span>PC com Windows</span> </a>
          </li>
          <li class="onlyUltimate onlyStandard onlyCore">
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos em nuvem" data-filt="cloud" aria-checked="false"> <span>Cloud</span> </a>
          </li>
          <li class="onlyUltimate onlyStandard onlyCore onlyPcgp onlyCons">
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos Xbox Play Anywhere" data-filt="xpa" aria-checked="false"> <span>Xbox Play Anywhere</span> </a>
          </li>
       </ul>
    </div>

    <!-- classes: onlyUltimate, onlyStandard, onlyCore, onlyCons, onlyPcgp --><div class="c-drawer radioDrawer onlyUltimate collectionsFilter" aria-label="Filtro coleções">
       <button class="c-glyph sortDrawer" aria-label="Filtro coleções" aria-expanded="true" aria-controls="ultimatecollfilt"> Coleções <span class="c-glyph chevron"></span></button>

       <div id="ultimatecollfilt" class="height200 selectSet collections-xbox" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-collection="allgames" style="display: block; height: auto; overflow: visible;">
        <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de coleções">
         <div>
             <div>
              <label class="c-label"> <input aria-posinset="1" aria-setsize="17" id="default4-1" type="radio" aria-label="Filtrar jogos por Todos os jogos" name="default4" value="allgames" checked="checked"> <span>Todos os jogos</span> </label> <label class="c-label"> <input aria-posinset="2" aria-setsize="17" id="default4-2" type="radio" aria-label="Filtrar jogos por Mais populares" name="default4" value="mostpopular"> <span>Mais populares</span> </label> <label class="c-label"> <input aria-posinset="3" aria-setsize="17" id="default4-3" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="default4" value="recentlyadded"> <span>Adicionados recentemente</span> </label> <label class="c-label"> <input aria-posinset="4" aria-setsize="17" id="default4-4" type="radio" aria-label="Filtrar jogos por Em breve" name="default4" value="comingsoon"> <span>Em breve</span> </label> <label class="c-label"> <input aria-posinset="5" aria-setsize="17" id="default4-5" type="radio" aria-label="Filtrar jogos por Saindo em breve" name="default4" value="leavingsoon"> <span>Saindo em breve</span> </label> <label class="c-label"> <input aria-posinset="6" aria-setsize="17" id="default4-6" type="radio" aria-label="Filtrar jogos por Jogue no primeiro dia" name="default4" value="playdayone"> <span>Jogar no primeiro dia</span> </label> <label class="c-label"> <input aria-posinset="7" aria-setsize="17" id="default4-7" type="radio" aria-label="Filtrar jogos por Activision" name="default4" value="activision"> <span>Activision</span> </label> <label class="c-label"> <input aria-posinset="8" aria-setsize="17" id="default4-8" type="radio" aria-label="Filtrar jogos por Bethesda Softworks" name="default4" value="bethesdasoftworks"> <span>Bethesda Softworks</span> </label> <label class="c-label"> <input aria-posinset="9" aria-setsize="17" id="default4-9" type="radio" aria-label="Filtrar jogos por Blizzard Entertainment" name="default4" value="blizzardentertainment"> <span>Blizzard Entertainment</span> </label> <label class="c-label"> <input aria-posinset="10" aria-setsize="17" id="default4-10" type="radio" aria-label="Filtrar jogos por Xbox Game Studios" name="default4" value="xboxgamestudios"> <span>Xbox Game Studios</span> </label> <label class="c-label"> <input aria-posinset="11" aria-setsize="17" id="default4-11" type="radio" aria-label="Filtrar jogos por EA Play" name="default4" value="eaplay"> <span>EA Play</span> </label> <label class="c-label"> <input aria-posinset="12" aria-setsize="17" id="default4-12" type="radio" aria-label="Filtrar jogos por Testes de jogos do EA Play" name="default4" value="eaplaygametrials"> <span>Avaliações EA Play Game</span> </label> <label class="c-label"> <input aria-posinset="13" aria-setsize="17" id="default4-13" type="radio" aria-label="Filtrar jogos por Riot Games" name="default4" value="riotgames"> <span>Riot Games</span> </label> <label class="c-label"> <input aria-posinset="14" aria-setsize="17" id="default4-14" type="radio" aria-label="Filtrar jogos por Ubisoft Connect" name="default4" value="ubisoftconnect"> <span>Ubisoft Connect</span> </label> <label class="c-label"> <input aria-posinset="15" aria-setsize="17" id="default4-15" type="radio" aria-label="Filtrar jogos por Ubisoft+ Classics" name="default4" value="ubisoftclassics"> <span>Ubisoft+ Classics</span> </label> <label class="c-label"> <input aria-posinset="16" aria-setsize="17" id="default4-16" type="radio" aria-label="Filtrar jogos por ID@Xbox" name="default4" value="idxbox"> <span>ID@Xbox</span> </label> <label class="c-label"> <input aria-posinset="17" aria-setsize="17" id="default4-17" type="radio" aria-label="Filtrar jogos por Benefícios no jogo" name="default4" value="ingamebenefits"> <span>Benefícios no jogo</span> </label>
              
             </div>
          </div>
      </fieldset>
         
       </div>
    </div>

    <div class="c-drawer radioDrawer onlyPcgp collectionsFilter" aria-label="Filtro coleções">
       <button class="c-glyph sortDrawer" aria-label="Filtro coleções" aria-expanded="true" aria-controls="ultimatecollfilt"> Coleções <span class="c-glyph chevron"></span></button>

       <div id="ultimatecollfilt" class="height200 selectSet collections-xbox" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-collection="allgames" style="display: block; height: auto; overflow: visible;">
        <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de coleções">
         <div>
             <div>
              <label class="c-label"> <input aria-posinset="1" aria-setsize="16" id="default114-1" type="radio" aria-label="Filtrar jogos por Todos os jogos" name="default4" value="allgames" checked="checked"> <span>Todos os jogos</span> </label> <label class="c-label"> <input aria-posinset="2" aria-setsize="16" id="default14-2" type="radio" aria-label="Filtrar jogos por Mais populares" name="default4" value="mostpopular"> <span>Mais populares</span> </label> <label class="c-label"> <input aria-posinset="3" aria-setsize="16" id="default14-3" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="default4" value="recentlyadded"> <span>Adicionados recentemente</span> </label> <label class="c-label"> <input aria-posinset="4" aria-setsize="16" id="default14-4" type="radio" aria-label="Filtrar jogos por Em breve" name="default4" value="comingsoon"> <span>Em breve</span> </label> <label class="c-label"> <input aria-posinset="5" aria-setsize="16" id="default14-5" type="radio" aria-label="Filtrar jogos por Saindo em breve" name="default4" value="leavingsoon"> <span>Saindo em breve</span> </label> <label class="c-label"> <input aria-posinset="6" aria-setsize="16" id="default14-6" type="radio" aria-label="Filtrar jogos por Jogue no primeiro dia" name="default4" value="playdayone"> <span>Jogar no primeiro dia</span> </label> <label class="c-label"> <input aria-posinset="7" aria-setsize="16" id="default14-7" type="radio" aria-label="Filtrar jogos por Activision" name="default4" value="activision"> <span>Activision</span> </label> <label class="c-label"> <input aria-posinset="8" aria-setsize="16" id="default14-8" type="radio" aria-label="Filtrar jogos por Bethesda Softworks" name="default4" value="bethesdasoftworks"> <span>Bethesda Softworks</span> </label> <label class="c-label"> <input aria-posinset="9" aria-setsize="16" id="default14-9" type="radio" aria-label="Filtrar jogos por Blizzard Entertainment" name="default4" value="blizzardentertainment"> <span>Blizzard Entertainment</span> </label> <label class="c-label"> <input aria-posinset="10" aria-setsize="16" id="default14-10" type="radio" aria-label="Filtrar jogos por Xbox Game Studios" name="default4" value="xboxgamestudios"> <span>Xbox Game Studios</span> </label> <label class="c-label"> <input aria-posinset="11" aria-setsize="16" id="default14-11" type="radio" aria-label="Filtrar jogos por EA Play" name="default4" value="eaplay"> <span>EA Play</span> </label> <label class="c-label"> <input aria-posinset="12" aria-setsize="16" id="default14-12" type="radio" aria-label="Filtrar jogos por Testes de jogos do EA Play" name="default4" value="eaplaygametrials"> <span>Avaliações EA Play Game</span> </label> <label class="c-label"> <input aria-posinset="13" aria-setsize="16" id="default14-13" type="radio" aria-label="Filtrar jogos por Riot Games" name="default4" value="riotgames"> <span>Riot Games</span> </label> <label class="c-label"> <input aria-posinset="14" aria-setsize="16" id="default14-14" type="radio" aria-label="Filtrar jogos por Ubisoft Connect" name="default4" value="ubisoftconnect"> <span>Ubisoft Connect</span> </label> <label class="c-label"> <input aria-posinset="15" aria-setsize="16" id="default14-15" type="radio" aria-label="Filtrar jogos por ID@Xbox" name="default4" value="idxbox"> <span>ID@Xbox</span> </label> <label class="c-label"> <input aria-posinset="16" aria-setsize="16" id="default14-16" type="radio" aria-label="Filtrar jogos por Benefícios no jogo" name="default4" value="ingamebenefits"> <span>Benefícios no jogo</span> </label>
              
             </div>
          </div>
      </fieldset>
         
       </div>
    </div>

    <div class="c-drawer radioDrawer onlyStandard collectionsFilter hidden" aria-label="Filtro coleções">
       <button class="c-glyph sortDrawer" aria-label="Filtro coleções" aria-expanded="true" aria-controls="standardcollfilt"> Coleções <span class="c-glyph chevron"></span></button>

       <div id="standardcollfilt" class="height200 selectSet collections-xbox" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-collection="allgames" style="display: block; height: auto; overflow: visible;">
    <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de coleções">
     <div>
       <div>
        <label class="c-label"><input aria-posinset="1" aria-setsize="11" id="standard-1" type="radio" aria-label="Filtrar jogos por Todos os jogos" name="standard" value="allgames" checked="checked"><span>Todos os jogos</span></label> <label class="c-label"><input aria-posinset="2" aria-setsize="11" id="standard-2" type="radio" aria-label="Filtrar jogos por Mais populares" name="standard" value="mostpopular"><span>Mais populares</span></label> <label class="c-label"><input aria-posinset="3" aria-setsize="11" id="standard-3" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="standard" value="recentlyadded"><span>Adicionados recentemente</span></label> <label class="c-label"><input aria-posinset="4" aria-setsize="11" id="standard-4" type="radio" aria-label="Filtrar jogos por Em breve" name="standard" value="comingsoon"><span>Em breve</span></label> <label class="c-label"><input aria-posinset="5" aria-setsize="11" id="standard-5" type="radio" aria-label="Filtrar jogos por Saindo em breve" name="standard" value="leavingsoon"><span>Saindo em breve</span></label> <label class="c-label"><input aria-posinset="6" aria-setsize="11" id="standard-6" type="radio" aria-label="Filtrar jogos por Activision" name="standard" value="activision"><span>Activision</span></label> <label class="c-label"><input aria-posinset="7" aria-setsize="11" id="standard-7" type="radio" aria-label="Filtrar jogos por Bethesda Softworks" name="standard" value="bethesdasoftworks"><span>Bethesda Softworks</span></label> <label class="c-label"><input aria-posinset="8" aria-setsize="11" id="standard-8" type="radio" aria-label="Filtrar jogos por Blizzard Entertainment" name="standard" value="blizzardentertainment"><span>Blizzard Entertainment</span></label> <label class="c-label"><input aria-posinset="9" aria-setsize="11" id="standard-9" type="radio" aria-label="Filtrar jogos por Xbox Game Studios" name="standard" value="xboxgamestudios"><span>Xbox Game Studios</span></label> <label class="c-label"><input aria-posinset="10" aria-setsize="11" id="standard-10" type="radio" aria-label="Filtrar jogos por ID@Xbox" name="standard" value="idxbox"><span>ID@Xbox</span></label> <label class="c-label"><input aria-posinset="11" aria-setsize="11" id="standard-11" type="radio" aria-label="Filtrar jogos por Benefícios no jogo" name="standard" value="ingamebenefits"><span>Benefícios no jogo</span></label>
       </div>
      </div>
    </fieldset>
         
       </div>
    </div>

    <div class="c-drawer radioDrawer onlyCore collectionsFilter hidden" aria-label="Filtro coleções">
       <button class="c-glyph sortDrawer" aria-label="Filtro coleções" aria-expanded="true" aria-controls="corecollfilt"> Coleções <span class="c-glyph chevron"></span></button>

       <div id="corecollfilt" class="height200 selectSet collections-xbox" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-collection="allgames" style="display: block; height: auto; overflow: visible;">
            <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de coleções">
            <div>
            <div>
                <label class="c-label"><input aria-posinset="1" aria-setsize="4" id="core-1" type="radio" aria-label="Filtrar jogos por Todos os jogos" name="core" value="allgames" checked="checked"><span>Todos os jogos</span></label> <label class="c-label"><input aria-posinset="2" aria-setsize="4" id="core-2" type="radio" aria-label="Filtrar jogos por Mais populares" name="core" value="mostpopular"><span>Mais populares</span></label> <label class="c-label"><input aria-posinset="3" aria-setsize="4" id="core-3" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="core" value="recentlyadded"><span>Adicionados recentemente</span></label> <label class="c-label"><input aria-posinset="4" aria-setsize="4" id="core-4" type="radio" aria-label="Filtrar jogos por Benefícios no jogo" name="core" value="ingamebenefits"><span>Benefícios no jogo</span></label>
            </div>
            </div>
            </fieldset>
         
       </div>
    </div>

    <div class="c-drawer radioDrawer onlyCons collectionsFilter hidden" aria-label="Filtro coleções">
       <button class="c-glyph sortDrawer" aria-label="Filtro coleções" aria-expanded="true" aria-controls="consolecollfilt"> Coleções <span class="c-glyph chevron"></span></button>

       <div id="consolecollfilt" class="height200 selectSet collections-xbox" aria-label="Use estes botões de opção para filtrar os resultados com base nestes parâmetros para esta página." data-collection="allgames" style="display: block; height: auto; overflow: visible;">
    <fieldset class="c-radio" role="radiogroup" aria-label="Seleções de opções para filtragem de coleções">
     <div>
       <div>
        <label class="c-label"><input aria-posinset="1" aria-setsize="5" id="console-1" type="radio" aria-label="Filtrar jogos por Todos os jogos" name="console" value="allgames" checked="checked"><span>Todos os jogos</span></label> <label class="c-label"><input aria-posinset="2" aria-setsize="5" id="console-2" type="radio" aria-label="Filtrar jogos por Mais populares" name="console" value="mostpopular"><span>Mais populares</span></label> <label class="c-label"><input aria-posinset="3" aria-setsize="5" id="console-3" type="radio" aria-label="Filtrar jogos por Adicionados recentemente" name="console" value="recentlyadded"><span>Adicionados recentemente</span></label> <label class="c-label"><input aria-posinset="4" aria-setsize="5" id="console-4" type="radio" aria-label="Filtrar jogos por Em breve" name="console" value="comingsoon"><span>Em breve</span></label> <label class="c-label"><input aria-posinset="5" aria-setsize="5" id="console-5" type="radio" aria-label="Filtrar jogos por Saindo em breve" name="console" value="leavingsoon"><span>Saindo em breve</span></label>
       </div>
      </div>
    </fieldset>
         
       </div>
    </div>

    <div class="refineHeading"><p class="c-subheading-4">Refinar resultados:</p></div>

    <div class="c-drawer f-checkbox" aria-label="Filtro de Gênero">
       <button class="c-glyph" aria-label="Filtro de Gênero" aria-expanded="false" aria-controls="genreFilter">Gêneros<span class="c-glyph chevron"></span></button>
       <ul id="genreFilter" class="height200" data-js-select-type="multi-select" aria-label="Use os links para refinar os resultados com base no gênero para esta página." hidden="" style="display: none; height: 0px; overflow: hidden;">
         <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de ação e aventura" data-filt="genre-action &amp; adventure" aria-checked="false"> <span>Ação e aventura</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos clássicos" data-filt="genre-classics" aria-checked="false"> <span>Clássicos</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos de família e crianças" data-filt="genre-family" aria-checked="false"> <span>Família e crianças</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos indie" data-filt="genre-indie" aria-checked="false"> <span>Indie</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos de plataformas" data-filt="genre-platformer" aria-checked="false"> <span>Plataforma</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos de quebra-cabeças e curiosidades" data-filt="genre-puzzle" aria-checked="false"> <span>Desafios</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de corrida e voo" data-filt="genre-racing" aria-checked="false"> <span>Corrida e voo</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos de RPG" data-filt="genre-role-playing" aria-checked="false"> <span>RPG</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por Jogos de tiro" data-filt="genre-shooter" aria-checked="false"> <span>Atirador</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de simulação" data-filt="genre-simulation" aria-checked="false"> <span>Simulação</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de esportes" data-filt="genre-sports" aria-checked="false"> <span>Esportes</span> </a>
          </li>
          <li>
            <a class="c-refine-item c-hyperlink" role="checkbox" href="#" aria-label="Refinar por jogos de estratégia" data-filt="genre-strategy" aria-checked="false"> <span>Estratégia</span> </a>
          </li>
       </ul>
    </div>

    <div class="c-drawer f-checkbox" aria-label="Filtro de classificação etária">
       <button class="c-glyph" aria-label="Filtro de classificação etária" aria-expanded="false" aria-controls="ratingFilter">Classificação indicativa<span class="c-glyph chevron"></span></button>
       <ul id="ratingFilter" class="height200" data-js-select-type="multi-select" aria-label="Use estes links para refinar os resultados com base na classificação etária para esta página." hidden="" style="display: none; height: 0px; overflow: hidden;"></ul>
    </div>

    <div class="closeShowResults">
     <button name="closeFilters" class="c-button closeFilters">FECHAR FILTROS</button> <button name="showResults" class="c-button f-primary showResults hidden">MOSTRAR RESULTADOS</button>
    </div>

   </div>
  </div>
 </div>

 <div class="games">

  <div class="m-area-heading spinnerHold">
      <div class="c-progress f-indeterminate-local f-progress-large" role="progressbar" aria-valuetext="Carregando..." tabindex="0" aria-label="barra de progresso grande de local indeterminado">
        <span></span> <span></span> <span></span> <span></span> <span></span>
      </div>  
    </div>

    <div class="specialBanners messageLeavingSoon hide">
      <p class="c-paragraph-4">Estes jogos sairão da biblioteca do Game Pass nas próximas duas semanas. Para continuar jogando, compre agora e economize até 20% com seu desconto de membro.</p>
    </div>

    <div class="specialBanners messageLeavingSoonNone hide">
      <p class="c-paragraph-4">Nenhum jogo sairá da biblioteca do Game Pass nas próximas duas semanas.</p>
    </div>

    <!-- <div class="specialBanners messageLeavingSoonStandard hide">
      <p class="c-paragraph-4">These games exit the Game Pass library in the next two weeks.</p>
    </div> --><div class="specialBanners messagePlayDayOne hide">
      <p class="c-paragraph-4">Jogue os jogos que ingressaram na biblioteca do Game Pass no primeiro dia. Aproveite jogos favoritos do&nbsp;Xbox Game Studios, Bethesda Softworks, Activision Blizzard, estúdios indie e muito mais.</p>
      <a href="https://www.xbox.com/xbox-game-pass/play-day-one" class="c-call-to-action c-glyph f-lightweight" aria-label="Saiba mais sobre como jogar no primeiro dia com o Xbox Game Pass"> <span>SAIBA MAIS</span> </a>
    </div>

    <!-- Banners All PC Banner/ EA PC Banner / Ubisoft PC Banner --><div class="theme-light specialBanner allpcBanner hide">
      <div data-grid="col-12 stack-2" class="theme-light">
        <div data-grid="col-2">
          <img class="" src="https://cms-assets.xboxservices.com/assets/fe/9a/fe9a129d-5b1c-46f6-8d07-c962d54a1c59.svg?n=944198-Catalog_Banner-0_XGP-App_230x120.svg" alt="Logotipo do aplicativo Xbox para PC">
        </div>
        <div data-grid="col-10">
          <h3 class="c-heading-4 zpt">Aplicativo Xbox para PC</h3>
          <p class="c-paragraph">Descubra, baixe, jogue e mantenha-se conectado com o aplicativo Xbox para PC. Veja o que seus amigos estão jogando e converse enquanto jogam juntos. Explore a biblioteca e comece a jogar com um clique.</p>
          <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph f-lightweight bannerDesk win10ban" aria-label="Obter o aplicativo, baixar e iniciar o aplicativo Xbox para PC"> <span>OBTENHA O APLICATIVO</span> </a> <a href="https://www.xbox.com/apps/xbox-app-on-pc" class="c-call-to-action c-glyph f-lightweight bannerMob win10ban" aria-label="Saiba mais, saiba mais sobre o aplicativo Xbox para PC"> <span>SAIBA MAIS</span> </a>
        </div>
      </div>
    </div>

    <div class="theme-light specialBanner eappcBanner hide">
      <div data-grid="col-12 stack-2" class="theme-light">
        <div data-grid="col-2">
          <img class="" src="https://assets.xboxservices.com/assets/54/c3/54c37476-fe31-47ee-b344-e81e6e0a85ad.svg?n=eaplay.svg" alt="Xbox Game Pass com ícones do EA Play">
        </div>
        <div data-grid="col-10">
          <h3 class="c-heading-4 zpt">Explore o EA Play com o aplicativo Xbox no PC com Windows</h3>
          <p class="c-paragraph">Os membros do PC Game Pass e do Ultimate podem acessar o EA Play no Windows pelo aplicativo Xbox no PC com Windows.</p>
          <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph f-lightweight bannerDesk win10ban" aria-label="baixe o aplicativo Xbox para Windows 10"> <span>BAIXE O APLICATIVO</span> </a> <a href="https://www.xbox.com/apps/xbox-app-on-pc" class="c-call-to-action c-glyph f-lightweight bannerMob win10ban" aria-label="Saiba mais sobre o aplicativo Xbox"> <span>SAIBA MAIS</span> </a>
        </div>
      </div>
    </div>

    <div class="theme-light specialBanner ubisoftpcBanner hide">
      <div data-grid="col-12 stack-2" class="theme-light">
        <div data-grid="col-2">
          <img class="" src="https://assets.xboxservices.com/assets/f0/4b/f04b3717-3ecc-48b2-a38b-dda98034e16d.svg?n=XGP-Catalog_Banner-0_XGP-UbiSoft_230x120.svg" alt="Xbox Game Pass com o logotipo do Ubisoft Connect">
        </div>
        <div data-grid="col-10">
          <h3 class="c-heading-4 zpt">Explore o Ubisoft Connect com o aplicativo Xbox no PC com Windows</h3>
          <p class="c-paragraph">Os membros do PC Game Pass e do Ultimate podem acessar determinados títulos do Ubisoft Connect no Windows pelo aplicativo Xbox no PC com Windows.</p>
          <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph f-lightweight bannerDesk win10ban" aria-label="Baixe o aplicativo Ubisoft Connect"> <span>BAIXE O APLICATIVO</span> </a> <a href="https://www.xbox.com/apps/xbox-app-for-pc" class="c-call-to-action c-glyph f-lightweight bannerMob win10ban" aria-label="Saiba mais sobre o aplicativo Xbox"> <span> SAIBA MAIS</span> </a>
        </div>
      </div>
    </div>

    <div class="theme-light specialBanner riotgamespcBanner hide">
      <div data-grid="col-12 stack-2" class="theme-light">
        <div data-grid="col-2">
          <img class="" src="https://assets.xboxservices.com/assets/63/87/638760f8-6d0f-40e0-b215-be4fec0a3c16.svg?n=XGP-Catalog_Banner-0_Riot-Games-XGP_230x120_02.svg" alt="Xbox Game Pass com logotipo da riot games">
        </div>
        <div data-grid="col-10">
          <h3 class="c-heading-4 zpt">Explore Riot Games no aplicativo Xbox para PC</h3>
          <p class="c-paragraph">Jogue jogos selecionados da Riot Games com benefícios premium para membros do Game Pass.</p>
          <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph f-lightweight bannerDesk win10ban" aria-label="Baixe o aplicativo para Riot Games"> <span>BAIXE O APLICATIVO</span> </a> <a href="https://www.xbox.com/apps/xbox-app-for-pc" class="c-call-to-action c-glyph f-lightweight bannerMob win10ban" aria-label="Saiba mais sobre o aplicativo Xbox"> <span>SAIBA MAIS</span> </a>
        </div>
      </div>
    </div>

    <div class="theme-light specialBanner cloudEnabled hide">
      <div data-grid="col-12 stack-2" class="theme-light">
        <div data-grid="col-2">
         <img class="" src="https://assets.xboxservices.com/assets/cb/b9/cbb9b99e-10aa-4d27-a470-0c73140610a2.svg?n=Games-Catalog_Banner-0_Features-Cloud_230x120.svg" alt="Ícone da nuvem">
        </div>
        <div data-grid="col-10">
         <h3 class="c-heading-4 zpt">Xbox Cloud Gaming (Beta)</h3>
         <p class="c-paragraph">Jogue centenas de jogos de alta qualidade nos dispositivos que você já possui.</p>
         <a href="https://www.xbox.com/xbox-game-pass/cloud-gaming" class="c-call-to-action c-glyph f-lightweight" aria-label="Saiba mais sobre o Cloud Gaming"> <span>SAIBA MAIS</span> </a>
        </div>
      </div>
    </div>

    <div class="gameDivsWrapper">
    </div>
    <ul data-grid="col-12" class="m-pagination m-pagination-group">
        <li class="paginateprevious">
            <a class="c-glyph paginateprevious" href="#" aria-label="" data-loc-aria="keyAriapreviouspage"> <span>Anterior</span> </a>
        </li>

        <li class="paginatenext">
            <a class="c-glyph" href="#" aria-label="" data-loc-aria="keyArianextpage"> <span>Próximo</span> </a>
        </li>
    </ul>

    <div data-grid="col-12" class="m-area-heading nogamesfound hidden">
      <p class="c-heading-4">Nenhum jogo encontrado.</p>
    </div>

 </div>
</section>  

<div class="win10link hide">
  <p class="c-paragraph-3 deskOnly padBot">Acesse esse jogo e outros títulos do EA Play com o aplicativo Xbox.</p>
  <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph popbuynow deskOnly" target="_blank" aria-label="baixe o aplicativo xbox"> <span>BAIXE O APLICATIVO XBOX</span> </a>
  <p class="c-paragraph-3 deskOnly">Já tem o aplicativo Xbox? <a href="ms-windows-store://pdp/?ProductId=9MV0B5HZVK9Z" data-retailer="ms store" class="poplastbutton win10button" target="_blank" aria-label="inicie o aplicativo na microsoft store">Abra o aplicativo</a> para jogar este título em seu PC com Windows.</p>
  <p class="c-paragraph-3 mobOnly">Baixe e jogue este título no seu PC com Windows usando o <a href="https://www.xbox.com/apps/xbox-app-on-pc" data-cta="learn" class="poplastbutton win10button" target="_blank" aria-label="Saiba mais sobre o aplicativo Xbox no PC">aplicativo Xbox no PC</a>.</p>
</div>

<div class="nonwin10link hide">
  <p class="c-paragraph-3">Baixe e jogue este título no seu PC com Windows usando o <a href="https://www.xbox.com/apps/xbox-app-on-pc" data-cta="learn" class="poplastbutton win10button" target="_blank" aria-label="Saiba mais sobre o aplicativo Xbox para PC">aplicativo Xbox para PC</a>.
  </p>
</div>

<div class="win10linkriot hide">
  <p class="c-paragraph-3 deskOnly padBot">Acesse esse jogo e outros títulos do Riot Games com o aplicativo Xbox.</p>
  <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph popbuynow deskOnly" target="_blank" aria-label="baixe o aplicativo xbox"> <span>BAIXE O APLICATIVO XBOX</span> </a>
  <p class="c-paragraph-3 deskOnly">Já tem o aplicativo Xbox? <a href="ms-windows-store://pdp/?ProductId=9MV0B5HZVK9Z" data-retailer="ms store" class="poplastbutton win10button" target="_blank" aria-label="inicie o aplicativo na microsoft store">Abra o aplicativo</a> para jogar este título em seu PC com Windows.</p>
  <p class="c-paragraph-3 mobOnly">Baixe e jogue este título no seu PC com Windows usando o <a href="https://www.xbox.com/apps/xbox-app-on-pc" data-cta="learn" class="poplastbutton win10button" target="_blank" aria-label="Saiba mais sobre o aplicativo Xbox no PC">aplicativo Xbox no PC</a>.</p>
</div>

<div class="nonwin10linkriot hide">
  <p class="c-paragraph-3">Baixe e jogue este título no seu PC com Windows usando o <a href="https://www.xbox.com/apps/xbox-app-on-pc" data-cta="learn" class="poplastbutton win10button" target="_blank" aria-label="Saiba mais sobre o aplicativo Xbox no PC">aplicativo Xbox no PC</a>.
  </p>
</div>

<div class="ubisoftlink hide">
  <p class="c-paragraph-3 padBot">Acesse esse jogo e outros títulos do Ubisoft Connect com o aplicativo Xbox.</p>
  <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph popbuynow deskOnly" target="_blank" aria-label="Baixe o aplicativo, baixe o aplicativo do Ubisoft Connect"> <span>BAIXE O APLICATIVO</span> </a>
  <p class="c-paragraph-3 deskOnly">Já tem o aplicativo Xbox? <a href="ms-windows-store://pdp/?ProductId=9MV0B5HZVK9Z" data-retailer="ms store" class="poplastbutton win10button" target="_blank" aria-label="inicie o aplicativo na microsoft store">Abra o aplicativo</a> para jogar este título em seu PC com Windows.</p>
  <p class="c-paragraph-3 mobOnly">Baixe e jogue este título no seu PC com Windows usando o <a href="https://www.xbox.com/apps/xbox-app-on-pc" data-cta="learn" class="poplastbutton win10button" target="_blank" aria-label="Saiba mais sobre o aplicativo Xbox no PC">aplicativo Xbox no PC</a>.</p>
</div> </div><div id="Three Up - Xbox Devices" class="xboxApps" role="none"><div class="banner" data-grid="container">
    <h2 class="c-heading-3 m-banner">Acesse o Xbox Game Pass nos seus dispositivos</h2>
</div>
<div class="m-content-placement theme-white" data-grid="container" id="xbox-apps">
    <div data-grid="col-12 pad-6x stack-2">
        <div data-grid="col-4">
            <section class="m-content-placement-item f-size-large f-precise-click">
                <picture> <img srcset="https://cms-assets.xboxservices.com/assets/13/bd/13bd3aac-cc20-4bc2-86b0-ffd8c00572f6.jpg?n=944198_Content-Placement-0_Xbox-on-PC_788x444.jpg" src="https://cms-assets.xboxservices.com/assets/13/bd/13bd3aac-cc20-4bc2-86b0-ffd8c00572f6.jpg?n=944198_Content-Placement-0_Xbox-on-PC_788x444.jpg" alt="Um notebook mostrando a interface do aplicativo Xbox em um computador Windows."> </picture>
                <div>
                    <h3 class="c-heading">Xbox no PC</h3>
                    <p class="c-paragraph">Descubra, baixe e jogue títulos no seu PC.</p>
                    <a href="https://aka.ms/xboxinstaller" class="c-call-to-action c-glyph appbutton zpt" data-cta="get" aria-label="Obter o aplicativo, baixar e iniciar o aplicativo Xbox para PC"> <span>OBTENHA O APLICATIVO</span> </a> <a href="https://www.xbox.com/apps/xbox-app-on-pc" class="c-call-to-action c-glyph appbutton zpt" data-cta="learn" aria-label="Saiba mais, saiba mais sobre o aplicativo Xbox para PC"> <span>SAIBA MAIS</span> </a>
                </div>
            </section>
        </div>
        <div data-grid="col-4">
            <section class="m-content-placement-item f-size-large f-precise-click">
                <picture> <img srcset="https://cms-assets.xboxservices.com/assets/ea/79/ea791e74-6dfa-4c7f-8f6a-0ad5ba67f1b5.jpg?n=944198_Content-Placement-0_Xbox-mobile_788x444.jpg" src="https://cms-assets.xboxservices.com/assets/ea/79/ea791e74-6dfa-4c7f-8f6a-0ad5ba67f1b5.jpg?n=944198_Content-Placement-0_Xbox-mobile_788x444.jpg" alt="Um celular mostrando a interface do usuário do aplicativo móvel do Xbox."> </picture>
                <div>
                    <h3 class="c-heading">Xbox em dispositivos móveis</h3>
                    <p class="c-paragraph">Receba notificações que alertam quando os novos jogos chegam ao Xbox Game Pass.</p>
                    <div>
                        <a href="https://apps.apple.com/us/app/xbox/id736179781" class="c-call-to-action f-image zpt" aria-label="Baixar o aplicativo Xbox Mobile na App Store da Apple" target="_blank" data-app-retailer="apple"> <img src="https://assets.xboxservices.com/assets/22/65/226530f5-d75a-4f60-83f5-d1a948459e7f.svg?n=Xboxcom_Image-0_Apple-Store-App-Badge_EN-US_120x40.svg" alt="Baixar na Apple App Store"> </a> <a href="https://play.google.com/store/apps/details?id=com.microsoft.xboxone.smartglass&amp;hl" class="c-call-to-action f-image zpt" aria-label="Baixar o aplicativo Xbox para dispositivos móveis no Google Play" target="_blank" data-app-retailer="google"> <img src="https://assets.xboxservices.com/assets/e9/c9/e9c997db-a5e6-4518-9e0d-92a596ccc02a.svg?n=Xboxcom_Image-0_Google-Play-App-Badge_EN-US_135x40.svg" alt="Baixe no Google Play"> </a>
                   </div>
                </div>
            </section>
        </div>
        <div data-grid="col-4">
            <section class="m-content-placement-item f-size-large f-precise-click">
                <picture> <img srcset="https://cms-assets.xboxservices.com/assets/80/9a/809a34d2-e64d-42ad-b0c9-862793974ead.jpg?n=944198_Content-Placement-0_Xbox-cloud-gaming_788x444.jpg" src="https://cms-assets.xboxservices.com/assets/80/9a/809a34d2-e64d-42ad-b0c9-862793974ead.jpg?n=944198_Content-Placement-0_Xbox-cloud-gaming_788x444.jpg" alt="Smart TV exibindo a tela inicial do aplicativo Xbox."> </picture>
                <div>
                    <h3 class="c-heading">Xbox Cloud Gaming</h3>
                    <p class="c-paragraph">Transmita e jogue em qualquer lugar com o Cloud Gaming.</p>
                    <a href="https://www.xbox.com/cloud-gaming" class="c-call-to-action c-glyph appbutton zpt" data-cta="learn" aria-label="Explorar o Cloud Gaming, saber mais sobre Xbox Cloud Gaming"> <span>EXPLORAR O CLOUD GAMING</span> </a>
                </div>
            </section>
        </div>
    </div>
</div></div><div id="Padding" role="none"><div class="m-" data-grid="container"></div></div><div id="Legal" class="legal" role="none"><div class="" data-grid="container" role="region" aria-label="Isenção de responsabilidade: rodapés">
  <div data-grid="col-12 pad-12x stack-2">
    <p class="c-caption-1"><b>Aviso de disponibilidade do Xbox Game Pass:</b></p>
    <p class="c-caption-1">
      Títulos, quantidade, recursos e disponibilidade variam com o tempo, de acordo com a região, com o plano do Xbox Game Pass e a plataforma. Consulte o catálogo de jogos atual em <a class="c-hyperlink white-c" href="https://xbox.com/xbox-game-pass/games">xbox.com/xbox-game-pass/games</a>. Saiba mais sobre as regiões com suporte em <a class="c-hyperlink white-c" href="https://www.xbox.com/regions">xbox.com/regions</a>.
    </p>
<p class="c-caption-1" id="fortniteinfo-PT-BR"><b>*</b> Benefício do Clube Fortnite previsto para ser lançado no Xbox Game Pass Ultimate em novembro de 2025. Disponibilidade sujeita a mudanças. Sujeito a termos.</p>

  <p class="c-caption-1" id="rewardsinfo"><b>† Rewards:</b> termos se aplicam. Conta da Microsoft necessária. Somente em mercados selecionados. Rewards variam de acordo com o plano do Game Pass e o nível do Rewards. Os valores dos pontos variam de acordo com a moeda local, o nível do Rewards e o número de pontos a resgatar. Multiplicadores de pontos comparados ao potencial de ganho no Game Pass Essential. Recompensas de gameplay para maiores de 18 anos. Missões exclusivas somente com planos Premium e Ultimate para títulos na biblioteca do Game Pass. Não inclui jogos para PC que exigem lançadores de terceiros ou jogados no Battlenet.net. Tempo de jogo requerido para todas as missões. Compras qualificadas em Microsoft Store (online ou no Windows ou no console) em Rewards com o Xbox.</p>
  </div>
</div></div><div id="React-MWF-Social-Menu-XGP" class="xboxSocial" role="none"><div class="" data-grid="container">
<div class="m-social f-horizontal f-share social-follow" role="region" aria-label="rodapé de compartilhamento social">
    <span role="heading" aria-level="2">Siga o Game Pass</span>
    <ul>
        <li title="Email">
            <a itemprop="sameAs" aria-label="Entrar em contato com o Xbox" href="https://account.xbox.com/ContactPreferences" target="_new"> <picture> <img src="https://assets.xboxservices.com/assets/f8/67/f86740d7-eedd-4d9c-a963-76af7e36c4b2.svg?n=Xbox-Follow-Footer_Image-0_Mail_32x32_02.svg" alt="Ícone de e-mail"> </picture> </a>
        </li>
        <li title="X">
            <a itemprop="sameAs" aria-label="Compartilhar no X" href="https://twitter.com/xboxgamepass" target="_new"> <picture> <img src="https://assets.xboxservices.com/assets/c9/71/c971845d-5e9d-4f26-8426-b71b9910b183.svg?n=Xbox-Follow-Footer_Image-0_X_32x32_02.svg" alt="Logotipo do X"> </picture> </a>
        </li>
        <li title="Instagram">
            <a itemprop="sameAs" aria-label="Compartilhar no Instagram" href="https://www.instagram.com/xboxgamepass" target="_new"> <picture> <img src="https://assets.xboxservices.com/assets/21/a4/21a47e36-c00c-4fb0-bd18-bc72cfc41e5d.svg?n=Xbox-Follow-Footer_Image-0_Instagram_32x32_02.svg" alt="Logotipo do Instagram"> </picture> </a>
        </li>
    </ul>
    <button class="c-glyph" aria-label="Mostrar links adicionais de redes sociais" aria-hidden="true" data-js-toggle="false"></button>
</div>
</div></div><div id="Custom Back to Top" role="none"><a id="bttbutton" href="#backtotop" class="m-back-to-top" aria-disabled="true" aria-label="voltar ao topo">
  <div class="c-glyph glyph-up"></div>
</a></div><div id="moduleBased-MWF-Script-calls" role="none">


<script>
//hreflang 
$("link[hreflang]").remove();
 var uri = new URL(document.URL);
 var urlRegion = uri.pathname.slice(1,6).toLowerCase();

if (typeof allregions === "undefined") {// if a lmited locale set is not declared locally on an individual page
    var allregions = ["en-us", "en-au", "en-hk", "en-in", "en-nz", "en-sg", "ja-jp", "ko-kr", "zh-hk", "zh-tw", "ar-ae", "ar-sa", "cs-cz", "da-dk", "de-at", "de-ch", "de-de", "el-gr", "en-gb", "en-ie", "en-za", "fi-fi", "fr-be", "fr-ch", "fr-fr", "he-il", "hu-hu", "it-it", "nb-no", "nl-be", "nl-nl", "pl-pl", "pt-pt", "ru-ru", "sk-sk", "sv-se", "tr-tr", "en-ca", "fr-ca", "es-ar", "es-cl", "es-co", "es-es", "es-mx", "pt-br"];
} 

var hlurl = $("meta[property='og:url']").attr("content")
if (hlurl === undefined) {
  hlurl = "https://www.xbox.com/" + urlRegion;
} else {
  hlurl = hlurl.toLowerCase();
}

// Aria Tool
var currentUrl = document.URL.toLowerCase();
if ((currentUrl.indexOf("origin") !== -1) && (currentUrl.indexOf("?aria-tool") !== -1)) {
    $("body").append('<script type="text/javascript" src="/en-US/global-shares/script/js/aria-alt.js"></s' + 'cript>');
}

for (var i = 0; i < allregions.length; i++) {
  var regionpre = allregions[i].split("-")[0];
  var regionpost = allregions[i].split("-")[1].toUpperCase();
  var regionfull = regionpre + "-" + regionpost
  var hllink = hlurl.replace(urlRegion, regionfull);
  $("head").prepend('<link rel="alternate" href="' + hllink + '" hreflang="' + regionfull + '" />');
}

</script>

<!-- Full Path in order to publish -->
<script type="text/javascript" src="https://www.xbox.com/en-US/global-shares/templates/JS/xbox-MWF-2021.js"></script></div><div id="Targeting" role="none"><script>
  xb_tgt = "so"
</script>

<script type="text/javascript" src="/en-US/xbox-game-pass/games/js/targeted-content/xgpcat-SignedOut.json"></script>

<meta name="awa-usersubtype" content="xgp-signedout"></div><div id="Populate Script" role="none"><script type="text/javascript" src="/en-us/xbox-game-pass/games/js/xgpcatPopulate-2025.js"></script></div></div></div></div></div><div class="uhf-footer uhf-footer-mode-full">    <div id="footerArea" class="uhf" data-m="{&quot;cN&quot;:&quot;footerArea&quot;,&quot;cT&quot;:&quot;Area_coreuiArea&quot;,&quot;id&quot;:&quot;a2Body&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;Body&quot;}">
                <div id="footerRegion" data-region-key="footerregion" data-m="{&quot;cN&quot;:&quot;footerRegion&quot;,&quot;cT&quot;:&quot;Region_coreui-region&quot;,&quot;id&quot;:&quot;r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;a2&quot;}">

    <div id="footerUniversalFooter" data-m="{&quot;cN&quot;:&quot;footerUniversalFooter&quot;,&quot;cT&quot;:&quot;Module_coreui-universalfooter&quot;,&quot;id&quot;:&quot;m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;r1a2&quot;}" data-module-id="Category|footerRegion|coreui-region|footerUniversalFooter|coreui-universalfooter">
        



<footer id="uhf-footer" class="c-uhff context-uhf" data-uhf-mscc-rq="false" data-footer-footprint="/XboxComUHF/FullFooter, fromService: True" data-m="{&quot;cN&quot;:&quot;Uhf footer_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;m1r1a2&quot;}">
        <nav class="c-uhff-nav" aria-label="Links de Recursos do Rodapé" data-m="{&quot;cN&quot;:&quot;Footer nav_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1m1r1a2&quot;}">
            
                <div class="c-uhff-nav-row">
                    <div class="c-uhff-nav-group" data-m="{&quot;cN&quot;:&quot;footerNavColumn1_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c1c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">
                        <div class="c-heading-4" role="heading" aria-level="2">Navegue</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Xbox consoles Navegue" class="c-uhff-link" href="https://www.xbox.com/pt-BR/consoles?xr=footnav" data-m="{&quot;cN&quot;:&quot;Xbox consoles_nav&quot;,&quot;id&quot;:&quot;n1c1c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c1c1c1m1r1a2&quot;}">Xbox consoles</a>
                            </li>
                            <li>
                                <a aria-label="Jogos Xbox Navegue" class="c-uhff-link" href="https://www.xbox.com/pt-BR/games?xr=footnav" data-m="{&quot;cN&quot;:&quot;Jogos Xbox_nav&quot;,&quot;id&quot;:&quot;n2c1c1c1m1r1a2&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c1c1c1m1r1a2&quot;}">Jogos Xbox</a>
                            </li>
                            <li>
                                <a aria-label="Xbox Game Pass Navegue" class="c-uhff-link" href="https://www.xbox.com/pt-BR/xbox-game-pass?xr=footnav" data-m="{&quot;cN&quot;:&quot;Xbox Game Pass_nav&quot;,&quot;id&quot;:&quot;n3c1c1c1m1r1a2&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c1c1c1m1r1a2&quot;}">Xbox Game Pass</a>
                            </li>
                            <li>
                                <a aria-label="Acessórios do Xbox Navegue" class="c-uhff-link" href="https://www.xbox.com/pt-BR/accessories?xr=footnav" data-m="{&quot;cN&quot;:&quot;Acessórios do Xbox_nav&quot;,&quot;id&quot;:&quot;n4c1c1c1m1r1a2&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c1c1c1m1r1a2&quot;}">Acessórios do Xbox</a>
                            </li>

                        </ul>
                        
                    </div>
                    <div class="c-uhff-nav-group" data-m="{&quot;cN&quot;:&quot;footerNavColumn2_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c2c1c1m1r1a2&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">
                        <div class="c-heading-4" role="heading" aria-level="2">Recursos</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Notícias do Xbox Recursos" class="c-uhff-link" href="https://news.xbox.com/pt-br/?xr=footnav" data-m="{&quot;cN&quot;:&quot;Notícias do Xbox_nav&quot;,&quot;id&quot;:&quot;n1c2c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c2c1c1m1r1a2&quot;}">Notícias do Xbox</a>
                            </li>
                            <li>
                                <a aria-label="Suporte do Xbox Recursos" class="c-uhff-link" href="https://support.xbox.com?xr=footnav" data-m="{&quot;cN&quot;:&quot;Suporte do Xbox_nav&quot;,&quot;id&quot;:&quot;n2c2c1c1m1r1a2&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c2c1c1m1r1a2&quot;}">Suporte do Xbox</a>
                            </li>
                            <li>
                                <a aria-label="Feedback Recursos" class="c-uhff-link" href="https://aka.ms/xboxideas?xr=footnav" data-m="{&quot;cN&quot;:&quot;Feedback_nav&quot;,&quot;id&quot;:&quot;n3c2c1c1m1r1a2&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c2c1c1m1r1a2&quot;}">Feedback</a>
                            </li>
                            <li>
                                <a aria-label="Padrões da Comunidade Recursos" class="c-uhff-link" href="https://www.xbox.com/pt-BR/legal/community-standards?xr=footnav" data-m="{&quot;cN&quot;:&quot;Padrões da Comunidade_nav&quot;,&quot;id&quot;:&quot;n4c2c1c1m1r1a2&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c2c1c1m1r1a2&quot;}">Padrões da Comunidade</a>
                            </li>
                            <li>
                                <a aria-label="Aviso de potenciais convulsões por fotossensibilidade Recursos" class="c-uhff-link" href="https://support.xbox.com/help/family-online-safety/online-safety/photosensitive-seizure-warning?xr=footnav" data-m="{&quot;cN&quot;:&quot;Aviso de potenciais convulsões por fotossensibilidade_nav&quot;,&quot;id&quot;:&quot;n5c2c1c1m1r1a2&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c2c1c1m1r1a2&quot;}">Aviso de potenciais convulsões por fotossensibilidade</a>
                            </li>

                        </ul>
                        
                    </div>
                    <div class="c-uhff-nav-group" data-m="{&quot;cN&quot;:&quot;footerNavColumn3_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c3c1c1m1r1a2&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">
                        <div class="c-heading-4" role="heading" aria-level="2">Microsoft Store</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Conta Microsoft Microsoft Store" class="c-uhff-link" href="https://account.microsoft.com?xr=footnav" data-m="{&quot;cN&quot;:&quot;Conta Microsoft_nav&quot;,&quot;id&quot;:&quot;n1c3c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c3c1c1m1r1a2&quot;}">Conta Microsoft</a>
                            </li>
                            <li>
                                <a aria-label="Suporte da Microsoft Store Microsoft Store" class="c-uhff-link" href="https://support.microsoft.com/pt-br/account-billing/payment-billing-and-the-microsoft-store-app-help-bdf79f17-1b6c-449c-a7fb-9ba16c7e6db2?xr=footnav" data-m="{&quot;cN&quot;:&quot;Suporte da Microsoft Store_nav&quot;,&quot;id&quot;:&quot;n2c3c1c1m1r1a2&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c3c1c1m1r1a2&quot;}">Suporte da Microsoft Store</a>
                            </li>
                            <li>
                                <a aria-label="Devoluções Microsoft Store" class="c-uhff-link" href="https://support.microsoft.com/pt-BR/account-billing/returning-items-you-bought-from-microsoft-store-for-exchange-or-refund-81629012-aa4f-f48b-2394-8596f415072b?xr=footnav" data-m="{&quot;cN&quot;:&quot;Devoluções_nav&quot;,&quot;id&quot;:&quot;n3c3c1c1m1r1a2&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c3c1c1m1r1a2&quot;}">Devoluções</a>
                            </li>
                            <li>
                                <a aria-label="Rastreamento de pedidos Microsoft Store" class="c-uhff-link" href="https://account.microsoft.com/orders?xr=footnav" data-m="{&quot;cN&quot;:&quot;Rastreamento de pedidos_nav&quot;,&quot;id&quot;:&quot;n4c3c1c1m1r1a2&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c3c1c1m1r1a2&quot;}">Rastreamento de pedidos</a>
                            </li>

                        </ul>
                        
                    </div>
                </div>
                <div class="c-uhff-nav-row">
                    <div class="c-uhff-nav-group" data-m="{&quot;cN&quot;:&quot;footerNavColumn4_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c4c1c1m1r1a2&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">
                        <div class="c-heading-4" role="heading" aria-level="2">Para desenvolvedores</div>
                        <ul class="c-list f-bare">
                            <li>
                                <a aria-label="Jogos Para desenvolvedores" class="c-uhff-link" href="https://developer.microsoft.com/pt-br/games/publish?xr=footnav" data-m="{&quot;cN&quot;:&quot;Jogos_nav&quot;,&quot;id&quot;:&quot;n1c4c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c4c1c1m1r1a2&quot;}">Jogos</a>
                            </li>

                        </ul>
                        
                    </div>
                </div>
        </nav>
    <div class="c-uhff-base">
                <a id="locale-picker-link" aria-label="Seletor de Idioma de Conteúdo. Definido como Português (Brasil)" class="c-uhff-link c-uhff-lang-selector c-glyph glyph-world" href="/Shell/ChangeLocale" data-m="{&quot;cN&quot;:&quot;locale_picker(BR)_nav&quot;,&quot;id&quot;:&quot;n5c1c1m1r1a2&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">Português (Brasil)</a>

            <a data-m="{&quot;id&quot;:&quot;n6c1c1m1r1a2&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}" href="https://aka.ms/yourcaliforniaprivacychoices" class="c-uhff-link c-uhff-ccpa">
        <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 14" xml:space="preserve" height="16" width="43">
            <title>Ícone de recusa de opções de privacidade</title>
            <path d="M7.4 12.8h6.8l3.1-11.6H7.4C4.2 1.2 1.6 3.8 1.6 7s2.6 5.8 5.8 5.8z" style="fill-rule: evenodd; clip-rule: evenodd; fill: rgb(255, 255, 255); --darkreader-inline-fill: var(--darkreader-text-ffffff, #e8e6e3);" data-darkreader-inline-fill=""></path>
            <path d="M22.6 0H7.4c-3.9 0-7 3.1-7 7s3.1 7 7 7h15.2c3.9 0 7-3.1 7-7s-3.2-7-7-7zm-21 7c0-3.2 2.6-5.8 5.8-5.8h9.9l-3.1 11.6H7.4c-3.2 0-5.8-2.6-5.8-5.8z" style="fill-rule: evenodd; clip-rule: evenodd; fill: rgb(0, 102, 255); --darkreader-inline-fill: var(--darkreader-text-0066ff, #339cff);" data-darkreader-inline-fill=""></path>
            <path d="M24.6 4c.2.2.2.6 0 .8L22.5 7l2.2 2.2c.2.2.2.6 0 .8-.2.2-.6.2-.8 0l-2.2-2.2-2.2 2.2c-.2.2-.6.2-.8 0-.2-.2-.2-.6 0-.8L20.8 7l-2.2-2.2c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0l2.2 2.2L23.8 4c.2-.2.6-.2.8 0z" style="fill: rgb(255, 255, 255); --darkreader-inline-fill: var(--darkreader-text-ffffff, #e8e6e3);" data-darkreader-inline-fill=""></path>
            <path d="M12.7 4.1c.2.2.3.6.1.8L8.6 9.8c-.1.1-.2.2-.3.2-.2.1-.5.1-.7-.1L5.4 7.7c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0L8 8.6l3.8-4.5c.2-.2.6-.2.9 0z" style="fill: rgb(0, 102, 255); --darkreader-inline-fill: var(--darkreader-text-0066ff, #339cff);" data-darkreader-inline-fill=""></path>
        </svg>
        <span>Suas opções de privacidade</span>
    </a>

        <noscript>
                <a data-m='{"id":"n7c1c1m1r1a2","sN":7,"aN":"c1c1m1r1a2"}' href="https://aka.ms/yourcaliforniaprivacychoices" class='c-uhff-link c-uhff-ccpa'>
        <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 14" xml:space="preserve" height="16" width="43">
            <title>&#205;cone de recusa de op&#231;&#245;es de privacidade</title>
            <path d="M7.4 12.8h6.8l3.1-11.6H7.4C4.2 1.2 1.6 3.8 1.6 7s2.6 5.8 5.8 5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#fff"/>
            <path d="M22.6 0H7.4c-3.9 0-7 3.1-7 7s3.1 7 7 7h15.2c3.9 0 7-3.1 7-7s-3.2-7-7-7zm-21 7c0-3.2 2.6-5.8 5.8-5.8h9.9l-3.1 11.6H7.4c-3.2 0-5.8-2.6-5.8-5.8z" style="fill-rule:evenodd;clip-rule:evenodd;fill:#06f"/>
            <path d="M24.6 4c.2.2.2.6 0 .8L22.5 7l2.2 2.2c.2.2.2.6 0 .8-.2.2-.6.2-.8 0l-2.2-2.2-2.2 2.2c-.2.2-.6.2-.8 0-.2-.2-.2-.6 0-.8L20.8 7l-2.2-2.2c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0l2.2 2.2L23.8 4c.2-.2.6-.2.8 0z" style="fill:#fff"/>
            <path d="M12.7 4.1c.2.2.3.6.1.8L8.6 9.8c-.1.1-.2.2-.3.2-.2.1-.5.1-.7-.1L5.4 7.7c-.2-.2-.2-.6 0-.8.2-.2.6-.2.8 0L8 8.6l3.8-4.5c.2-.2.6-.2.9 0z" style="fill:#06f"/>
        </svg>
        <span>Suas op&#231;&#245;es de privacidade</span>
    </a>

        </noscript>
            <a data-m="{&quot;id&quot;:&quot;n8c1c1m1r1a2&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}" href="https://go.microsoft.com/fwlink/?linkid=2259814" class="c-uhff-link c-uhff-consumer">
        <span>Privacidade dos Dados de Saúde do Consumidor</span>
    </a>

        <nav aria-label="Links corporativos da Microsoft">
            <ul class="c-list f-bare" data-m="{&quot;cN&quot;:&quot;Corp links_cont&quot;,&quot;cT&quot;:&quot;Container&quot;,&quot;id&quot;:&quot;c9c1c1m1r1a2&quot;,&quot;sN&quot;:9,&quot;aN&quot;:&quot;c1c1m1r1a2&quot;}">
                                <li id="c-uhff-footer_contactus">
                    <a class="c-uhff-link" href="https://support.microsoft.com/pt-br/contactus" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_ContactUs_nav&quot;,&quot;id&quot;:&quot;n1c9c1c1m1r1a2&quot;,&quot;sN&quot;:1,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Entre em contato com a Microsoft</a>
                </li>
                <li id="c-uhff-footer_privacyandcookies">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?LinkId=521839" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_PrivacyandCookies_nav&quot;,&quot;id&quot;:&quot;n2c9c1c1m1r1a2&quot;,&quot;sN&quot;:2,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Privacidade e Cookies</a>
                </li>
                <li class="" id="c-uhff-footer_managecookies">
                    <a class="c-uhff-link" href="#" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_ManageCookies_nav&quot;,&quot;id&quot;:&quot;n3c9c1c1m1r1a2&quot;,&quot;sN&quot;:3,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Gerenciar cookies</a>
                </li>
                <li id="c-uhff-footer_compliance">
                    <a class="c-uhff-link" href="https://www.microsoft.com/pt-br/legal/compliance" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_Compliance_nav&quot;,&quot;id&quot;:&quot;n4c9c1c1m1r1a2&quot;,&quot;sN&quot;:4,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Ética e Compliance</a>
                </li>
                <li id="c-uhff-footer_termsofuse">
                    <a class="c-uhff-link" href="https://go.microsoft.com/fwlink/?LinkID=206977" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_TermsOfUse_nav&quot;,&quot;id&quot;:&quot;n5c9c1c1m1r1a2&quot;,&quot;sN&quot;:5,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Nota Legal </a>
                </li>
                <li id="c-uhff-footer_trademarks">
                    <a class="c-uhff-link" href="https://www.microsoft.com/trademarks" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_Trademarks_nav&quot;,&quot;id&quot;:&quot;n6c9c1c1m1r1a2&quot;,&quot;sN&quot;:6,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Marcas</a>
                </li>
                <li id="c-uhff-third_party_notices">
                    <a class="c-uhff-link" href="https://www.xbox.com/pt-BR/legal/legal-notices" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Third_Party_Notices_nav&quot;,&quot;id&quot;:&quot;n7c9c1c1m1r1a2&quot;,&quot;sN&quot;:7,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Avisos de terceiros</a>
                </li>
                <li id="c-uhff-footer_aboutourads">
                    <a class="c-uhff-link" href="https://choice.microsoft.com" data-mscc-ic="false" data-m="{&quot;cN&quot;:&quot;Footer_AboutourAds_nav&quot;,&quot;id&quot;:&quot;n8c9c1c1m1r1a2&quot;,&quot;sN&quot;:8,&quot;aN&quot;:&quot;c9c1c1m1r1a2&quot;}">Sobre os nossos anúncios</a>
                </li>

                <li>© Microsoft 2025</li>
                
            </ul>
        </nav>
        
    </div>
    
</footer>

<script id="uhf-footer-ccpa">
    const globalPrivacyControlEnabled = navigator.globalPrivacyControl;

    const GPC_DataSharingOptIn = (globalPrivacyControlEnabled) ? false : checkThirdPartyAdsOptOutCookie();

    if(window.onGPCLoaded) {
        window.onGPCLoaded();
    }
    
    function checkThirdPartyAdsOptOutCookie() {
        try {
            const ThirdPartyAdsOptOutCookieName = '3PAdsOptOut';
            var cookieValue = getCookie(ThirdPartyAdsOptOutCookieName);
            return cookieValue != 1;
        } catch {
            return true;
        }
    }

    function getCookie(cookieName) {
        var cookieValue = document.cookie.match('(^|;)s*' + cookieName + 's*=s*([^;]+)');
        return (cookieValue) ? cookieValue[2] : '';
    }
</script>







    </div>
        </div>

    </div>
</div></div></div></div><script>_satellite["_runScript1"](function(event, target, Promise) {
//# sourceURL=CookieStatusInsightswithPageAction
/**
 * Minecraft cookie insight tracker based on siteConsent object.
 *
 * @author    MLSD Tagging & Analytics Team
 * @version   1.1
 */

(function () {
  try {
    var readCookiee = function (name) {
      try {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ')
            c = c.substring(1, c.length);
          if (c.indexOf(nameEQ) === 0)
            return c.substring(nameEQ.length, c.length);
        }
        return null;
      }
      catch (err) {
        console.log("Error: " + err);
      }
    };

    var wcpcheckcount = 0;
    var trackWcpCookieConsent = function () {
      try {
        if (typeof window.siteConsent != "undefined") {
          if (siteConsent.isConsentRequired) {
            var MSCCCookieValuee = readCookiee("MSCC");
            if (MSCCCookieValuee == null) {
              setCCStatuswithPageAction("anlytcs,Ignrd;social,Ignrd;advert,Ignrd");
            }
            else if (MSCCCookieValuee.match(/cid/ig) != null && MSCCCookieValuee.match(/cid/ig).length >= 1) {
              var MSCCCookieSplit = MSCCCookieValuee.split("-");
              var cValues = {};
              var convertVal = { 0: "Ignrd", 1: "Reject", 2: "Accept" }
              for (i = 0; i < MSCCCookieSplit.length; i++) {
                var cVal = MSCCCookieSplit[i].split("=");
                cValues[cVal[0]] = convertVal[cVal[1]];
              }
              var finalVal = "anlytcs," + cValues['c1'] + ";social," + cValues['c2'] + ";advert," + cValues['c3'];
              setCCStatuswithPageAction(finalVal);
            }
            else {
              setCCStatuswithPageAction("CValues Not Present");
            }
          }
          else {
            setCCStatuswithPageAction("MSCC:NR");
          }
        }
        else if (wcpcheckcount < 20) {
          wcpcheckcount++;
          setTimeout(function () { trackWcpCookieConsent() }, 500);
        }
        else if (wcpcheckcount == 20) {
          setCCStatuswithPageAction("siteConsent Object Not Present");
        }
      }
      catch (err) {
        console.log("Error: " + err);
      }
    };

    var setCCStatuswithPageAction = function (CookieStatusInsightsVal) {
      try {
        if (document.querySelector && document.querySelector("meta[name='awa-ver']")) {
          document.querySelector("meta[name='awa-ver']").setAttribute("content", CookieStatusInsightsVal);
        } else {
          var metaa = document.createElement('meta');
          metaa.name = "awa-ver";
          metaa.content = CookieStatusInsightsVal;
          document.getElementsByTagName('head')[0].appendChild(metaa);
        }
        if(window.xbcTelemetry && typeof(xbcTelemetry._webAnalytics.updateCoreDataConfig) == 'function'){
          xbcTelemetry._webAnalytics.updateCoreDataConfig({ pageTags: {metaTags : {ver: CookieStatusInsightsVal}} });
        }
      }
      catch (err) {
        console.log("Error: " + err);
      }
    };
    trackWcpCookieConsent();
  }
  catch (err) {
    console.log("Error: " + err);
  }
}());
});</script>
        <div id="authContainer">

        <!-- JS dependencies to load after content -->
        <script id="__LOADABLE_REQUIRED_CHUNKS__" type="application/json" crossorigin="true">[1096,7243]</script><script id="__LOADABLE_REQUIRED_CHUNKS___ext" type="application/json" crossorigin="true">{"namedChunks":["ContentPage"]}</script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/6305.45931e87.js" crossorigin="true"></script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/4485.a5cc6d8c.js" crossorigin="true"></script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/7442.f799eab2.js" crossorigin="true"></script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/1438.5803057f.js" crossorigin="true"></script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/9363.03b437ae.js" crossorigin="true"></script>
<script async="" data-chunk="client" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/client.ff18c110.js" crossorigin="true"></script>
<script async="" data-chunk="ContentPage" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/1096.7f23b4f9.chunk.js" crossorigin="true"></script>
<script async="" data-chunk="ContentPage" src="https://assets-xbxweb.xbox.com/xbox-web/static/js/ContentPage.4056e4d1.chunk.js" crossorigin="true"></script>

      
  </div><style>.jump-g.jumpganimate.jumpgoffleft {right: 150px;opacity: 0;}.jump-g.jumpganimate {position: relative;transition:700ms all;right:0}</style><style class="darkreader darkreader--sync" media="screen"></style><div class="high-contrast-test" style="color: rgb(153, 153, 153); width: 0px; height: 0px; font-size: 10px; line-height: 1em; --darkreader-inline-color: var(--darkreader-text-999999, #a8a095);" data-darkreader-inline-color=""></div><div style="width:0;height:0;font-size:0;" class="CatAnnounce" aria-live="assertive"></div><script>_satellite["_runScript2"](function(event, target, Promise) {
},e.checkWcpScStatusAndFireFuncInQueue=function(){for(var n=0;n<t.catOrder.length;n++)e.checkConsentStatus(t.catOrder[n])&&e.fireCategoryFunction(t.catOrder[n]);e.checkConsentStatus("analytics")&&e.checkConsentStatus("advertising")&&e.checkConsentStatus("socialmedia")&&(e.fireCategoryFunction("allCategory"),t.category_all_status=!0)},e.dynamicLoadMediaTagsPagesCheck=function(){try{var t=0;return t=window.location.pathname.match(/(en-us|en-ca|en-gb|de-de|fr-ca|fr-fr)windowsbusinesswindows-11-intel-vpro-hybrid-work?/i),Boolean(t)}catch(t){e.debugLog("dynamicLoadMediaTagsPagesCheck error: "+t)}},e.dynamicLoadMediaTagsSetup=function(){try{!e.hasAddedConsentCheckCallbacks&&window.siteConsent.consentChangedCallbacks&&e.dynamicLoadMediaTagsPagesCheck()&&(window.siteConsent.consentChangedCallbacks.callbackArray.push(e.checkCookieConsent),e.hasAddedConsentCheckCallbacks=!0)}catch(t){e.debugLog("dynamicLoadMediaTagsSetup error: "+t)}};var o=function(){try{e.checkSiteConsentObject()?(clearInterval(n),e.checkWcpScStatusAndFireFuncInQueue(),e.dynamicLoadMediaTagsSetup()):t.siteConsentLoopCount>500&&(clearInterval(n),"function"==typeof e.whenSCLoopExceeded&&e.whenSCLoopExceeded()),t.siteConsentLoopCount++}catch(t){e.debugLog("setLoopForSiteConsent error: "+t)}};t.useMSCC=void 0===_satellite.getVar("UseMSCC")||_satellite.getVar("UseMSCC"),e.hasAddedConsentCheckCallbacks=!1,e.goForSiteConsentCheck=function(){try{window.location.hostname.match(/xbox.com/i)&&void 0===window.siteConsent?n=setInterval(o,40):document.querySelectorAll("#primaryArea[data-m]").length>0?(t.category_all_status=!0,e.fireCategoryFunction("allCategory")):e.checkSiteConsentObject()?(e.checkWcpScStatusAndFireFuncInQueue(),e.dynamicLoadMediaTagsSetup()):t.useMSCC?void 0!==window.mscc&&void 0===window.siteConsent?"function"==typeof window.mscc.hasConsent&&window.mscc.hasConsent()?(t.category_all_status=!0,e.fireCategoryFunction("allCategory")):n=setInterval(o,40):void 0===window.mscc&&void 0===window.siteConsent&&(t.category_all_status=!0,e.fireCategoryFunction("allCategory")):n=setInterval(o,40)}catch(t){e.debugLog("goForSiteConsentCheck Error: "+t)}},e.mediaCCPAIntervalCounter=0,e.mediaCCPAIntervalFunction=function(){try{var t=e.getCCPAConsentStatus();null!=t?(clearInterval(e.mediaCCPAInterval),t&&e.goForSiteConsentCheck()):e.mediaCCPAIntervalCounter>500&&clearInterval(e.mediaCCPAInterval),e.mediaCCPAIntervalCounter++}catch(t){e.debugLog("tu.mediaCCPAIntervalFunction Error: "+t)}},e.checkCookieConsent=function(){try{window.location.hostname.match(/amsshop|xboxdesignlab/i)?null!=t.util.readCookie("amcookie_policy_restriction")&&"0"!==t.util.readCookie("amcookie_allowed")||(t.category_all_status=!0,e.fireCategoryFunction("allCategory")):e.SkipCCPACheck()?e.goForSiteConsentCheck():e.mediaCCPAInterval=setInterval(e.mediaCCPAIntervalFunction,10)}catch(t){e.debugLog("checkCookieConsent Error: "+t)}},e.checkCookieConsent()}catch(t){console.error(t)}}(window.wdgtagging,window.wdgtagging.util);
});</script><script>_satellite["_runScript3"](function(event, target, Promise) {
null!=window.wdgtagging&&function(t,a){var e,o,g,n,c,s;e="www.xbox.com"===(s=window.location.host)||"xboxdesignlab.xbox.com"===s||"gear.xbox.com"===s||"dreamscape.xbox.com"===s||"arcadecontest.xbox.com"===s?"prod":"test";var i=window.location.pathname.toLowerCase().split("/"),l=1;if((o=i[l])?o.match(/^..-.*-..$/)?(g=o.split("-")[0],n=o.split("-")[2]):o.match(/^..-.*$/)?(g=o.split("-")[0],n=o.split("-")[1]):(g="",n=""):(g="",n=""),"xboxdesignlab.xbox.com"===s||"gear.xbox.com"===s){if(l=2,"homepage"!=(c=a.tlcStr(i[l],"homepage")))for(l++;l<i.length;)c+="/"+i[l],l++}else if(l+=1,"homepage"!==(c=a.tlcStr(i[l],"homepage"))){for(l++;l<i.length;)c+="/"+i[l],l++;c=a.tlcStr(c).replace(/[-_]/g," ")}"arcadecontest.xbox.com"!==s&&"msxboxspacejamsweeps.gmrpreprod.com"!==s||t.setData("pageType",a.getMetaTagContent("gmr-pagetype")),t.setData("env",e),t.setData("langLoc",o),t.setData("lang",g),t.setData("loc",n),t.setData("gpn",c)}(window.wdgtagging,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript4"](function(event, target, Promise) {
null!==window.wdgtagging&&function(t,a,e){try{if(!window.location.pathname.match(/searchresults/i))return;e("div[role=main]").attr({"data-bi-area":"body","data-bi-id":"a3Body","data-bi-name":"mainContent"}),e(document).on("mousedown","div[class*=CollectionPromo-module] a",(function(){try{var t=e(this).parents("div[class*=CollectionPromo-module__contentContainer]");t.length&&t.attr({"data-bi-name":"banner-module","data-module-id":"true"});var n=e(this).attr("class");n&&(n=n.split(" ")[0]),e(this).attr({"data-bi-ecn":"banner-cta","data-bi-id":n})}catch(t){a.debugLog("mousedown on banner error: "+t)}})),e(document).on("mousedown","div[class*=SortAndFilters-module__container]:not([data-bi-name])",(function(){try{e(this).attr({"data-bi-name":e(this).attr("class").split(" ")[0],"data-module-id":"true"})}catch(t){a.debugLog("mousedown filter panel section error: "+t)}})),e(document).on("mousedown","button[aria-expanded]",(function(){try{a.tagGenericName(e(this));var t="EXPAND";"true"==e(this).attr("aria-expanded")&&(t="REDUCE"),e(this).attr("data-bi-bhvr",t)}catch(t){a.debugLog("mousedown button aria-expanded error: "+t)}})),e(document).on("mousedown","button[aria-checked]",(function(){try{a.tagGenericName(e(this));var t="APPLY";"true"==e(this).attr("aria-checked")&&(t="REMOVE"),e(this).attr("data-bi-bhvr",t)}catch(t){a.debugLog("mousedown button aria-checked error: "+t)}})),e(document).on("mousedown","div[class*=StackFilters-module__container] button",(function(){try{a.tagGenericName(e(this)),e(this).attr("data-bi-bhvr","REMOVE")}catch(t){a.debugLog("mousedown button on stackfilters container error: "+t)}})),a.tagButtonNameInSearchTilesSection=function(t){try{if(a.tagGenericName(e(t)),e(t).attr("data-bi-name"))return;var n=e(t).attr("title")||e(t).attr("aria-label");e(t).attr("data-bi-name",n)}catch(t){a.debugLog("tagButtonNameInSearchTilesSection error: "+t)}},e(document).on("mousedown","div[class*=SearchTabs-module__tabsWrapper]:not([data-bi-name])",(function(){try{e(this).attr({"data-bi-name":"SearchTabs-module-tabsWrapper","data-module-id":"true"})}catch(t){a.debugLog("mousedown SearchTabs Wrapper error: "+t)}})),e(document).on("mousedown","div[class*=SearchTabs-module] button",(function(){a.tagButtonNameInSearchTilesSection(this)})),e(document).on("mousedown","div[class*=SearchTabs-module] a",(function(){try{e("div[class*=SearchTabs-module] button:not([data-bi-name])").each((function(){a.tagButtonNameInSearchTilesSection(this)}));var t=e(this).parents("div[class*=SearchTabs-module]"),n=t.find("button[class*=_activeTab]").attr("data-bi-name");if(!n)return;var o=t.find("div[class*=SearchTabs-module__tabContainer]").first();n+="_tab",o.attr("data-bi-name",n)}catch(t){a.debugLog("mousedown search tab section error: "+t)}}))}catch(t){a.debugLog("Search Result page script error: "+t)}}(window.wdgtagging,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript5"](function(event, target, Promise) {
null!=window.wdgtagging&&function(a,e){var t=window.location.pathname,r=window.location.hostname;e.getRandomNumber=function(){return 1e13*(Math.random()+"")};try{if(r.match(/xbox.com/gi)){var o=function(){window.addEventListener("message",(function(a){try{if(a.origin&&"https://www.microsoft.com"!==a.origin)return;if(a.data&&a.data.message&&a.data.status&&a.data.orderId&&a.data.orderInfo&&a.data.orderInfo.orderState&&a.data.orderInfo.lineItems&&a.data.orderInfo.lineItems[0].totalRetailPrice&&"done"==a.data.message&&"success"==a.data.status&&"Purchased"==a.data.orderInfo.orderState)try{var r=a.data.orderId,o=a.data.orderInfo.lineItems[0].totalRetailPrice;t.match(/(en-us|es-mx|en-au|en-ca|fr-ca|en-gb|pt-br|ja-jp|de-de|fr-fr)/i)&&(t.match(/xbox-game-pass/i)||t.match(/xbox-game-pass(ultimate|core|pc-game-pass)/i)||t.match(/gamesea-play/i)||t.match(/cloud-gaming/i))&&e.requestImage("https://pixel.everesttech.net/px2/4249?px_evt=t&ev_Xbox_Purchases="+o+"&ev_transid="+encodeURIComponent(r))}catch(a){e.debugLog("Error tagging Adobe pixel on purchase complete. Error: "+a)}}catch(a){e.debugLog("Error Tagging XGP Purchase Complete Adobe Tag. Error: "+a)}}),!1)};a.catCheckAllExecuteOrPush(o)}}catch(a){e.debugLog("Error tagging Xbox Game Pass - "+a)}}(window.wdgtagging,window.wdgtagging.util);
});</script><script>_satellite["_runScript6"](function(event, target, Promise) {
null!==window.wdgtagging&&function(t,a,e){try{var n=!1,o=setInterval((function(){var a=e(document).find("#csInv");if(a.length>0&&e(a).is(":visible")&&0!=e(a).css("opacity")){clearInterval(o),n=!0;var r={actionType:"O",behavior:"SURVEYINITIATE",uri:location.href,pageName:t.getData("gpn"),contentTags:{contentName:"comscore-survey-overlay",areaName:"body"}};window.owap.capturePageAction(null,r)}}),1e3);setTimeout((function(){n||clearInterval(o)}),6e4),e(document).on("mouseover","#csInv:not('[data-module-id]')",(function(){var t=this;e(t).attr({"data-bi-area":"body","data-bi-name":"comscore-survey-overlay","data-bi-id":e(t).attr("id")||"","data-module-id":"comscore-survey-overlay"})})),e(document).on("mousedown","#csInv a, #csInv button, #csInv input[type='button'].srInvButtons",(function(){var t=this;if(a.tagGenericName(e(t)),!e(t).attr("data-bi-name")){var n=a.etlcStr(e(t).attr("value"),"")||a.etlcStr(e(t).attr("title"),"")||"";e(t).attr("data-bi-name",n)}e(t).attr({"data-bi-area":"body","data-bi-id":e(t).attr("id")||""})}))}catch(t){a.debugLog("Error in comscore survey overlay tagging. Error: "+t)}}(window.wdgtagging,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript7"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(e,a,t){a.lineage={main_sel:"MAIN",zone_id:"a3",sec_custom_sel:"",grp_custom_sel:"",pnl_custom_sel:"",subpnl_custom_sel:"",exclude_sec_sel:""},t.isDebug=!1,a.lineageSetupCounter=1,"1"===t.readCookie("debug")?t.isDebug=t.readCookie("debug"):location.search.indexOf("debug=1")>-1&&(t.isDebug=!0),t.lineageDebug=function(e){t.isDebug&&console.log(e)},t.lineageDebug("OneDS Core Lineage Start"),t.getLineageName=function(e,a){return e.attr("data-lineage-name")||e.attr("data-productid")||e.attr("data-bigid")||e.attr("data-id")||e.attr("data-vg")||e.attr("id")||a},t.resetLineageName=function(e){e.attr("data-bi-name")&&e.attr("data-bi-id")&&e.attr("data-bi-name")==e.attr("data-bi-id")&&e.attr("data-bi-name",null)},t.setLineageSection=function(e,i,n,s){s=s||!1;var l="r"+n+i;t.resetLineageName(e),e.attr("data-bi-id",l),e.attr("data-bi-name")&&!s||!t.getLineageName(e)||e.attr("data-bi-name",t.getLineageName(e));var g="DIV[data-grid*=col-12],DIV[data-grid*=col-10],SECTION[data-grid*=col-12],SECTION[data-grid*=col-10],SECTION[data-bi-area=body]"+a.lineage.grp_custom_sel,u=1;t.lineageDebug("Setup Lineage Groups Start:"+e.children(g).length),e.children(g).each((function(){t.setLineageGroup(jQuery(this),l,u,s),u++})),t.lineageDebug("Setup Lineage Groups End")},t.setLineageGroup=function(e,i,n,s){s=s||!1;var l="m"+n+i;t.resetLineageName(e),e.attr("data-bi-id",l),e.attr("data-bi-name")&&!s||!t.getLineageName(e)||e.attr("data-bi-name",t.getLineageName(e));var g,u="DIV,SECTION"+a.lineage.pnl_custom_sel,r=1;t.lineageDebug("Setup Lineage Panels Start:"+e.children(u).length),e.children(u).each((g=l,function(){r=t.setLineagePanel(jQuery(this),g,r,s)})),t.lineageDebug("Setup Lineage Panels End")},t.setLineagePanel=function(e,a,i,n){var s,l;if(n=n||!1,l=i,e.is("[data-grid='col-12 stack-2']"))jQuery("[data-grid*='col-6 pad-'] [data-grid=col-6], [data-grid*='col-4 pad-'] [data-grid=col-12], [data-grid='col-12 stack-2'] [data-grid='col-4 pad-6x'],[data-grid*='col-3']",e).each((function(){s="c"+l+a,t.resetLineageName(jQuery(this)),jQuery(this).attr("data-bi-id",s),jQuery(this).attr("data-bi-name")&&!n||!t.getLineageName(jQuery(this))||jQuery(this).attr("data-bi-name",t.getLineageName(jQuery(this))),t.setLineageSubPanel(jQuery(this),s,n),l++})),jQuery(e).children("section").each((function(){s="c"+l+a,t.resetLineageName(jQuery(this)),jQuery(this).attr("data-bi-id",s),jQuery(this).attr("data-bi-name")&&!n||!t.getLineageName(jQuery(this),jQuery(this).attr("data-bi-id"))||jQuery(this).attr("data-bi-name",t.getLineageName(jQuery(this),jQuery(this).attr("data-bi-id"))),t.setLineageSubPanel(jQuery(this),s,n),l++}));else if(e.is("[data-grid='col-12 pad-6x stack-2']"))jQuery("[data-grid=col-6]",e).each((function(){s="c"+l+a,t.resetLineageName(jQuery(this)),jQuery(this).attr("data-bi-id",s),jQuery(this).attr("data-bi-name")&&!n||!t.getLineageName(jQuery(this))||jQuery(this).attr("data-bi-name",t.getLineageName(jQuery(this))),t.setLineageSubPanel(jQuery(this),s,n),l++}));else{var g;if(s="c"+i+a,t.resetLineageName(e),e.attr("data-bi-id",s),e.attr("data-bi-name")&&!n||!t.getLineageName(e)||e.attr("data-bi-name",t.getLineageName(e)),e.hasClass("f-stacked"))l=1,e.children("DIV,SECTION").each((function(){g="c"+l+s,t.resetLineageName(jQuery(this)),jQuery(this).attr("data-bi-id",g),jQuery(this).attr("data-bi-name")&&!n||!t.getLineageName(jQuery(this))||jQuery(this).attr("data-bi-name",t.getLineageName(jQuery(this))),t.setLineageSubPanel(jQuery(this),g,n),l++}));else t.setLineageSubPanel(e,s,n);i++}return i},t.setLineageSubPanel=function(e,i,n){n=n||!1;var s,l,g=1;e.children("DIV,SECTION,UL,LI").each(function(e){return function(){s=e,((l=jQuery(this)).is("LI")||(!l.attr("data-bi-name")||n)&&t.getLineageName(l)||l.is(a.lineage.subpnl_custom_sel))&&(l.attr("data-bi-name",t.getLineageName(l)),!l.attr("data-bi-id")||n?(s="c"+g+e,l.attr("data-bi-id",s)):s=l.attr("data-bi-id")),t.setLineageSubPanel(l,s,n),g++}}(i))},a.initLineage=function(e){e&&"object"==typeof e&&(e.main_sel&&(a.lineage.main_sel=e.main_sel),e.zone_id&&(a.lineage.zone_id=e.zone_id),e.sec_custom_sel&&(a.lineage.sec_custom_sel.length>0&&e.sec_custom_sel.length>0&&(a.lineage.sec_custom_sel+=","),a.lineage.sec_custom_sel+=e.sec_custom_sel),e.grp_custom_sel&&(a.lineage.grp_custom_sel.length>0&&e.grp_custom_sel.length>0&&(a.lineage.grp_custom_sel+=","),a.lineage.grp_custom_sel+=e.grp_custom_sel),e.pnl_custom_sel&&(a.lineage.pnl_custom_sel.length>0&&e.pnl_custom_sel.length>0&&(a.lineage.pnl_custom_sel+=","),a.lineage.pnl_custom_sel+=e.pnl_custom_sel),e.subpnl_custom_sel&&(a.lineage.subpnl_custom_sel.length>0&&e.subpnl_custom_sel.length>0&&(a.lineage.subpnl_custom_sel+=","),a.lineage.subpnl_custom_sel+=e.subpnl_custom_sel),e.exclude_sec_sel&&(a.lineage.exclude_sec_sel.length>0&&e.exclude_sec_sel.length>0&&(a.lineage.exclude_sec_sel+=","),a.lineage.exclude_sec_sel+=e.exclude_sec_sel)),a.lineage.sec_custom_sel=(a.lineage.sec_custom_sel.length>0?",":"")+a.lineage.sec_custom_sel,a.lineage.grp_custom_sel=(a.lineage.grp_custom_sel.length>0?",":"")+a.lineage.grp_custom_sel,a.lineage.pnl_custom_sel=(a.lineage.pnl_custom_sel.length>0?",":"")+a.lineage.pnl_custom_sel,a.lineage.exclude_sec_sel?a.lineage.sec_sel="section:not("+a.lineage.exclude_sec_sel+"),DIV[data-grid=container]:not("+a.lineage.exclude_sec_sel+"),DIV[data-vg]:not("+a.lineage.exclude_sec_sel+")"+a.lineage.sec_custom_sel:a.lineage.sec_sel="section,DIV[data-grid=container],DIV[data-vg]"+a.lineage.sec_custom_sel},a.lineageDOMReady=function(){return jQuery(a.lineage.main_sel).length>0&&jQuery(a.lineage.main_sel).children(a.lineage.sec_sel).length>0},a.setupLineage=function(e){try{if(a.lineageDOMReady()&&a.lineageSetupCounter<61){t.lineageDebug("Setup Lineage Start");var i=jQuery(a.lineage.main_sel),n=1;jQuery(a.lineage.main_sel).attr("data-bi-id",a.lineage.zone_id+"Body"),jQuery(a.lineage.main_sel).attr("data-bi-name",t.getLineageName(jQuery(a.lineage.main_sel),"mainContent")),i.find("[data-lineage-name]:not([data-bi-name])").each((function(){jQuery(this).attr("data-bi-name",jQuery(this).attr("data-lineage-name"))})),t.lineageDebug("Setup Lineage Sections Start:"+jQuery(a.lineage.main_sel).children(a.lineage.sec_sel).length),jQuery(a.lineage.main_sel).children(a.lineage.sec_sel).each((function(){t.setLineageSection(jQuery(this),a.lineage.zone_id,n),n++})),t.lineageDebug("Setup Lineage Sections End"),i.find("[data-bi-id]:not([data-bi-name])").each((function(){jQuery(this).attr("data-bi-name",jQuery(this).attr("data-bi-id"))})),"function"==typeof e&&e.apply(),t.lineageDebug("Setup Lineage End")}else a.lineageSetupCounter++,a.lineageSetupCounter>240?"function"==typeof e&&e.apply():setTimeout((function(){a.setupLineage(e)}),500),t.lineageDebug("Setup Lineage : LineageDOMReady false")}catch(e){console.error("Setup Lineage Error:"+e)}},t.lineageDebug("OneDS Core Lineage End")}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript8"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t){var n=[];if(jQuery("[id*='ContentBlockList']").each((function(){try{jqthis=jQuery(this),jqthis.find("a").length>0&&jqthis.not("[data-sec]")&&(jqthis.find("[id*='ContentBlockList']").length>0?jqthis.find("[id*='ContentBlockList']").each((function(){jQuery(this).find("a, button").length<=0&&n.push(jqthis)})):n.push(jqthis)),jqthis.find("button").length>0&&jqthis.not("[data-sec]")&&(jqthis.find("[id*='ContentBlockList']").length>0?jqthis.find("[id*='ContentBlockList']").each((function(){jQuery(this).find("a, button").length<=0&&n.push(jqthis)})):n.push(jqthis))}catch(n){t.debugLog("Error in ms.index setting on ContentBlockList elements. Error: "+n)}})),n.length>0)try{jQuery(n).each((function(){jQuery(this).attr("data-sec","")}))}catch(n){t.debugLog("Error assigning data-sec inside panelIndexArray iteration. Error: "+n)}}(window.wdgtagging.util,window.wdgtagging.oneds,window.jQuery));
});</script><script>_satellite["_runScript9"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,e,i){var o,n,d,s,c,l=location.pathname;if(i("#bodycolumn>div[id='BodyContent']").length){var m={main_sel:"#BodyContent>DIV",zone_id:"a3",sec_custom_sel:"[data-sec],[id*='ContentBlockList_'].drawer,[id*='TopContentBlockList_'],.e49-wrapper,.bottomBGImage,.gameFeatureFullWidth,.bottomBG,.theme-black",grp_custom_sel:".m-hero,.mosaic-container,.m-hero-item,[id^='ContentBlockList_'],[data-grid='container'],.gameSection,.featuredgames,[id^='ContentBlockList_'] > div,.c-drawer > [data-grid='container'],.c-drawer,.custom-e49-nav,.m-multi-hero",pnl_custom_sel:".m-global-promotion,.m-product-placement-item,.m-panes-product-placement-item,section.f-stacked,.m-product-placement,section.m-content-placement-item,.c-drawer-toggle,.c-drawer > [data-grid='container'],.show-desktop,.CTAdiv,#stealth-carousel,.reg,.game-pass-pivot .c-pivot ul",subpnl_custom_sel:".m-product-placement-item,[data-grid] .m-content-placement-item,.single-controller,.gameDivsWrapper,.m-panes,[data-dealtypes],[data-dealnumber],.m-panes-product-placement-item,section.f-stacked > div,[data-grid],.sku-chooser__panel,.m-panes section,.c-carousel,.c-carousel > div,.c-carousel ul,.purchaseButtons,.c-drawer-toggle,.m-feature,.stealth-sub-carousel,.stealth-sub-carousel-panel,.theme-dark, #formUser, #success-box, #FailedMsg,.animate__animated,.form-section,.game-pass-pivot .c-pivot ul li",exclude_sec_sel:""};0===i("#BodyContent").length&&i("SECTION.body>DIV").length>0?m.main_sel="SECTION.body>DIV":0===i("#BodyContent").length&&(m.main_sel="SECTION.body"),window.location.pathname.match(/..-..play/i)&&0===i("#BodyContent").length&&i("#bodycolumn").length>0&&(m.main_sel="#bodycolumn>DIV[role='main']")}else m={main_sel:"#bodycolumn>div",zone_id:"a3",sec_custom_sel:"div, section",grp_custom_sel:"div.buybox, .pageBarNavWrap, section[class='m-hero-item']>div, .m-banner, div[class='gamesSection']>div, .m-hero-item, #gettingstarted, .zpt, #accessories, div[id*='Two']>div, .faq-mwf, .legal>div, #MWF-Social-Menu-XGP>div",pnl_custom_sel:"nav[class='c-in-page-navigation'],.m-content-placement-item,.high-contrast, .m-banner, .c-carousel, section[class='m-hero-item']>div, .customfourscootup, .zpt, .m-content-placement, .c-drawer, .c-group, .m-social",subpnl_custom_sel:".c-navigation-menu, .CTAdiv, .c-group, .c-carousel>div, section[class='m-hero-item']>div>div, .m-content-placement, .content-copy, .content-copy>div>div, .zpt,.XgpImmersiveSkuModule-module__details___2WJRb, .XgpImmersiveSkuModule-module__price___1Si4f, .m-content-placement>div, .m-content-placement>div>div",exclude_sec_sel:"div[id='moduleBased-shared-head-content']"};a.postLineage=function(){i("#bodycolumn a, #bodycolumn button, SECTION.body a, SECTION.body button, .xgp-modal a, .xgp-modal button, #PageContent a,#PageContent button").not("[data-bi-id]").each((function(){(s=i(this)).attr("data-bi-id")||(o=s.parents("[data-bi-id]:first")).length>0&&(n=o.find("a[data-bi-id],button[data-bi-id]").not(o.find("[data-bi-id] a[data-bi-id],[data-bi-id] button[data-bi-id]")),c=(o.attr("data-bi-id")||"").replace(/a(*)Body/g,"a$1"),n.length>0&&(d=n.length)&&d>0?s.attr("data-bi-id","n"+(d+1)+c):s.attr("data-bi-id","n1"+c))}))};var r=window.location.pathname;r.match(/jumpingames(crackdown-3|metro-exodus|devil-may-cry-5|kingdom-hearts-3|division-2)?/gi)&&(m.sec_custom_sel+=",[id*='ContentBlockList_']",m.grp_custom_sel+=",.ms-draggable,.buy-bar,.gh-allup,.legal-footer,#little-hand-container",m.pnl_custom_sel+=",.ms-draggable-area,DIV",m.subpnl_custom_sel+=",.ms-draggable-hotspot-container,DIV,[data-host],.modal-pad,.modal-columns,.social,.c-carousel,li"),location.pathname.match(/wallpapers/gi)&&(m.pnl_custom_sel+=",.m-content-placement",m.subpnl_custom_sel+=",.viewer-content"),l.match(/promotionssummer-spotlight/gi)&&(m.sec_custom_sel+=",[id*='TopContentBlockList_'],[id*='ContentBlockList_']",m.pnl_custom_sel+=".gameDivLink,.gameMoreInfo",m.subpnl_custom_sel+=",.popinfo,.popupShow"),l.match(/jumpin/i)&&(m.sec_custom_sel+=",.mosaic",m.grp_custom_sel+=",.pt12,[data-grid*='col-12 stack-2']",m.pnl_custom_sel+=",.pt12,[data-grid],.zoomImg",m.subpnl_custom_sel+=",.pt12,.zoomImg,[data-grid]"),l.match(/community?/gi)&&(m.grp_custom_sel+=",[data-grid],.gamer-spotlight,.mixer-events-buffer,.events,.behind-scenes,.ambassador,.videoverlay",m.pnl_custom_sel+=",.triptych__box,[data-grid],#Stealth-Carousel,.mosaic__limit,.m-ambient-video",m.subpnl_custom_sel+=",.mobile-third,.triptych__panel,.mixer__top-games,.no-mobile,.mosaic__element,.video__content,.ambassador__social,[data-grid],.icon-break,.stealth-sub-carousel-panel,.triptych__poster,.triptych__content,.triptych__video,.triptych__details"),r.match(/livegold?/gi)&&(m.grp_custom_sel+=",.m-image-intro"),r.match(/gamessea-of-thieves?/gi)&&(m.grp_custom_sel+=",.BGimgintro",m.pnl_custom_sel+=",.m-hero-item,#whatsnew",m.subpnl_custom_sel+=",.c-pivot,.media-gallery-black,.m-product-placement"),(r.match(/gamesid/gi)||r.match(/..-..xbox-oneaccessoriescontrollerselite-wireless-controller-series-2/gi)||r.match(/games(devil-may-cry-5|dragon-ball-fighterz)?/gi))&&(m.sec_custom_sel+=",[id^='ContentBlockList_']",m.grp_custom_sel+=",[id^='ContentBlockList_']> div",m.pnl_custom_sel+=",.m-,div",m.subpnl_custom_sel+=",section,div"),(r.match(/developers/gi)||r.match(/xbox-app/gi))&&(m.grp_custom_sel+=",[id^='ContentBlockList_'] > div,.xgp-modal div[role*=dialog]",m.pnl_custom_sel+=",.m-content-placement-item,.xgp-modal div[role*=document], .high-contrast",m.subpnl_custom_sel+=",div,section"),r.match(/promotionsvisit-xbox/gi)&&(m.grp_custom_sel+=",#ContentBlockList_1 div",m.pnl_custom_sel+=",three-up, div > hero, div three-sixty,div enhanced,div locations,div postcard,div games,div gamepass,upsell",m.subpnl_custom_sel+=",.theme-black,.theme-dark,div,section"),l.match(/liveyear-in-reviewhome/gi)&&(m.sec_custom_sel+=",[id^='ContentBlockList']",m.grp_custom_sel+=",#__nuxt",m.pnl_custom_sel+=",#__layout,.yir-global",m.subpnl_custom_sel+=",SECTION,.builder-globe__container,.yir-global,.yir-globe-builder,.yir-globe-outer"),window.location.href.match(/livegold?/i)&&(m.sec_custom_sel+=",[id^='ContentBlockList']"),r.match(/promotionssalessales-and-specials/gi)&&(m.sec_custom_sel+=",[id^='ContentBlockList_']"),r.match(/xbox-one-x?$/gi)&&(m.sec_custom_sel+=",[id*='ContentBlockList_']",m.grp_custom_sel+=",section",m.pnl_custom_sel+=",DIV"),r.match(/de-depromotionscontrol-your-discount?$/gi)&&(m.sec_custom_sel+=",[id*='ContentBlockList_'],[id*='dialog-cyd-game'] [aria-label='Lightbox'], [data-move]"),l.match(/gamesgears-5/gi)&&(m.sec_custom_sel+=",.bigbackground",m.grp_custom_sel+=",[id*='ContentBlockList_']"),location.pathname.match(/gamesminecraft/gi)&&(m.pnl_custom_sel+=",[data-grid='container'] > div",m.subpnl_custom_sel+=",[data-grid='container'] > div > section, [data-grid='container'] > div > section > div, [data-grid='container'] > div > section > div > section"),location.hostname.match(/arcadecontest.xbox.com|msxboxspacejamsweeps.gmrpreprod.com/i)&&(m.main_sel+=",body>.container",m.sec_custom_sel+=",.column,.promo-image",m.grp_custom_sel+=",.contentContainer,.column-content",m.pnl_custom_sel+=",.logo,.iframe-container,.contentBlock,.column-content,.seperator",m.subpnl_custom_sel+=",.form-content"),location.pathname.match(/play/i)&&(m.sec_custom_sel+=",DIV[role='main']>DIV",m.grp_custom_sel+=",[data-grid='container'],[data-grid*='col-12'],.banner-background",m.pnl_custom_sel+=",.m-banner"),r.match(/xbox-game-passpc-game-passtrial-offer/gi)&&(m.main_sel+=",#bodycolumn>DIV",m.sec_custom_sel+=",.theme-black, [class*='Jalisco']",m.grp_custom_sel+=",.theme-black div[data-grid='container']",m.pnl_custom_sel+=",DIV"),r.match(/2023recap/gi)&&(m.main_sel+=",#PageContent>DIV",m.sec_custom_sel+=",.YearInReviewPage-module__yir-wrapper___QB0uc",m.grp_custom_sel+=",.TopModule-module__non-engagement-top-module-container___5nmvG",m.pnl_custom_sel+=",.YearInReviewPage-module__yir-generic-container___rQRrM",m.subpnl_custom_sel+=",.TopModule-module__header-cta___Tw6kG"),a.initLineage(m),a.setupLineage(a.postLineage);var g="#bodycolumn a:not([data-bi-id]), #bodycolumn button:not([data-bi-id]),SECTION.body a:not([data-bi-id]), SECTION.body button:not([data-bi-id]),#PageContent a:not([data-bi-id]), #PageContent button:not([data-bi-id])";if(i(document).on("mousedown",g,(function(){a.postLineage()})),r.match(/jumpingames(crackdown-3|metro-exodus|devil-may-cry-5|kingdom-hearts-3|division-2)?/gi)&&i("#mainModal").on("mousedown touchstart",(function(){var t=i("li.f-active .modal-heading").length>0?i("li.f-active .modal-heading").text()+" : "+i("li.f-active .modal-heading").attr("template"):i(".modal-heading").text()+" : "+i(".modal-heading").attr("template");i(this).attr("data-bi-name",e.tlcStr(t))})),i("[data-mgt-container]").each((function(){i(this).attr({"data-bi-name":i(this).attr("data-mgt-container"),"data-module-id":"set"})})),i("[data-mgt-panel]").each((function(){i(this).attr("data-bi-name",i(this).attr("data-mgt-panel"))})),i(document).on("mouseenter","[id*='ContentBlockList'] DIV:not([data-bi-id]), [id*='ContentBlockList'] SECTION:not([data-bi-id]), [id*='TopContentBlockList'] DIV:not([data-bi-id]), [id*='TopContentBlockList'] SECTION:not([data-bi-id]), [id*='dialog-cyd-game'] [aria-label='Lightbox'] DIV:not([data-bi-id]), [id*='dialog-cyd-game'] [aria-label='Lightbox'] SECTION:not([data-bi-id])",(function(){try{var t,a,l=i(this).parents("[data-bi-id]:first"),m=l.attr("data-bi-id");m.match(/^r([0-9]*)a/i)?(t=m.match(/^r([0-9]*)a/i)[1],window.wdgtagging.util.setLineageSection(l,window.wdgtagging.oneds.lineage.zone_id,t,!0)):m.match(/^m([0-9]*)r/i)?(t=(a=m.match(/^m([0-9]*)(r.*)/i))[1],window.wdgtagging.util.setLineageGroup(l,a[2],t,!0)):m.match(/^c([0-9]*)m/i)?(t=(a=m.match(/^c([0-9]*)(m.*)/i))[1],window.wdgtagging.util.setLineagePanel(l,a[2],t,!0)):m.match(/^c([0-9]*)c/i)&&(a=m.match(/^c([0-9]*)(c.*)/i),window.wdgtagging.util.setLineageSubPanel(l,"c"+a[1]+a[2],!0)),l.find("a,button").removeAttr("data-bi-id"),l.find("a,button").each((function(){(s=i(this)).attr("data-bi-id")||(o=s.parents("[data-bi-id]:first")).length>0&&(n=o.find("a[data-bi-id],button[data-bi-id]").not(o.find("[data-bi-id] a[data-bi-id],[data-bi-id] button[data-bi-id]")),c=(o.attr("data-bi-id")||"").replace(/a(*)Body/g,"a$1"),n.length>0&&(d=n.length)&&d>0?s.attr("data-bi-id","n"+(d+1)+c):s.attr("data-bi-id","n1"+c))})),l.attr("data-bi-name")&&l.attr("data-bi-name").match(/r([0-9]*)a([0-9])/i)&&l.attr("data-bi-name",null),!l.attr("data-bi-name")&&null!=l.attr("data-bi-id")&&e.getLineageName(l,l.attr("data-bi-id"))&&l.attr("data-bi-name",e.getLineageName(l,l.attr("data-bi-id"))),l.find("[data-bi-id]").each((function(){(i(this).is("a")||i(this).is("button"))&&e.tagGenericName(jQuery(this)),jQuery(this).attr("data-bi-name")&&jQuery(this).attr("data-bi-name").match(/r([0-9]*)a([0-9])/i)&&jQuery(this).attr("data-bi-name",null),!jQuery(this).attr("data-bi-name")&&null!=jQuery(this).attr("data-bi-id")&&e.getLineageName(jQuery(this),jQuery(this).attr("data-bi-id"))&&jQuery(this).attr("data-bi-name",e.getLineageName(jQuery(this),jQuery(this).attr("data-bi-id")))}))}catch(t){e.debugLog("lineage Setting error"+t)}})),window.location.href.match(/xbox-app/gi)){if(i("#xbox-app-modal").not("[data-bi-id]")){var u,p=i("div[data-bi-id='a3Body']:last").attr("data-bi-id");c=(p||"").replace(/a(*)Body/g,"a$1"),u=(d=i("#bodycolumn [data-bi-id]:last").attr("data-bi-id").match(/r(.*)a/))&&d[1]?parseInt(d[1],10)+1:1,i("#xbox-app-modal").attr("data-bi-name",e.getLineageName(i(this),"xbox-app-modal")),e.setLineageSection(i("#xbox-app-modal"),m.zone_id,u)}i(document).on("mouseover",".xgp-modal a, .xgp-modal button",(function(){s=i(this),(o=s.parents("[data-bi-id]:first")).length>0&&(n=o.find("a[data-bi-id],button[data-bi-id]").not(o.find("[data-bi-id] a[data-bi-id],[data-bi-id] button[data-bi-id]")),c=(o.attr("data-bi-id")||"").replace(/a(*)Body/g,"a$1"),n.length>0&&(d=n.length)&&d>0?s.attr("data-bi-id","n"+(d+1)+c):s.attr("data-bi-id","n1"+c))}))}i(document).ready((function(){var t="#dialog-cyd-game, [data-move], .gameMoreInfo";i(document).on("mouseenter",t,(function(){if(window.location.href.match(/promotionscontrol-your-discount/gi)||window.location.href.match(/xbox-game-pass/gi)){if(i(t).not("[data-bi-id]")){var a,l=i("div[data-bi-id='a3Body']:last").attr("data-bi-id");c=(l||"").replace(/a(*)Body/g,"a$1"),a=(d=(i("#bodycolumn [data-bi-id]:last").attr("data-bi-id")||"").match(/r(.*)a/))&&d[1]?parseInt(d[1],10)+1:1,i(t).attr("data-bi-name",e.getLineageName(i(this),"xbox-overlay")),e.setLineageSection(i(t),m.zone_id,a)}i(document).on("mouseover","#dialog-cyd-game a, #dialog-cyd-game button, [data-move] a, [data-move] button, .gameMoreInfo a, .gameMoreInfo button",(function(){s=i(this),(o=s.parents("[data-bi-id]:first")).length>0&&(n=o.find("a[data-bi-id],button[data-bi-id]").not(o.find("[data-bi-id] a[data-bi-id],[data-bi-id] button[data-bi-id]")),c=(o.attr("data-bi-id")||"").replace(/a(*)Body/g,"a$1"),n.length>0&&(d=n.length)&&d>0?s.attr("data-bi-id","n"+(d+1)+c):s.attr("data-bi-id","n1"+c))}))}}))})),window.location.href.match(/promotionssalessales-and-specials/gi)&&i(document).on("mouseenter",".gameDivsWrapper:not([data-bi-id])",(function(){try{var t=i(this).parents("[id*='ContentBlockList_']"),a=t.attr("data-bi-id");if("r"===a[0]){var o=".gameDivsWrapper"+window.wdgtagging.oneds.lineage.grp_custom_sel,n=1;t.children(o).each(function(t){return function(){n=window.wdgtagging.util.setLineageGroup(jQuery(this),t,n)}}(a))}}catch(t){e.debugLog("lineage Setting error"+t)}})),(window.location.href.match(/livegold?/i)||window.location.href.match(/promotionssalessales-and-specials/gi))&&i(document).on("mouseenter",".gameDivsWrapper > .m-product-placement-item:not([data-bi-id])",(function(){try{var t=i(this).parents(".gameDivsWrapper"),a=t.attr("data-bi-id");if("m"===a[0]){var o=".gameDiv"+window.wdgtagging.oneds.lineage.pnl_custom_sel,n=1;t.children(o).each(function(t){return function(){n=window.wdgtagging.util.setLineagePanel(jQuery(this),t,n)}}(a))}}catch(t){e.debugLog("lineage Setting error"+t)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript10"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,e,o){o("#BodyContent,.m-page-bar").attr("data-bi-area","body"),e.getActionType=function(t){var a;return 1==t.which?a="CL":2==t.which?a="CM":3==t.which?a="CR":13==t.which&&(a="KE"),a},e.actItemStringInLightbox=function(t){try{var a=o(t).find("ul li.selected");return a.length?e.tlcStr(a.first().text(),"none"):"none"}catch(t){return e.debugLog("Error on actItemStringInLightbox:"+t),"none"}},e.actItemStringToLineageInLightbox=function(t){try{var a=e.actItemStringInLightbox(t);o(t).find("[role=dialog]").attr("data-bi-name",a)}catch(t){e.debugLog("Error on actItemStringToLineageInLightbox"+t)}},e.tagLightboxArea=function(){try{if(!o(".c-dialog").length)return;o(".c-dialog").each((function(){try{o(this).attr("data-bi-area","body"),o(this).hasClass("hatchDialog")?o(this).attr("data-bi-name","getHatch-lightbox"):o(this).attr("data-bi-name","lightbox"),o(this).attr("data-module-id","lightbox")}catch(t){e.debugLog("Error on lightbox foreach function: "+t)}e.actItemStringToLineageInLightbox(this)})),o(document).on("mousedown",".c-dialog a, .c-dialog button",(function(){try{var t=o(this).parents(".c-dialog").first();e.actItemStringToLineageInLightbox(t)}catch(t){e.debugLog("Error on mousedown in lightbox: "+t)}}))}catch(t){e.debugLog("Error on tagLightboxArea: "+t)}},e.tagLightboxArea(),window.location.pathname.match(/xbox-game-pass/i)&&o(document).on("mouseenter",".gameMoreInfo",(function(){o(this).find("a, button").attr("data-bi-area","body")})),window.location.pathname.match(/liveyear-in-review/i)&&(o("a.cta-login:not([data-bi-bhvr])").attr("data-bi-bhvr","SIGNIN"),setTimeout((function(){if(getCookie("xbox_info")){var t={actionType:"O",content:{contentName:"LoginSuccessful"},behavior:"REGISTRATIONCOMPLETE"};window.owap.captureContentUpdate(t)}}),500));window.location.hostname;var n=window.location.pathname;e.tagChooseContentType=function(t){return t.find("img").length>0||t.find("picture").length>0?"image":i(t,"class","glyph-play")&&(t.find("span").length<=0||i(t.find("span"),"class","screen-reader"))||i(t,"class","mscom-popup-close|m-back-to-top|video_pp_button|ps-lightbox-close")||t.is("button")?"button":"text"};var i=function(t,a,e){var n=o(t),i=new RegExp(e,"i");return n.attr(a)&&n.attr(a).match(i)};e.tagGenericName=function(t){try{if(t.find("h3").length>0&&o.trim(t.find("h3").first().text()).length>0)t.attr("data-bi-name",e.etlcStr(o.trim(t.find("h3").first().text()),"undefined"));else if(t.children().length>1&&o.trim(t.children().first()[0].textContent).length>0)t.attr("data-bi-name",e.etlcStr(o.trim(t.children().first()[0].textContent),"undefined"));else if(o.trim(t[0].textContent).length>0)t.find("noscript").length>0?t.attr("data-bi-name",e.etlcStr(e.excludeSelector(t,"noscript").text(),"undefined")):t.attr("data-bi-name",e.etlcStr(t.text(),"undefined"));else if(t.find("img[alt]").length>0)t.attr("data-bi-name",e.etlcStr(t.find("img[alt]").first().attr("alt"),"img"));else if(t.is("button[role=tab]")&&!t.find("span").length){var a=t.attr("aria-controls")||t.attr("title")||t.attr("aria-label");t.attr("data-bi-name",e.etlcStr(a,"tab"))}}catch(t){e.debugLog("Error tagging data-bi-name(link text) in the common tagging script. Error: "+t)}};var r="a:not([data-m] a), .location-block a.mt-3:not([data-bi-name]),a#signIn,button:not([data-m] button)";if(o(document).on("mousedown",r,(function(){try{e.tagGenericName(o(this));var t=o(this).closest("[data-promo-card]");if(t){var a=t.attr("data-bi-slot"),n=t.attr("data-bi-hn");o(this).attr({"data-bi-slot":a,"data-bi-hn":n})}}catch(t){e.debugLog("Error calling the tagGenericName function in the mousedown listener in the common tagging script. Error: "+t)}})),o(document).on("mousedown",".showMoreText",(function(){try{o(this).attr({"data-bi-name":e.etlcStr(o(this).text(),"a")})}catch(t){e.debugLog("Error calling the tagGenericName function in the mousedown listener in the common tagging script. Error: "+t)}})),o(document).on("mousedown","#BodyContent  A[href*='account.xbox.com/Account/Signin'],#BodyContent A[href*='auth/msa?action=logIn&returnUrl'], #headerArea A[href*='auth/msa?action=logIn&returnUrl'], #bodycolumn A[href*='account.xbox.com/account/signin'],#bodycolumn A[href*='auth/msa?action=logIn&returnUrl'],#bodycolumn A[href*='login.live.com'],#bodycolumn A[href*='signup.live.com']",(function(){o(this).attr("data-bi-area","body"),o(this).attr("data-bi-bhvr","SIGNIN")})),o(document).on("mousedown",".consoleFilterButton a,.heroTabControls a",(function(){o(this).attr("data-bi-bhvr","APPLY")})),o(document).on("mousedown",".showMore",(function(){try{var t=o(".gameDiv:not(:visible)").length>0?"EXPAND":"REDUCE";o(this).attr({"data-bi-name":e.etlcStr(o(this).text(),"button"),"data-bi-bhvr":t})}catch(t){e.debugLog("Error calling the tagGenericName function in the mousedown listener in the common tagging script. Error: "+t)}})),o(document).on("mousedown",".showLess",(function(){try{o(this).attr({"data-bi-name":e.etlcStr(o(this).text(),"button"),"data-bi-bhvr":"REDUCE","data-bi-type":e.tagChooseContentType(o(this))})}catch(t){e.debugLog("Error calling the tagGenericName function in the mousedown listener in the common tagging script. Error: "+t)}})),o(document).on("mousedown",".faq-mwf button",(function(){o(this).attr("aria-expanded").match(/true/)?o(this).attr("data-bi-bhvr","REDUCE"):o(this).attr("aria-expanded").match(/false/)&&o(this).attr("data-bi-bhvr","EXPAND"),o(this).attr("data-bi-type",e.tagChooseContentType(o(this)))})),o(document).on("mousedown",".paginateprevious A,.f-previous,#Stealth-Carousel .left-arrow, .slick-slider .glyph-chevron-left.slick-arrow,.art-prev, .slick-prev, .swiper-button-prev",(function(){try{var t="prev";if(o(this).attr({"data-bi-bhvr":"NAVIGATIONBACK","data-bi-name":t,"data-bi-type":e.tagChooseContentType(o(this))}),!o(this).is("a")&&!o(this).is("button")){var a={actionType:"CL"};window.owap.capturePageAction(this,a)}}catch(t){e.debugLog("Error tagging Navigation prev data: "+t)}})),o(document).on("mousedown",".paginatenext A,.f-next,#Stealth-Carousel .right-arrow, .slick-slider .glyph-chevron-right.slick-arrow,.art-next, .slick-next, .swiper-button-next",(function(){try{var t="next";if(o(this).attr({"data-bi-bhvr":"NAVIGATIONFORWARD","data-bi-name":t,"data-bi-type":e.tagChooseContentType(o(this))}),!o(this).is("a")&&!o(this).is("button")){var a={actionType:"CL"};window.owap.capturePageAction(this,a)}}catch(t){e.debugLog("Error tagging Navigation next data: "+t)}})),o(document).on("mousedown",".glyph-pause",(function(){o(this).attr({"data-bi-name":"pause","data-bi-type":e.tagChooseContentType(o(this))})})),o(document).on("mousedown",".glyph-play,#playPause",(function(){var t;t=o("#playPause").length>0?o(this).hasClass("state-pause")?"play":"pause":"play",o(this).attr({"data-bi-name":t,"data-bi-type":e.tagChooseContentType(o(this))})})),(n.match(/promotionsvoyage/gi)||n.match(/promotionsthe-quest/gi))&&o(document).on("mousedown",".m-feature A:not(A[href*='store'])",(function(){o(this).attr("data-bi-type",e.tagChooseContentType(o(this)))})),e.filterSel=null,setTimeout((function(){o(document).on("click",".catCheck:not(input[type='checkbox'])",(function(){try{var t=o(this);if(t.attr("data-bi-type","option"),t.attr("data-bi-name")||t.attr("data-bi-name",e.etlcStr(o(this).next("SPAN").text())),e.filterSel!=t.attr("data-bi-name")){var a={actionType:"CL",behavior:t.is(":checked")?"APPLY":"REMOVE"};window.owap.capturePageAction(this,a),e.filterSel=t.attr("data-bi-name")}}catch(t){e.debugLog("Error tagging behavior for Checkboxes section. Error: "+t)}}))}),3e3),o(document).on("mousedown",".m-hero a, .m-hero button, .m-hero [data-js-href]",(function(){try{var t=o(this).parents(".m-hero"),a=t.find("li.f-active").attr("id");t.attr("data-bi-name",a)}catch(t){e.debugLog("Error on adding Hero for lineage: "+t)}})),o(document).on("mousedown","[data-js-href]",(function(t){var a,n,i=o(this).attr("data-js-href");if(o(this).find("a[href]").each((function(){if(n=o(this).attr("href"),i==n)return a=o(this),!1})),a||(a=o(this).find("a.c-call-to-action[href]").length>0?o(this).find("a.c-call-to-action[href]").first():o(this).find("a[href]").first()),a){e.tagProdName(a),e.tagProdSkuId(a),e.tagGenericName(a),"undefined"===a.attr("data-bi-name")?o(this).attr("data-bi-name",e.etlcStr(o(this).find("img").attr("alt"),"undefined")):o(this).attr("data-bi-name",a.attr("data-bi-name")),o(this).attr("data-bi-id")||o(this).attr("data-bi-id",a.attr("data-clickname")||a.attr("data-bi-id")||""),a.attr("data-bi-prtnm")||e.tagPartnerLinks(a),a.attr("data-bi-prtnm")||e.tagPartnerName(a),o(this).attr("data-bi-slot")||o(this).attr("data-bi-slot",a.closest("li").attr("data-bi-slot")),o(this).attr("data-bi-hn")||o(this).attr("data-bi-hn",a.closest("li").attr("data-bi-hn"));var r=a.attr("href")||"";r.match(/(microsoft|xbox).com/i)&&r.match(/((store|p|d))/gi)||r.match(/(microsoft|xbox).com..-..configure/i)?a.attr({"data-bi-bhvr":"PARTNERREFERRAL","data-bi-prtnm":"ms store"}):a.attr("href").match(/support.xbox.com/i)&&a.attr("data-bi-bhvr","COMMUNITY"),o(this).attr({"data-bi-bhvr":a.attr("data-bi-bhvr"),"data-bi-prtnm":a.attr("data-bi-prtnm"),"data-bi-prtid":a.attr("data-bi-prtid"),"data-bi-product":a.attr("data-bi-product"),"data-bi-sku":a.attr("data-bi-sku"),"data-bi-prod":a.attr("data-bi-prod"),"data-bi-type":"image"})}if(o(t.target).closest("a").is("a")||o(t.target).is("a")||o(t.target).closest("button").is("button")||o(t.target).is("button")||o(t.target).hasClass("addtocolcheckbox"))t.preventDefault();else{var c={targetUri:o(this).attr("data-js-href"),actionType:"CL"};window.owap.capturePageAction(this,c)}})),o(document).on("mousedown","ul[role='tablist'] li[role='tab']",(function(){try{var t=o("span",this).text()||o(this).text();t=e.tlcStr(t,"undefined"),o(this).attr("data-bi-name",t)}catch(t){e.debugLog("mousedown tablist error: "+t)}})),o(document).on("mousedown","li[role='tab']",(function(t){if(o(t.target).closest("a").is("a")||o(t.target).is("a")||o(t.target).closest("button").is("button")||o(t.target).is("button")||o(t.target).hasClass("addtocolcheckbox"))t.preventDefault();else{var a=o(this).attr("data-bi-name");a&&"undefined"!==a||e.tagGenericName(o(this)),o(this).attr("data-bi-type",e.tagChooseContentType(o(this)));var n={actionType:"CL"};window.owap.capturePageAction(this,n)}})),o(document).on("mousedown","button[role='tab'], .m-back-to-top",(function(){e.tagGenericName(o(this)),o(this).attr("data-bi-name")||(o(this).attr("title")?o(this).attr("data-bi-name",o(this).attr("title")):o(this).attr("aria-controls")?o(this).attr("data-bi-name",o(this).attr("aria-controls")):o(this).attr("data-bi-name","toggle"))})),o(document).on("mousedown",".c-menu-item",(function(t){if(o(this).attr({"data-bi-type":"option","data-bi-name":e.etlcStr(o(this).find("span").text()),"data-bi-bhvr":"APPLY"}),o(t.target).closest("a").is("a")||o(t.target).is("a")||o(t.target).closest("button").is("button")||o(t.target).is("button"))t.preventDefault();else{var a={actionType:"CL"};window.owap.capturePageAction(this,a)}})),o(document).on("mousedown",".c-refine-item",(function(){o(this).attr("data-bi-type","option"),o(this).hasClass("f-selected")?o(this).attr("data-bi-bhvr","REMOVE"):o(this).attr("data-bi-bhvr","APPLY")})),o(document).on("mousedown",".c-drawer>.c-glyph, #BodyContent a[aria-expanded], #BodyContent button[aria-expanded]",(function(){o(this).attr("data-bi-type",e.tagChooseContentType(o(this))),o(this).attr("data-bi-name",e.etlcStr(o(this).text())),"false"==o(this).attr("aria-expanded")?o(this).attr("data-bi-bhvr","EXPAND"):o(this).attr("data-bi-bhvr","REDUCE")})),o(document).on("mousedown",".c-select-menu",(function(){o(this).find("button").attr("data-bi-name",e.etlcStr(o(this).find("button").text()))})),o(document).on("mousedown","a.glyph-cancel,button.glyph-cancel",(function(){o(this).attr("data-bi-bhvr","REMOVE")})),(n.match(/..-..xbox-one-x/gi)||n.match(/promotions/gi))&&(o(document).on("mousedown",".glyph-add, .glyph-cancel, .glyph-remove, a.white-c",(function(){if(!o(this).attr("data-bi-name")){var t=o(this).attr("aria-label")||o(this).text();o(this).attr("data-bi-name",e.etlcStr(t)),e.tagGenericName(o(this))}})),o(document).on("mousedown",".glyph-add",(function(){o(this).attr("data-bi-bhvr","EXPAND")})),o(document).on("mousedown",".glyph-cancel, .glyph-remove",(function(){o(this).attr("data-bi-bhvr","REDUCE")}))),e.tagInputElem=function(t){try{if(!o(t).attr("data-bi-name")){var a=o(t).attr("value")||o(t).attr("name")||o(t).text()||e.etlcStr(o.trim(o(t).next("span").text()))||"";o(t).attr({"data-bi-name":a})}if(o(t).attr("id")){var n=o(t).attr("id");o(t).attr("data-bi-id",n)}var i="APPLY";o(t).is(":checkbox")&&(i=o(t).is(":checked")?"REMOVE":"APPLY"),o(t).attr({"data-bi-type":"option","data-bi-bhvr":i})}catch(t){e.debugLog("Error tagging behavior for Checkboxes section. Error: "+t)}},e.tagInputForEach=function(){o("input:checkbox, input:radio").each((function(){e.tagInputElem(this)}))},e.tagInputForEach(),o(document).on("click","input:checkbox, input:radio",(function(){e.tagInputElem(this)})),o(document).on("mousedown","[class*=modal]",(function(){e.tagInputForEach()})),o(".showMoreText[role*='button']").on("mousedown",(function(){o(".faqMore").hasClass("hiddenFaq")?o(this).attr("data-bi-bhvr","EXPAND"):o(this).attr("data-bi-bhvr","REDUCE")})),o(".single-controller").each((function(){var t=o(this).find(".c-heading-4").text()||"";t&&o(this).attr("data-bi-name",t)})),o(document).on("mouseenter",".single-controller",(function(){var t=o(this).find(".c-heading-4").text()||"";t&&o(this).attr("data-bi-name",t)})),o("a.fb").attr({"data-bi-bhvr":"SOCIALSHARE","data-bi-name":"facebook"}),o("a.tw").attr({"data-bi-bhvr":"SOCIALSHARE","data-bi-name":"twitter"}),o(document).on("mousedown",".zoomImg[data-js-dialog-show]",(function(t){if(o(this).attr({"data-bi-type":"image","data-bi-name":e.etlcStr(o(this).find("[alt]").attr("alt"))}),o(t.target).closest("a").is("a")||o(t.target).is("a")||o(t.target).closest("button").is("button")||o(t.target).is("button"))t.preventDefault();else{var a={actionType:"CL"};window.owap.capturePageAction(this,a)}})),e.setSocialLike=function(t){try{var a;if(t.href&&t.href.length&&(a=t.href.match(/(instagram|facebook|twitter|tiktok|youtube|snapchat|linkedin|whatsapp.comchannel|weibo.com|space.bilibili.com|weixin.qq.com|twitch.tv|x.comxbox|x.comgearsofwar|www.x.com)/i)),a){var n=a[0];o(t).attr({"data-bi-socchn":n,"data-bi-bhvr":"SOCIALLIKE"})}}catch(t){e.debugLog("Error tagging sociallike behavior. Error: "+t)}},o(document).on("mousedown",".socialBanner a, .social-follow a, .m-feature .m-social a, .iconBlade .icons a, .social-icons a, .c-group-logo .m-image-logo a, .social-media-icons .social-text a,.m-social a, .social-section .icons a, .mosaic__item a[href*='instagram.com/xbox']",(function(){e.setSocialLike(this)})),(n.match(/community?/gi)||n.match(/e3?/gi))&&(o(document).on("mousedown",".triptych__panel",(function(){if(!o(this).hasClass("expanded")){var t={behavior:"EXPAND",contentTags:{contentName:o(this).find("img").attr("alt")}};window.owap.capturePageAction(this,t)}})),o(document).on("mousedown",".community__social-links a,.ambassador__social a,.iconBlade .icons a,.mosaic A[href*='instagram'], .heroSocial a, .waysToView a, .featureCal a",(function(){(o(this).attr("href").match(/instagram.com/i)||o(this).attr("href").match(/twitter.com/i)||o(this).attr("href").match(/mixer.com/i)||this.href.match(/youtube.com/i)||this.href.match(/facebook.com?/i)||this.href.match(/twitch.tv?/i)||this.href.match(/mixer.com?/i))&&o(this).attr({"data-bi-socchn":this.hostname.replace("www.","").replace(".com",""),"data-bi-bhvr":"SOCIALLIKE"})})),o(".m-product-placement .m-product-placement-item a, .featureCal .c-group a").each((function(){var t=e.etlcStr(this.href.split("/")[2]);o(this).attr({"data-bi-bhvr":"PARTNERREFERRAL","data-bi-prtnm":t})}))),o(document).on("mousedown",".glyph-cancel:not([data-bi-name]), [class*=closeContainer] button",(function(){o(this).attr({"data-bi-name":"close"})})),(n.match(/xbox-one-x?/)||n.match(/promotions/gi)||n.match(/gamesfortnite-welcome/gi))&&(o(".c-pivot A[role='tab'], .c-pivot li[role='tab'], li[role='tab'], a.slider-block").each((function(){o(this).attr("data-bi-name")||e.tagGenericName(o(this))})),o(document).on("mousedown",".c-pivot A[role='tab'], .c-pivot li[role='tab'], #whatsnew li[role='tab']",(function(){o(this).attr("data-bi-name")||e.tagGenericName(o(this))}))),n.match(/promotionssales/gi)&&o(document).on("mousedown",".popupShow A:not([data-bi-name])",(function(){var t=e.etlcStr(o(this).text())||e.tagGenericName(this);o(this).attr("data-bi-name",t)})),n.match(/xbox-game-pass?/)&&(o(".sku-chooser a").each((function(){try{o(this).attr("data-bi-source",e.getProductInfo(this).id)}catch(t){}})),o(document).on("mousedown",".sku-chooser a",(function(){try{o(this).attr("data-bi-source")||o(this).attr("data-bi-source",e.getProductInfo(this).id)}catch(t){}}))),o(document).on("mousedown",".m-content-placement-item A[href*='twitter']:not([data-bi-bhvr]),.m-content-placement-item A[href*='facebook']:not([data-bi-bhvr])",(function(){o(this).attr({"data-bi-socchn":this.hostname.replace("www.","").replace(".com",""),"data-bi-bhvr":"SOCIALLIKE"})})),n.match(/(..-.*)games/gi)&&o(document).on("mousedown",".f-size-large a[data-js-dialog-show]",(function(){if(o(this).find("img")){var t=o(this).find("img").attr("alt")||o(this).find("span").text();t=e.etlcStr(t),o(this).attr("data-bi-name",t)}})),o(document).on("mousedown","#headerArea  A[href*='account/signin']#mectrl_main_trigger",(function(){var t=o(this).attr("aria-label")||"signin",a=JSON.parse(o(this).parents("#meControl").attr("data-m"));a.bhvr="SIGNIN",a.cN=e.etlcStr(t),o(this).attr("data-m",JSON.stringify(a))})),o(document).on("mousedown","#headerArea  a#mectrl_body_signOut",(function(){var t="signout",a=JSON.parse(o(this).parents("#meControl").attr("data-m"));a.bhvr="SIGNOUT",a.cN=e.etlcStr(t),o(this).attr("data-m",JSON.stringify(a))})),o(document).on("keypress","form.xghsearch [type='search']:not([data-search-initiate-ods])",(function(){o(this).attr("data-search-initiate-ods",!0);var t={behavior:"SEARCHINITIATE",actionType:"O",contentTags:{contentName:"Search bar",areaName:"body"}};window.owap.capturePageAction(null,t)})),e.odssearchTrack=function(t){try{var a,n;a="Search bar",n=(n=o(t).parents("form.xghsearch").find("[type='search']")).attr("value")||n.val(),o(t).attr({"data-bi-bhvr":"SEARCH","data-bi-name":a,"data-bi-srchtype":"manual","data-bi-srchq":n}),window.owap.capturePageAction(t,{actionType:"OTHER"})}catch(t){e.debugLog("Search Tracking not working "+t)}},o(document).on("mousedown","form.xghsearch button[name='search-button']:not([data-search-initiate-ods])",(function(){o(this).attr("data-bi-mto","true"),e.odssearchTrack(this)})),o(document).on("keypress","form.xghsearch [type='search']",(function(t){"13"==(t.keyCode?t.keyCode:t.which)&&e.odssearchTrack(this)})),o(document).on("mousedown","#lbclosebutton",(function(){var t={behavior:"REDUCE",contentTags:{contentName:"close button",areaName:"body"}};window.owap.capturePageAction(null,t)})),o(document).on("mousedown",".cards__content button",(function(){e.tagGenericName(o(this).closest("a"));var t=o(this).closest("a").attr("data-bi-name");o(this).attr("data-bi-name",t)})),n.match(/..-..xbox-oneaccessoriescontrollerselite-wireless-controller-series-2/gi)||n.match(/..-..accessoriescontrollerselite-wireless-controller-series-2/gi)||n.match(/..-..accessoriescontrollersxbox-elite-wireless-controller-series-2-core/gi)||n.match(/..-..promotionsvisit-xbox/gi)||n.match(/..-..accessoriesheadsetsxbox-wireless-headset/gi)||n.match(/accessoriesheadsetsstarfield-limited-edition/gi)){var c=function(t){try{var a={actionType:"CL",uri:location.href};window.owap.capturePageAction(t,a)}catch(t){e.debugLog("Error on rotating image function: "+t)}};o(document).on("click mousedown touchend","img#rotatorImage, .pano-slider img.pano-image",(function(){try{if(!o(this).attr("data-bi-name")){var t=o(this).attr("alt")||o(this).attr("id")||"";o(this).attr("data-bi-name",t)}c(this)}catch(t){e.debugLog("Error on rotating image: "+t)}})),o(document).on("mousedown touchend","#slider360, .pano-slider input.slider",(function(){try{if(!o(this).attr("data-bi-name")){var t=o(this).attr("aria-label")||o(this).val()||"";o(this).attr("data-bi-name",t)}o(this).attr("data-bi-type",e.tagChooseContentType(o(this))),c(this)}catch(t){e.debugLog("Error on rotating image based on input event: "+t)}})),o(document).on("mousedown","ul.pano-nav li a",(function(){var t=o(this).parent("li").index()+1;o(this).attr("data-bi-name","slide-"+t)}))}if(o(document).on("mousedown","a[href*='support.xbox.com'], a[href*='support.microsoft.com']",(function(){o(this).attr("data-bi-bhvr","COMMUNITY")})),o(document).on("mousedown","a[href*='compass-ssl.xbox.com'], a[href*='assets.xboxservices.com/assets']",(function(){(o(this).attr("href")||"").match(/.exe|.pdf|.ics|.zip/i)&&o(this).attr("data-bi-bhvr","DOWNLOAD")})),window.location.pathname.match(/xbox-one-x?$/gi)&&o(document).on("click","input.slider",(function(){var t={actionType:"CL",behavior:"OTHER",uri:location.href,contentTags:{contentName:o(this).attr("aria-label"),areaName:"body"}};window.owap.capturePageAction(this,t)})),o(document).on("mousedown",".OttoGallery",(function(){try{e.tagGenericName(o(this))}catch(t){e.debugLog("Error while tagging content Name to .OttoGallery element. Error: "+t)}})),o('[id*="ContentBlockList_"]').each((function(){try{e.getLineageName(o(this))&&o(this).attr("data-bi-name",e.getLineageName(o(this))),o(this).attr("data-bi-name")&&o(this).attr("data-module-id","true")}catch(t){e.debugLog("Error on container name set up on contentblocklist. Error: "+t)}})),o(document).on("mousedown","[id*='ContentBlockList_']:not([data-bi-name])",(function(){try{e.getLineageName(o(this))&&o(this).attr("data-bi-name",e.getLineageName(o(this))),o(this).attr("data-bi-name")&&o(this).attr("data-module-id","true")}catch(t){e.debugLog("Error on container name set up on contentblocklist. Error: "+t)}})),o(document).on("mousedown",".Modal-module__modalContent___WdkIT button, .Modal-module__modalContent___WdkIT a",(function(){try{e.tagGenericName(o(this)),o(this).parents(".Modal-module__modalContent___WdkIT").attr({"data-bi-name":"ContextualStoreModal","data-module-id":"true"})}catch(t){e.debugLog("Error while tagging contextual modal container name. Error: "+t)}})),e.tagDraggableImage=function(t){try{var a=!1;o(t).on({mousedown:function(){a=!1},mousemove:function(){a=!0},mouseup:function(){try{var t=a;if(a=!1,t){var n=o(this).find("img[alt]").length>0?"Dragged: "+o(this).find("img").attr("alt"):"";o(this).attr("data-bi-name",n);var i={actionType:"CL",behavior:"0",contentTags:{contentName:n}};window.owap.capturePageAction(this,i)}}catch(t){e.debugLog("Draggable Carousel Picture Tagging on mousemove Error: "+t)}}})}catch(t){e.debugLog("Draggable Carousel Picture Tagging Error: "+t)}},e.draggableImageSectors=".c-carousel li picture:not(li[id*=dark] picture)",e.tagDraggableImage(e.draggableImageSectors),window.location.pathname.match(/promotionsHalo-Masterpiece/gi)&&window.location.hostname.match(/xbox.com/i)&&o(document).on("mousedown",'#myModal a[onclick="closeModal()"]',(function(){var t="close";o(this).attr("data-bi-name",t)})),0===o("#bodycolumn>div[id='BodyContent']").length){try{o("#bodycolumn > div > *").each((function(){var t=o(this).attr("id")||o(this).attr("class").split(" ").shift();o(this).attr({"data-bi-name":t,"data-module-id":"true"})}))}catch(t){e.debugLog("Error on container name setup on Cloud Gaming"+t)}try{o(document).on("mousedown","#bodycolumn > div > *:not([data-module-id])",(function(){var t=o(this).attr("id")||o(this).attr("class").split(" ").shift();o(this).attr({"data-bi-name":t,"data-module-id":"true"})}))}catch(t){e.debugLog("Error on container name setup on new page structure: "+t)}o("#bodycolumn").attr("data-bi-area","body")}if(n.match(/promotionspower-her-dreams/i))try{o(document).on("mouseover",".c-checkbox",(function(){e.tagInputForEach()}))}catch(t){e.debugLog("Error on checkbox tagging on power her dreams page: "+t)}if(location.pathname.match(/family-hubchild-account/gi))try{o(document).on("mousedown",".m-rich-content-block li a",(function(){var t=o(this).closest("[data-grid]").find(".c-heading-5").text()||"";t.length>0&&o(this).closest("[data-grid]").attr("data-bi-name",t)}))}catch(t){e.debugLog("Error on adding content name on lineage block: "+t)}if(o(document).on("mousedown","select, ul li.select-option[role=option]",(function(t){try{if(o(t.target).closest("a").is("a")||o(t.target).is("a")||o(t.target).closest("button").is("button")||o(t.target).is("button"))return;var a=o(this),n=a.attr("aria-label")||"select from dropdown",i={actionType:"CL",contentTags:{contentName:n,contentType:"dropdown"}};a.attr({"data-bi-name":n,"data-bi-bhvr":"APPLY"}),window.owap.capturePageAction(this,i)}catch(t){e.debugLog("Mousedown on selection error: "+t)}})),o(document).on("change","select",(function(){var t=o(this),a=this.options[this.selectedIndex].text.trim(),e={actionType:"CL",behavior:"APPLY",contentTags:{contentName:a,contentType:"option"}};t.attr("data-bi-name",a),window.owap.capturePageAction(this,e)})),window.location.pathname.match(/(accessories|xbox-game-passgames)homeNew/i))try{o(document).on("mousedown",".c-label",(function(){var t=o(this).find("input")||" ";o(t).attr({"data-bi-name":e.etlcStr(o(this).find("span").text())})}))}catch(t){e.debugLog("Error on adding content name for dropdown: "+t)}if(n.match(/promotionswhat-are-you-playing/i)){try{o(document).on("mousedown","ul#questions-list li",(function(){o(this).attr({"data-bi-name":e.etlcStr(o(this).text()),"data-bi-bhvr":"APPLY"});var t={actionType:"CL"};window.owap.capturePageAction(this,t)}))}catch(t){e.debugLog("Error on Choosing Question tagging on What are you playing page: "+t)}o(document).on("mousedown","div.game-overlay",(function(t){var a=o(this).find("span").attr("class"),n=o(this).closest(".c-card").attr("data-bi-name");try{if(a)return void t.preventDefault();o(this).attr({"data-bi-name":e.etlcStr(n),"data-bi-bhvr":"APPLY","data-bi-type":e.tagChooseContentType(o(this))});var i={actionType:"CL"};window.owap.capturePageAction(this,i)}catch(t){e.debugLog("Error on Clicking Game Card tagging on What are you playing page: "+t)}}))}e.setSlotAndHeaderNameInfo=function(){try{o("ul.heroList li[id*=hero]:has(h2),.m-hero-item.videohero:not('ul.heroList li[id*=hero]:has(h2) .m-hero-item.videohero')").each((function(t){o(this).attr({"data-bi-slot":[t+1],"data-bi-hn":o(this).find("h2").text(),"data-promo-card":"true"})})),o(".hp-mosaic li[data-mosaic]:has(h2)").each((function(t){o(this).attr({"data-bi-slot":[t+11],"data-bi-hn":o(this).find("h2").text(),"data-promo-card":"true"})}))}catch(t){e.debugLog("setSlotAndHeaderNameInfo function error: "+t)}},e.setSlotAndHeaderNameInfoCounter=0,e.setSlotAndHeaderNameInfoInterval=setInterval((function(){try{var t=o("ul.heroList li[id*=hero]:has(h2),.m-hero-item.videohero:not('ul.heroList li[id*=hero]:has(h2) .m-hero-item.videohero')").length,a=o(".hp-mosaic li[data-mosaic]:has(h2)"),n=a.length;n&&(n=!1,a.first().find("h2").text()&&(n=a.first().find("h2").text().trim())),t&&n?(clearInterval(e.setSlotAndHeaderNameInfoInterval),e.setSlotAndHeaderNameInfo()):e.setSlotAndHeaderNameInfoCounter>30&&clearInterval(e.setSlotAndHeaderNameInfoInterval),e.setSlotAndHeaderNameInfoCounter++}catch(t){e.debugLog("setSlotAndHeaderNameInfoInterval function error: "+t)}}),200),o(document).on("mousedown","div.accordion__panel",(function(){try{if("true"==o(this).attr("aria-expanded"))return;e.tagGenericName(o(this)),o(this).attr("data-bi-bhvr","EXPAND"),o(this).attr("data-bi-type",e.tagChooseContentType(o(this))),window.owap.capturePageAction(this,{actionType:"CL"})}catch(t){e.debugLog("Error Tagging onclick of Accordion Expand from Console Xbox Series Pages. error: "+t)}})),o(document).on("mousedown",".accordion__panel input.btnClose, .tooltip-close",(function(){try{o(this).attr({"data-bi-name":e.etlcStr(o(this).attr("class"),"close"),"data-bi-bhvr":"REDUCE","data-bi-type":e.tagChooseContentType(o(this))});var t={actionType:"CL"};if(o(this).hasClass("tooltip-close"))return;window.owap.capturePageAction(this,t)}catch(t){e.debugLog("Error Tagging onclick of close from Console Xbox Series Pages. error: "+t)}})),o(document).on("mousedown",".hotspot",(function(){try{o(this).attr("data-bi-name",o(this).attr("aria-label"))}catch(t){e.debugLog("Error onclick of tooltip in xbox series page. Error: "+t)}})),n.match(/gamescall-of-duty-black-ops-6/i)&&o(document).on("mousedown","button.wf-vault-upgrade-btn",(function(){try{var t="EXPAND";o(".wf-vault-open").length&&(t="REDUCE"),o(this).attr("data-bi-bhvr",t)}catch(t){e.debugLog("Error on mousedown dropdown component: "+t)}})),o(document).on("mousedown",".stealth-carousel a, .stealth-carousel button",(function(){try{var t=o(this).closest("div[id*='ContentBlockList']").find(".m-banner h3").text()||o(this).closest("div[id*='Custom Sneaky Slider']").attr("data-bi-name"),a=o(this).parents(".stealth-carousel");if(t)o(this).attr("data-bi-hn",t);else if(a){var n=a.find(".stealth-sub-carousel:not([aria-hidden='true'])").find(".stealth-sub-carousel-panel:not([aria-hidden='true']):not(.panel-hide, .hide-panel)").find("[class*='c-heading']").text().trim();n&&o(this).attr("data-bi-hn",n)}}catch(t){e.debugLog("Error in adding in data-bi-hn attribute: "+t)}})),window.location.pathname.match(/xbox-game-passpc-game-pass/i)&&o(document).on("mousedown",".wf-carousel-card",(function(){try{var t=o(this).attr("onclick");if(!t.length)return;if(!(t=t.match(/'(.*?)'/i))||!t.length||t.length<2)return;t=t[1],o(this).attr("data-bi-mto","true");var a={actionType:"CL",targetUri:t};window.owap.capturePageAction(this,a)}catch(t){e.debugLog("Error in adding tagertURI:",t)}})),o(document).on("mousedown",".f-next, .f-previous",(function(){try{var t=o(this).closest("div[class*='featured-games']").find("div[class*='m-area-heading']").first().text().trim();t&&o(this).attr("data-bi-hn",t)}catch(t){wdgtagging.util.debugLog("Error in Implementing data-bi-hn in Carousel in Xbox Game Pass Ultimate Page: "+t)}})),o(document).on("mousedown","div.qclosebutton",(function(){try{o(this).attr({"data-bi-type":"button","data-bi-name":"popup close button"});var t={actionType:"CL"};window.owap.capturePageAction(this,t)}catch(t){wdgtagging.util.debugLog("Error in Implementing Tagging For Popup Close Icon Click for Quick Look Popup: "+t)}})),window.location.pathname.match(/eventsxbox-games-showcase/i)&&(o(document).on("mousedown",".m-panes-product-placement-item .c-call-to-action, .saveDateOnly .c-call-to-action",(function(){try{var t=o(this).closest("section").find("img").attr("src");t.indexOf("Calender")>-1?(o(this).closest("section").attr("data-bi-name")||o(this).closest("section").attr("data-bi-name","Calender Reminder"),o(this).attr("data-bi-bhvr","DOWNLOAD")):t.indexOf("Mail")>-1&&(o(this).closest("section").attr("data-bi-name")||o(this).closest("section").attr("data-bi-name","Sign up for email reminders"))}catch(t){e.debugLog("Error tagging data-bi-name & data-bi-bhvr in the xbox games showcase page. Error: "+t)}})),o(document).on("mousedown","div[class*='Modal-module__modalContent'] .c-button",(function(){try{o(this).closest("div[class*='Modal-module__modalContent']").attr("data-module-id")||o(this).closest("div[class*='Modal-module__modalContent']").attr({"data-bi-name":"Signup Modal","data-module-id":"true"}),o(this).attr("data-bi-bhvr")||o(this).attr("data-bi-bhvr","SIGNUP")}catch(t){e.debugLog("Error tagging data-bi-name & data-bi-bhvr for sign up button click in Modal popup. Error: "+t)}}))),n.match(/xbox-game-pass/i)&&o(document).on("mousedown",".c-in-page-navigation, .sku-chooser__panel",(function(){try{var t=o(this).is(".c-in-page-navigation")?"c-in-page-navigation":"sku-chooser__panel";o(this).attr("data-bi-name",t)}catch(t){e.debugLog("Error in Tagging Join now buttons:",t)}})),o(document).on("mouseover mousedown focusout change",".filtersAndResults .sortDropdown select",(function(t){try{const a=o(this);let e=a.attr("data-bi-bhvr");"mouseover"!==t.type||e?"mousedown"===t.type?a.attr("data-bi-bhvr","REDUCE"===e?"EXPAND":"REDUCE"):"focusout"!==t.type&&"change"!==t.type||a.attr("data-bi-bhvr","EXPAND"):a.attr("data-bi-bhvr","EXPAND")}catch(t){e.debugLog("Error in Tagging dropdown buttons:",t)}})),
n.match(/rog-xbox-ally/i)&&(o(document).on("mousedown pointerover",".rotator360:not([data-bi-name])",(function(){try{o(this).attr("data-bi-name","rotator360")}catch(t){e.debugLog("image rotator bi-name setting error: ",t)}})),e.imageSliderManualEvent=function(t){try{o(t).attr("data-bi-name",o(t).attr("aria-label"));var a={actionType:"CL",behavior:"OTHER",uri:location.href};window.owap.capturePageAction(t,a)}catch(t){e.debugLog("image rotator input 1ds event error: ",t)}},o(document).on("change","input.slider360",(function(){e.imageSliderManualEvent(this)})),o(document).on("pointerup",".img-container",(function(){e.imageSliderManualEvent(this)}))),o(window).on("load",(function(){const t=setInterval((()=>{const a=o(".m-ambient-video").find("universal-media-player");a.length>0&&(clearInterval(t),a.each(((t,a)=>{const e=a.shadowRoot&&a.shadowRoot.querySelector("ump-modals")&&a.shadowRoot.querySelector("ump-modals").shadowRoot&&a.shadowRoot.querySelector("ump-modals").shadowRoot.querySelector("ump-age-gate-verification")&&a.shadowRoot.querySelector("ump-modals").shadowRoot.querySelector("ump-age-gate-verification").shadowRoot;if(!e)return;const n=o(e);n.find(".dialog").attr({"data-bi-name":"ump-age-gate-verification-dialog","data-module-id":"true"}),n.find(".dialog .select-container .select").on("change",(function(){const t=o(this).attr("aria-label");o(this).attr("data-bi-name",t);const a={actionType:"CL",behavior:"APPLY",contentTags:{contentName:t,contentType:"option"}};window.owap.capturePageAction(this,a)})),n.find(".dialog button").on("mousedown",(function(){o(this).attr("data-bi-name","Submit");const t={actionType:"CL",contentTags:{contentName:"Submit",contentType:"button"}};window.owap.capturePageAction(this,t)}))})))}),500)}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript11"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,n,g){g(document).on("mousedown","a[href*='aka.ms/XboxInstaller'], a[href*='XboxInstaller.exe'], button[data-cta-href*='XboxInstaller.exe'], a[href*='aka.ms/xboxinstaller']",(function(){g(this).attr({"data-bi-bhvr":"DOWNLOADCOMMIT","data-bi-prtnm":"ms store"}),g(this).attr("data-bi-name")&&g(this).attr("data-m")||n.tagGenericName(g(this))}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript12"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,o,r){o.tagPartnerName=function(t){try{!r(t).attr("data-bi-prtnm")&&t.href&&r.trim(t.hostname)&&!t.hostname.match(/javascript|^#|xbox.com/i)&&r(t).attr("data-bi-prtnm",t.hostname)}catch(t){o.debugLog("tagPartnerName function error: "+t)}},o.tagChooseContentType=function(t){try{return t.find("img").length>0||t.find("picture").length>0?"image":e(t,"class","glyph-play")&&(t.find("span").length<=0||e(t.find("span"),"class","screen-reader"))||e(t,"class","mscom-popup-close|m-back-to-top|video_pp_button|ps-lightbox-close")||t.is("button")?"button":"text"}catch(t){o.debugLog("tagChooseContentType function error: "+t)}};var e=function(t,a,o){var e=r(t),i=new RegExp(o,"i");return e.attr(a)&&e.attr(a).match(i)};r(document).on("mousedown","a:not([data-m]):not([data-bi-type]), button:not([data-m]):not([data-bi-type])",(function(){try{r(this).attr("data-bi-type",o.tagChooseContentType(r(this)))}catch(t){o.debugLog("Error tagging on Picking up any tag that is missing contentType. Error: "+t)}})),o.tagProdSkuId=function(t){try{var a,e;r(t).is("a")&&(e=!0);var i=r(t).attr("data-cta-href");if(!e&&i&&""!=i){var n=document.createElement("A");n.href=i,a=r(n)}else a=r(t);var d=a.is("A")?a[0].pathname:"",c=a.is("A")?a[0].hostname:"",s=a.is("A")?a[0].search:"";if(d.match(/onerfsignin/i)){var h=document.createElement("a");if(h.href=window.wdgtagging.util.getQueryParam("ru",s),!h||!r(h).attr("href"))return;d=r(h)[0].pathname||"",c=r(h)[0].hostname||"",s=r(h)[0].search||""}var m,g,u,l=(a=r(t)).find("button");if(d.match(/productID/i))a.attr("data-bi-product",d.split("productID")[1]);else if(s.match(/pid=/i)){var p=window.wdgtagging.util.getQueryParam("pid",s);a.attr("data-bi-product",p)}else c.match(/xbox.com/gi)&&d.match(/..-..configure/i)?(u=(m=d.substring(d.indexOf("/configure")).split("/")).length>2?m[2]:null,a.attr("data-bi-product",u)):c.match(/xbox.com/gi)&&d.match(/gamesstore/i)?(u=(m=d.substring(d.indexOf("/games/store")).split("/")).length>4?m[4]:null,a.attr("data-bi-product",u)):d.match(/playgames/i)?(u=(m=d.substring(d.indexOf("/play/games")).split("/")).length>4?m[4]:null,a.attr("data-bi-product",u)):d.match(/store(b|d|config|buy|p)/i)||d.match(/storeconfigurexbox-design-lab/gi)?(u=(m=d.substring(d.indexOf("/store")).split("/")).length>4?m[4]:null,a.attr("data-bi-product",u)):d.match(/storebuild/)?(produId=d.split("/")[5],a.attr("data-bi-product",produId)):a.is("[data-xbbigid]")&&a.attr("data-bi-product",a.attr("data-xbbigid"));if(s.match(/sid=/i))g=window.wdgtagging.util.getQueryParam("sid",s),a.attr("data-bi-sku",g);else if(d.match(/store(d|config|p)/i)){var f=m.length>5?m[5]:null;a.attr("data-bi-sku",f)}else if(c.match(/xbox.com/gi)&&d.match(/gamesstore/i)){f=(m=d.substring(d.indexOf("/games/store")).split("/")).length>5?m[5]:null;a.attr("data-bi-sku",f)}else if(c.match(/xbox.com/gi)&&d.match(/playgames/i)){f=(m=d.substring(d.indexOf("/play/games")).split("/")).length>5?m[5]:null;a.attr("data-bi-sku",f)}if(!a.attr("data-bi-product")){var b=a.attr("data-updated-productid"),w=a.attr("data-special-productid"),v=null!=w&&w.length>1?w:b;null!=v&&v.length>1&&(x=v.split("/")[0],g=v.split("/")[1],x&&(a.attr("data-bi-product",x),l.attr("data-bi-product",x)),g&&(a.attr("data-bi-sku",g),l.attr("data-bi-sku",g)))}if(!a.attr("data-bi-product"))if(null!=a.attr("data-productId")||null!=a.attr("data-bigid")||null!=a.parent().attr("data-bigid")||null!=a.parent().attr("data-productId")){var y=null!=a.attr("data-productId")?a.attr("data-productId"):a.parent().attr("data-productId");if(y||(y=null!=a.attr("data-bigid")?a.attr("data-bigid"):a.parent().attr("data-bigid")),y){var x=y.split("/")[0],k=y.split("/")[1];x&&(a.attr("data-bi-product",x),l.attr("data-bi-product",x)),k&&(a.attr("data-bi-sku",k),l.attr("data-bi-sku",k))}}else if(a.attr("onclick")&&a.attr("onclick").match(/(xboxContextualStore|OpenWithExp)/i)){var L=a.attr("onclick").match(/([w]+)(['"]?([w]+)?['"]?,?['"]?([w]+)?['"]?)/),A={open:2,openwithexp:3},E=1;if(L&&L[E]){var R=r.trim(L[E].toLowerCase()),C=(p=L[A[R]])||null;a.attr("data-bi-product",C)}}if(!a.attr("data-bi-product")&&d.match(/(..-..)?(p|d)/gi)){var T=d.split("/"),P=d.match(/(..-..)/i);x=P?T[4]:T[3],g="",P&&T.length>5?g=T[5]:!P&&T.length>4&&(g=T[4]),a.attr({"data-bi-sku":g,"data-bi-product":x})}}catch(t){o.debugLog("tagProdSkuId function error: "+t)}},o.tagProdName=function(t){try{var a,e;r(t).is("a")&&(e=!0);var i=r(t).attr("data-cta-href");if(!e&&i&&""!=i){var n=document.createElement("A");n.href=i,a=r(n)}else a=r(t);var d,c,s=a.is("A")?a[0].pathname:"",h=a.is("A")?a[0].hostname:"",m=a.is("A")?a[0].search:"";if(s.match(/onerfsignin/i)){var g=document.createElement("a");if(g.href=window.wdgtagging.util.getQueryParam("ru",m),!g||!r(g).attr("href"))return;s=r(g)[0].pathname||"",h=r(g)[0].hostname||"",m=r(g)[0].search||""}if(!h.match(/(xbox|microsoft).com/i))return;if(a=r(t),s.match(/store(b|d|config|buy|p)/i))c=(d=s.substring(s.indexOf("/store")).split("/")).length>=4?d[3].replace(/-/g," "):null,a.attr("data-bi-prod",o.tlcStr(c));else if(h.match(/xbox.com/gi)&&s.match(/gamesstore/i))c=(d=s.substring(s.indexOf("/games/store")).split("/")).length>3?d[3].replace(/-/g," "):null,a.attr("data-bi-prod",o.tlcStr(c));else if(s.match(/playgames/i))c=(d=s.substring(s.indexOf("/play/games")).split("/")).length>3?d[3].replace(/-/g," "):null,a.attr("data-bi-prod",o.tlcStr(c));else if(s.match(/product/i)){var u=s.split("/");c=4==u.length?u[2].replace(/-/g," "):u[3].replace(/-/g," "),a.attr("data-bi-prod",o.tlcStr(c))}else if(s.match(/storebuild/gi)||s.match(/storebuy/gi)){var l=window.location.pathname.split("/");if(null===(c=6==l.length?l[3].replace(/-/g," ")+"-"+l[4].replace(/-/g," ")+" "+l[5].replace(/-/g," "):null)){var p=s.split("/");c=6==p.length?p[4].replace(/-/g," "):null}a.attr("data-bi-prod",o.tlcStr(c))}else if(s.match(/(..-..)?p/gi)){var f=s.split("/");c=s.match(/(..-..)/i)?f[3].replace(/-/g," "):f[2].replace(/-/g," "),a.attr("data-bi-prod",o.tlcStr(c))}}catch(t){o.debugLog("tagProdName function error: "+t)}},o.tagPartnerLinks=function(t){try{if(void 0!==r(t)){var a,e,i;r(t).is("a")&&(i=!0);var n=r(t).attr("data-cta-href");if(!i&&n&&""!=n){var d=document.createElement("A");d.href=n,a=(e=r(d)).attr("href")}else a=r(t).attr("href"),e=r(t);var c=e[0].hostname||"";if(a&&!1===a.startsWith("#")){var s=r.trim(r(t).attr("data-retailer")).toLowerCase();if(a&&(a.match(/microsoft.com/i)&&a.match(/(store|p|d)/i)||a.match(/gamesstore/i)||a.match(/xbox.com..-..configure/i)||a.match(/playgames/gi)))s="ms store",o.tagProdSkuId(t);else if(a&&a.match(/^https?:login.live.com/i)){var h=a.replace(/.*&wreply=(.*)/,"$1").split("&")[0];if(h){var m=decodeURIComponent(h).replace(/^https?:(www.)?microsoft.com(..-..)?store(.*)/,"$3");if(m.match(/^buy?pid=.+/i)){var g=m.replace(/^buy?pid=(.*)/,"$1").split("&")[0].toUpperCase();g&&t.attr({"data-bi-product":g});var u=m.replace(/.*sid=(.*)/,"$1").split("&")[0].toUpperCase();u&&t.attr({"data-bi-sku":u})}}}s&&(o.tagGenericName(t),t.attr({"data-bi-prtnm":s,"data-bi-bhvr":"PARTNERREFERRAL","data-bi-type":o.tagChooseContentType(t)})),(!a.match(/javascript:void(0)|xbox.com/i)||a.match(/gamesstore/i)||a.match(/xbox.com..-..configure/i)||a.match(/playgames/i)||a.match(/xbox.com..-..cart/i))&&t.attr("data-bi-prtid",c)}}}catch(t){o.debugLog("tagPartnerLinks function error: "+t)}},o.tagMsStoreLink=function(t){try{o.tagProdName(r(t)),o.tagPartnerLinks(r(t)),r(t).attr({"data-bi-prtnm":"ms store","data-bi-bhvr":"PARTNERREFERRAL","data-bi-type":o.tagChooseContentType(r(this))})}catch(t){o.debugLog("Error tagging on MsStore link Function. Error: "+t)}};var i="A[href*='apps.apple.com']:not([data-m]), A[href*='itunes.apple.com']:not([data-m]), A[href*='aka.ms/xbox.events.ios']:not([data-m]), A[href*='aka.ms/xbox.events.android']:not([data-m]), A[href*='play.google']:not([data-m]), A[href*='//go.onelink.me/app']:not([data-m]), A[href*='ms-windows-store:']:not([data-m]), a[href*='XboxFamilyBetaAndroid']:not([data-m]), a[href*='XboxFamilyBetaiOS']:not([data-m]),  a[href*='galaxystore.samsung.com']:not([data-m]),  a[href*='Aka.ms/XboxFamilySettingsiOS']:not([data-m]),  a[href*='Aka.ms/XboxFamilySettingsAndroid']:not([data-m]),  a[href*='testflight.apple.com']:not([data-m])",n="button[data-cta-href*='ms-windows-store'],button[data-uri*='ms-windows-store']";r("a[data-retailer]").each((function(){r(this).is(i)||o.tagPartnerLinks(r(this))})),r(document).on("mousedown","a[data-retailer]",(function(){o.tagPartnerLinks(r(this))}));var d=" A[href*='marketplace.xbox.com'][data-retailer][data-retailer!='']:not([data-m]), a[href*='microsoftstore']:not([data-m]),  a[href*='microsoft.com'][href*='/store/'],[id*='ContentBlockList']  a[href*='microsoft.com'][href*='/store/'],[id*='TopContentBlockList']  a[href*='microsoft.com'][href*='/store/']:not([data-m]),  a[href*='microsoft.com'][href*='/p/']:not([data-m]), a[href*='microsoft.com'][href*='/d/']:not([data-m])";r(d).each((function(){o.tagMsStoreLink(r(this))})),r(document).on("mousedown",d,(function(){o.tagMsStoreLink(r(this))}));var c=" [id*='ContentBlockList'] a[href*='microsoft.com'][href*='/p/'], [id*='ContentBlockList'] a[href*='microsoft.com'][href*='/d/'], [id*='TopContentBlockList'] a[href*='microsoft.com'][href*='/p/'], [id*='TopContentBlockList'] a[href*='microsoft.com'][href*='/d/'], .c-dialog a[href*='microsoft.com'][href*='/p/'], .c-dialog a[href*='microsoft.com'][href*='/d/'], .c-dialog a[href*='microsoft.com'][href*='/store/']";r(c).each((function(){o.tagMsStoreLink(r(this))})),r(document).on("mousedown",c,(function(){o.tagMsStoreLink(r(this))}));var s="a[href*='/games/store/'], a[href*='xbox.com'][href*='/configure/'],button[data-cta-href*='/configure/'], button[data-cta-href*='/store/']";r(s).each((function(){o.tagMsStoreLink(r(this))})),r(document).on("mousedown",s,(function(){o.tagMsStoreLink(r(this))})),window.location.pathname.match(/developerscreators-program/gi)&&r(document).on("mousedown"," #ContentBlockList_4 A:not(a[href*='docs.microsoft.com']), #ContentBlockList_5 a",(function(){var t=this.href.split("/")[2].replace("www.","");r(this).attr({"data-bi-bhvr":"PARTNERREFERRAL","data-bi-prtnm":t,"data-bi-type":o.tagChooseContentType(r(this))})})),r(document).on("mousedown","A:not([data-bi-product]):not([data-m]),[id*='ContentBlockList'] A:not([data-bi-product])",(function(){jqThis=r(this);try{o.tagProdSkuId(jqThis),jqThis.attr("data-productid")?jqThis.attr("data-bi-product",jElem.attr("data-productid")):jqThis.attr("productbuyxmlid")&&jqThis.attr("data-bi-product",jElem.attr("productbuyxmlid"))}catch(t){o.debugLog("Mosuedown on anchor links Product data setting error: "+t)}})),window.location.pathname.match(/promotionsvoyage/gi)&&r(document).on("mousedown",".center-mod A[href*='app.appsflyer']",(function(){var t=this.href.split("/")[2].replace("www.","");r(this).attr({"data-bi-bhvr":"DOWNLOADCOMMIT","data-bi-prtnm":t,"data-bi-type":o.tagChooseContentType(r(this))})})),window.location.pathname.match(/promotionsxbox-cutouts/gi)&&r(document).on("mousedown",".m-content-placement-item a[href*='query.prod.cms.rt']",(function(){r(this).attr("data-bi-bhvr","DOWNLOADCOMMIT")})),o.tagDownloadCommit=function(t){var a=r(t).attr("data-retailer")||r(t).attr("data-cta-href")||r(t).attr("data-uri")||t.hostname||"";(r(t).is("a[href]")&&r(t).attr("href").match(/ms-windows-store:/gi)||a.match(/ms-windows-store:/gi))&&(a="ms store"),r(t).attr({"data-bi-bhvr":"DOWNLOADCOMMIT","data-bi-prtnm":a,"data-bi-type":o.tagChooseContentType(r(t))})};try{r(i).each((function(){o.tagDownloadCommit(this)})),r(n).each((function(){o.tagDownloadCommit(this)}))}catch(t){o.debugLog("Error while tagging links with DOWNLOADCOMMIT on pageload. Error: "+t)}r(document).on("mousedown",i,(function(){try{o.tagDownloadCommit(this)}catch(t){o.debugLog("Error while tagging links with DOWNLOADCOMMIT on pageAction. Error: "+t)}})),r(document).on("mousedown",n,(function(){try{o.tagDownloadCommit(this)}catch(t){o.debugLog("Error while tagging links with DOWNLOADCOMMIT on pageAction. Error: "+t)}})),window.location.pathname.match(/xbox-one-sfamily-entertainment?/gi)&&r(document).on("mousedown"," A[href*='/live-apps/']:not([data-m])",(function(){var t=this.pathname.split("/");t.length>5&&(t=t[5]),r(this).attr({"data-bi-prod":t,"data-bi-prtnm":"ms store","data-bi-bhvr":"PARTNERREFERRAL"})})),window.location.pathname.match(/promotionsgame-pass-offer?/gi)&&r(document).on("mousedown",".m-area-heading.threeliner A:not([data-retailer])",(function(){r(this).attr({"data-bi-prtnm":o.tlcStr(this.hostname.replace("www.","")),"data-bi-bhvr":"PARTNERREFERRAL"})})),r("a[href]:not([data-bi-prtnm])").each((function(){var t=this;o.tagPartnerName(t)})),r(document).on("mousedown","a[href]:not([data-bi-prtnm]), .c-age-rating a[href]",(function(){r(this).is(".c-age-rating a[href]")&&r(this).removeAttr("data-bi-prtnm"),o.tagPartnerName(this)})),window.location.pathname.match(/..-..promotionstus-juegos-digitaleshome/gi)&&r(document).on("mousedown",".container-logos .logos A[href], #ContentBlockList_5 section.m-content-placement-item A[href]",(function(){r(this).attr("data-bi-bhvr","PARTNERREFERRAL")})),r(document).on("mousedown","a[href*='stores.footlocker'], a[href*='www.footlocker']",(function(){r(this).attr("data-bi-bhvr","PARTNERREFERRAL")})),window.location.pathname.match(/promotionscontrol-your-discount/gi)&&r(document).on("mousedown",".container-retailers a[href]",(function(){r(this).attr("data-bi-bhvr","PARTNERREFERRAL")})),o.tagMSLinkLightbox=function(t){try{r(t).attr("data-retailer","ms store"),o.tagMsStoreLink(r(t));var a=r(t).closest(".hatchretailer[data-retailerpriority=0]");r(a).attr({"data-gm-store":r(t).attr("data-bi-prtnm"),"data-gm-productId":r(t).attr("data-bi-product"),"data-gm-productName":r(t).attr("data-bi-prod"),"data-gm-productSku":r(t).attr("data-bi-sku")})}catch(t){o.debugLog("Error Tagging on setting up ms link data on the lightbox. Error: "+t)}},r(document).on("mousedown",".hatchProd[data-js-dialog-show]",(function(){try{var t=r(this).attr("data-js-dialog-show"),a=r(".hatchDialog[id*="+t+"][data-product-name]").attr("data-product-name"),e=r(this).attr("data-hatch-bigids");r(this).attr({"data-bi-bhvr":"INTENTTOBUY","data-bi-prtnm":"gethatch","data-bi-prod":a,"data-bi-product":t,"data-bi-sku":e})}catch(t){o.debugLog("Mousedown on open getHatch lightbox error: "+t)}})),r(document).on("mousedown",".c-dialog:not([data-bi-area])",(function(){o.tagLightboxArea()})),r(document).on("mouseenter",".c-dialog",(function(){r(this).find("input:not([data-bi-name])").length&&o.tagInputElem(),r(this).find(".hatchretailer a[href*=microsoft][href*='/p/'], .hatchretailer a[href*=microsoft][href*='/d/']").each((function(){var t=this;o.tagMSLinkLightbox(r(t))}))})),r(document).on("mousedown",".c-dialog .hatchretailer a[href]",(function(){try{if(r(this).attr("href").match(/microsoft.com/i))o.tagMSLinkLightbox(r(this));else{var t=r(this).closest(".hatchretailer[data-retailerpriority]"),a=r(t).siblings("[data-retailerpriority][data-gm-store]");if(a.length)var e=a.attr("data-gm-productName"),i=a.attr("data-gm-productId"),n=a.attr("data-gm-productSku");else{var d=r(this).closest(".hatchDialog[data-product-name]");if(d.length)e=d.attr("data-product-name"),i=d.attr("id"),n=d.attr("data-product-spec")}r(this).attr({"data-bi-prod":e,"data-bi-product":i,"data-bi-sku":n})}}catch(t){o.debugLog("Mosuedown on getHatch links error: "+t)}}));var h="a[href*=where-to-buy][data-bi-bhvr*=PARTNERREFERRAL], button[data-cta-href*=where-to-buy][data-bi-bhvr*=PARTNERREFERRAL]";r(document).on("mousedown",h,(function(){try{r(this).removeAttr("data-bi-bhvr")}catch(t){o.debugLog("removePartnerSelector mousedown error: "+t)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript13"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(a,t,i){var r;jQuery("div.accordion li").each((function(){try{r=jQuery(this);var a=jQuery.trim(jQuery("h3",r).text())||jQuery.trim(r.attr("aria-label"))||"";r.attr({"data-bi-name":a.toLowerCase(),"data-bi-slot":r.index()+1})}catch(a){i.debugLog("Error tagging Accordion section. Error: "+a)}})),jQuery("div.accordion li").click((function(){try{var a=jQuery(this);if(a.attr("class")!=a.attr("data-lastClass")&&"expanded"==a.attr("class")){var t={behavior:"EXPAND",actionType:"CL"};window.owap.capturePageAction(this,t)}jQuery("div.accordion li").each((function(){var a=jQuery(this);a.attr("data-lastClass",a.attr("class"))}))}catch(a){i.debugLog("Error tagging Accordion section. Error: "+a)}})),jQuery("div.accordion div.btnClose").click((function(){try{var a=(r=jQuery(this)).closest("li");r.attr({"data-bi-name":a.attr("data-bi-name"),"data-bi-slot":a.attr("data-bi-slot")});var t={behavior:"REDUCE",actionType:"CL"};window.owap.capturePageAction(this,t)}catch(a){i.debugLog("Error tagging Accordion section. Error: "+a)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript14"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,o,n){n(document).on("mousedown",".fui-FluentProvider .fui-MenuItem",(function(t){try{if(n(t.target).closest("a").is("a")||n(t.target).is("a")||n(t.target).closest("button").is("button")||n(t.target).is("button"))return;var a={actionType:"CL"};window.owap.capturePageAction(this,a)}catch(t){o.debugLog("Error Tagging Chat Bot Menu Item: "+t)}})),n(document).on("mousedown",".fui-Button[type=submit]",(function(){try{var t=this,a=JSON.parse(n(t).attr("data-m")||"{}");a.cN="Submit Button",a.ecn="Submit Button",a.cT="button",a.pa="Body",a.compnm="StoreAssistant",n(t).attr("data-m",JSON.stringify(a))}catch(t){o.debugLog("Error Tagging submit arrow button: "+t)}})),n(document).on("keydown",".copilot-container .fai-ContentEditableSpan",(function(t){try{if("13"==(t.keyCode?t.keyCode:t.which)){var a=this,e=JSON.parse(n(a).attr("data-m")||"{}");e.cN="Input Entered",e.ecn="Input Entered",e.pa="Body",e.compnm="StoreAssistant",n(a).attr("data-m",JSON.stringify(e));var r={actionType:"CL"};window.owap.capturePageAction(this,r)}}catch(t){o.debugLog("Error Tagging Enter Key Pressed to Submit Input: "+t)}})),n(document).on("mousedown",".copilot-container .fai-CopilotMessage a[href]",(function(){try{var t=this;o.tagProdName(n(t)),o.tagPartnerLinks(n(t));var a=JSON.parse(n(t).attr("data-m")||"{}");a.bhvr||(a.bhvr=n(t).attr("data-bi-bhvr")),a.prtid||(a.prtid=n(t).attr("data-bi-prtid")),a.prtnm||(a.prtnm=n(t).attr("data-bi-prtnm")),a.pid||(a.pid=n(t).attr("data-bi-product")),a.prod||(a.prod=n(t).attr("data-bi-prod")),n(t).attr("data-m",JSON.stringify(a))}catch(t){o.debugLog("Error Tagging Partner referral tagging for links inside chatbot: "+t)}})),n(document).on("mousedown",".copilot-container .button-compose [role='button']",(function(t){try{if(n(t.target).closest("a").is("a")||n(t.target).is("a")||n(t.target).closest("button").is("button")||n(t.target).is("button"))return;var a=this,e=JSON.parse(n(a).attr("data-m")||"{}");e.cN="New Chat Icon",e.ecn="New Chat Icon",e.pa="Body",e.compnm="StoreAssistant",n(a).attr("data-m",JSON.stringify(e));var r={actionType:"CL"};window.owap.capturePageAction(this,r)}catch(t){o.debugLog("Error Tagging New Chat Icon click: "+t)}})),n(document).on("mousedown",".copilot-container .fai-CopilotMessage [role='button'][aria-expanded]",(function(t){try{if(n(t.target).closest("a").is("a")||n(t.target).is("a")||n(t.target).closest("button").is("button")||n(t.target).is("button"))return;var a=this,e=JSON.parse(n(a).attr("data-m")||"{}");"true"==n(a).attr("aria-expanded")?(e.cN="See Less",e.ecn="See Less",e.bhvr="REDUCE"):"false"==n(a).attr("aria-expanded")&&(e.cN="See More",e.ecn="See More",e.bhvr="EXPAND"),e.pa="Body",e.compnm="StoreAssistant",n(a).attr("data-m",JSON.stringify(e));var r={actionType:"CL"};window.owap.capturePageAction(this,r)}catch(t){o.debugLog("Error Tagging See More|See Less link clicks: "+t)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript15"](function(event, target, Promise) {
null!==window.wdgtagging&&null!==window.wdgtagging.oneds&&function(e,t,i,o){window.location.pathname,window.location.href;i.oneDSVList={},i.changeAppId="JS:XboxWeb",i.videoAPI=!0,i.oneDSIframeVideoTaggingConstructor=function(e,t,o,n,a){i.oneDSVList[e]={},i.oneDSVList.inLightBox=!0,i.oneDSVList[e].videoName=t,i.oneDSVList[e].isEnded=!1,i.oneDSVList[e].isMuted=a||"",i.oneDSVList[e].isloop="",i.oneDSVList[e].shouldCapture=!0,i.oneDSVList[e].paused=!1,i.oneDSVList[e].lastSentPercentage=-1,i.oneDSVList[e].started=!0,i.oneDSVList[e].completed=!1,i.oneDSVList[e].myTimeStamp=Math.floor(Date.now()/1e3),i.oneDSVList[e].wdgVideoObject={},i.oneDSVList[e].wdgVideoObject.behavior="",i.oneDSVList[e].wdgVideoObject.actionType=o||"",i.oneDSVList[e].wdgVideoObject.contentTags={},i.oneDSVList[e].wdgVideoObject.contentTags.vidnm=t,i.oneDSVList[e].wdgVideoObject.contentTags.vidid=e,i.oneDSVList[e].wdgVideoObject.contentTags.area="body",i.oneDSVList[e].wdgVideoObject.contentTags.vidpct="",i.oneDSVList[e].wdgVideoObject.contentTags.viddur=n||"",i.oneDSVList[e].wdgVideoObject.contentTags.type="video",i.oneDSVList[e].wdgVideoObject.contentTags.containerName="oneplayer",i.oneDSVList[e].wdgVideoObject.contentTags.parentpage=window.location.href,i.oneDSVList[e].wdgVideoObject.contentTags.field1="mgt"},i.checkIframeDomain=function(e){try{return Boolean(e.match(/www.(microsoft|xbox).com/i))}catch(e){return i.debugLog("checkIframeDomain error: "+e),!1}},window.onload=function(){o("iframe[class*=wirewaxplayer], iframe[src*=videoplayer]").each((function(){var e={setAppId:!0,appId:"JS:XboxWeb",vTagging:!0},t=new URL(this.src).origin;i.checkIframeDomain(t)&&this.contentWindow.postMessage(e,t)})),o("iframe[class*=wirewaxplayer], iframe[src*=videoplayer]").each((function(){var e={videoAPI:!0,vTagging:!0,tOffIframeTagging:!0},t=new URL(this.src).origin;i.checkIframeDomain(t)&&this.contentWindow.postMessage(e,t)}))},o(window).on("message",(function(e){if(null!=e.originalEvent.origin.match(/www.(microsoft|xbox).com/)&&(e.originalEvent.data&&e.originalEvent.data.onePlayerApi&&(i.changeAppId&&o("iframe[class*=wirewaxplayer], iframe[src*=videoplayer]").each((function(){var e={setAppId:!0,appId:"JS:XboxWeb",vTagging:!0},t=new URL(this.src).origin;i.checkIframeDomain(t)&&this.contentWindow.postMessage(e,t)})),i.videoAPI&&o("iframe[class*=wirewaxplayer], iframe[src*=videoplayer]").each((function(){var e={videoAPI:!0,tOffIframeTagging:!0,vTagging:!0},t=new URL(this.src).origin;i.checkIframeDomain(t)&&this.contentWindow.postMessage(e,t)}))),!e.originalEvent.data||"video"===e.originalEvent.data.tagging||"behavior"===e.originalEvent.data.tagging))if("video"==e.originalEvent.data.tagging){var t=e.originalEvent.data.type,n=e.originalEvent.data.targetVideoId,a=e.originalEvent.data.targetVideoName;switch(t){case"ended":i.oneDSVList[n].isEnded=!0;break;case"pause":if(e.originalEvent.data.readyState>2&&!e.originalEvent.data.ended){i.oneDSVList[n].paused=!0;var d=10*Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*10);i.oneDSVList[n].wdgVideoObject.behavior="VIDEOPAUSE",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct=d.toString(),window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject)}else i.oneDSVList[n].paused=!1;e.originalEvent.data.ended||(i.oneDSVList[n].shouldCapture=!0,"A"===i.oneDSVList[n].wdgVideoObject.actionType&&(i.oneDSVList[n].wdgVideoObject.actionType="O"));break;case"playing":if(i.oneDSVList[n].wdgVideoObject.actionType||(i.oneDSVList[n].wdgVideoObject.actionType=e.originalEvent.data.autoplay?"A":"O"),i.oneDSVList[n].wdgVideoObject.contentTags.viddur||(i.oneDSVList[n].wdgVideoObject.contentTags.viddur=e.originalEvent.data.duration),"boolean"!=typeof i.oneDSVList[n].isMuted&&(i.oneDSVList[n].isMuted=e.originalEvent.data.muted||0===e.originalEvent.data.volume),"boolean"!=typeof i.oneDSVList[n].isloop&&(i.oneDSVList[n].isloop=e.originalEvent.data.loop),0===Math.floor(e.originalEvent.data.currentTime)&&i.oneDSVList[n].shouldCapture&&(i.oneDSVList[n].started&&i.oneDSVList[n].completed&&i.oneDSVList[n].isEnded?(i.oneDSVList[n].wdgVideoObject.behavior="VIDEOREPLAY",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct="0",window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject)):i.oneDSVList[n].started||(i.oneDSVList[n].wdgVideoObject.behavior="VIDEOSTART",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct="0",window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject),i.oneDSVList[n].started=!0),"A"!==i.oneDSVList[n].wdgVideoObject.actionType||i.oneDSVList.inLightBox||(i.oneDSVList[n].shouldCapture=!1)),i.oneDSVList[n].paused&&i.oneDSVList[n].shouldCapture){i.oneDSVList[n].paused=!1;d=10*Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*10);i.oneDSVList[n].wdgVideoObject.behavior="VIDEOCONTINUE",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct=d.toString(),window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject)}i.oneDSVList[n].isEnded=e.originalEvent.data.ended;break;case"seeked":if(i.oneDSVList[n].shouldCapture&&Math.floor(Date.now()/1e3)-i.oneDSVList[n].myTimeStamp>1&&!i.oneDSVList[n].isEnded){var s=Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*100);d=10*Math.floor(s/10);if(100===i.oneDSVList[n].lastSentPercentage&&(0===s||e.originalEvent.data.currentTime<.75))return;i.oneDSVList[n].wdgVideoObject.behavior="VIDEOJUMP",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct=d.toString(),window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject),"A"===i.oneDSVList[n].wdgVideoObject.actionType&&(i.oneDSVList[n].wdgVideoObject.actionType="O"),i.oneDSVList[n].myTimeStamp=Math.floor(Date.now()/1e3)}break;case"timeupdate":i.oneDSVList[n].wdgVideoObject.actionType||(i.oneDSVList[n].wdgVideoObject.actionType=e.originalEvent.data.autoplay?"A":"O"),i.oneDSVList[n].wdgVideoObject.contentTags.viddur||(i.oneDSVList[n].wdgVideoObject.contentTags.viddur=e.originalEvent.data.duration),"boolean"!=typeof i.oneDSVList[n].isMuted&&(i.oneDSVList[n].isMuted=e.originalEvent.data.muted||0===e.originalEvent.data.volume),"boolean"!=typeof i.oneDSVList[n].isloop&&(i.oneDSVList[n].isloop=e.originalEvent.data.loop);var r=e.originalEvent.data.currentTime/e.originalEvent.data.duration*100>=99||e.originalEvent.data.duration-e.originalEvent.data.currentTime<.75;if(("O"===i.oneDSVList[n].wdgVideoObject.actionType||i.oneDSVList.inLightBox)&&i.oneDSVList[n].shouldCapture&&!r&&!i.oneDSVList[n].paused&&!i.oneDSVList[n].isEnded)(d=10*Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*10))!==i.oneDSVList[n].lastSentPercentage&&(i.oneDSVList[n].wdgVideoObject.behavior="VIDEOCHECKPOINT",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct=d.toString(),window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject),i.oneDSVList[n].lastSentPercentage=d),Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*100)>1&&e.originalEvent.data.currentTime>1&&(i.oneDSVList[n].isEnded=e.originalEvent.data.ended);("O"===i.oneDSVList[n].wdgVideoObject.actionType||i.oneDSVList.inLightBox)&&i.oneDSVList[n].shouldCapture&&!i.oneDSVList[n].completed&&r&&(i.oneDSVList[n].wdgVideoObject.behavior="VIDEOCOMPLETE",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct="100",window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject),i.oneDSVList[n].completed=!0,i.oneDSVList[n].isloop&&(i.oneDSVList[n].shouldCapture=!1)),r&&("O"===i.oneDSVList[n].wdgVideoObject.actionType||i.oneDSVList.inLightBox)&&100!==i.oneDSVList[n].lastSentPercentage&&(i.oneDSVList[n].myTimeStamp=Math.floor(Date.now()/1e3),i.oneDSVList[n].wdgVideoObject.behavior="VIDEOCHECKPOINT",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct="100",window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject),i.oneDSVList[n].lastSentPercentage=100,i.oneDSVList[n].isloop&&(i.oneDSVList[n].shouldCapture=!1)),r&&(i.oneDSVList[n].isEnded=!0);break;case"volumechange":if(i.oneDSVList[n].isMuted||!e.originalEvent.data.muted&&0!==e.originalEvent.data.volume||"A"!==i.oneDSVList[n].wdgVideoObject.actionType)if(i.oneDSVList[n].isMuted||!e.originalEvent.data.muted&&0!==e.originalEvent.data.volume||"O"!==i.oneDSVList[n].wdgVideoObject.actionType&&!i.oneDSVList.inLightBox){if(!(i.oneDSVList[n].isMuted&&!e.originalEvent.data.muted&&e.originalEvent.data.volume>0))return;i.oneDSVList[n].isMuted=e.originalEvent.data.muted||0===e.originalEvent.data.volume,i.oneDSVList[n].shouldCapture=!0,i.oneDSVList[n].wdgVideoObject.behavior="VIDEOUNMUTE","A"===i.oneDSVList[n].wdgVideoObject.actionType&&(i.oneDSVList[n].wdgVideoObject.actionType="O")}else i.oneDSVList[n].isMuted=e.originalEvent.data.muted||0===e.originalEvent.data.volume,i.oneDSVList[n].shouldCapture=!0,i.oneDSVList[n].wdgVideoObject.behavior="VIDEOMUTE";else i.oneDSVList[n].isMuted=e.originalEvent.data.muted||0===e.originalEvent.data.volume,i.oneDSVList[n].shouldCapture=!1,i.oneDSVList[n].wdgVideoObject.behavior="VIDEOMUTE";d=10*Math.floor(e.originalEvent.data.currentTime/e.originalEvent.data.duration*10);i.oneDSVList[n].wdgVideoObject.contentTags.vidpct=d.toString(),window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject);break;case"videostart":i.oneDSVList[n]&&delete i.oneDSVList[n];var g=e.originalEvent.data.targetVideoActionType,c=e.originalEvent.data.targetVideoDuration,V=e.originalEvent.data.targetVideoIsMuted;i.oneDSIframeVideoTaggingConstructor(n,a,g,c,V),i.oneDSVList[n].wdgVideoObject.behavior="VIDEOSTART",i.oneDSVList[n].wdgVideoObject.contentTags.vidpct="0",window.owap.capturePageAction(null,i.oneDSVList[n].wdgVideoObject)}}else if("behavior"==e.originalEvent.data.tagging){var l=e.originalEvent.data.behavior;246!=l&&247!=l&&250!=l&&251!=l&&253!=l||window.owap.capturePageAction(null,e.originalEvent.data)}}))}(window.wdgtagging,window.wdgtagging.jsll,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript16"](function(event, target, Promise) {
null!=window.wdgtagging&&function(a,o){var r=window.location.pathname;if(window.location.hostname.match(/xbox.com/gi)){var t=function(){try{window.addEventListener("message",(function(a){try{if(a.origin&&"https://www.microsoft.com"!==a.origin)return;if(a.data&&a.data.message&&a.data.status&&a.data.orderInfo&&a.data.orderInfo.orderState&&"done"==a.data.message&&"success"==a.data.status&&"Purchased"==a.data.orderInfo.orderState)try{(r.match(/(ja-jp|de-de|fr-fr|pl-pl|ko-kr)(xbox-game-pass)?$/gi)||r.match(/(en-us|es-mx|en-au|en-ca|fr-ca|en-gb|pt-br|ja-jp|de-de|fr-fr)/gi)&&(r.match(/xbox-game-pass/i)||r.match(/xbox-game-pass(ultimate|core|pc-game-pass)/gi)||r.match(/gamesea-play/i)||r.match(/cloud-gaming/gi)))&&o.requestImage("https://secure.adnxs.com/px?id=1564575&t=2&consent=1")}catch(a){o.debugLog("Error on loading Xandr pixel on purchase confirmation. Error: "+a)}}catch(a){o.debugLog("Error on loading Xandr pixel on purchase confirmation. Error: "+a)}}),!1)}catch(a){o.debugLog("Error on loading Xandr pixel on purchase confirmation. Error: "+a)}};a.catCheckAllExecuteOrPush(t)}}(window.wdgtagging,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript17"](function(event, target, Promise) {
null!=window.wdgtagging&&function(a,t){var e=window.location.pathname;try{if(e.match(/(en-us)/gi)&&(e.match(/xbox-game-pass/i)||e.match(/xbox-game-pass(ultimate|core|pc-game-pass)/gi)||e.match(/gamesea-play/i)||e.match(/cloud-gaming/gi))){var r=function(){t.getRandomNumber=function(){return 1e13*(Math.random()+"")},t.triggerSnapPixel=function(a){try{var e="https://tr.snapchat.com/p?pid=f1a3ab55-8263-4ef0-a556-b8c653ff2e08&ev=";e=e+a+"&v=2.3&rand="+t.getRandomNumber()+"&pl="+window.document.URL+"&u_hem=",t.requestImage(e),t.requestImage("https://tr.snapchat.com/cm/s?pnid=140")}catch(a){t.debugLog("triggerSnapPixel function error: "+a)}},t.triggerSnapPixel("PAGE_VIEW"),$(document).on("mousedown","a.xbstorebuy[href*='JavaScript:void(0)']",(function(){try{t.triggerSnapPixel("ADD_CART")}catch(a){t.debugLog("Error Tagging onmousedown of Join Buttons: "+a)}})),window.addEventListener("message",(function(a){try{if(a.origin&&"https://www.microsoft.com"!==a.origin)return;if(a.data&&a.data.message&&a.data.status&&a.data.orderInfo&&a.data.orderInfo.orderState&&"done"==a.data.message&&"success"==a.data.status&&"Purchased"==a.data.orderInfo.orderState)try{t.triggerSnapPixel("PURCHASE")}catch(a){t.debugLog("Error tagging Snap pixel on purchase complete. Error: "+a)}}catch(a){t.debugLog("Error Tagging XGP Purchase Complete Snap Tag. Error: "+a)}}),!1)};a.catCheckAllExecuteOrPush(r)}}catch(a){t.debugLog("Error tagging Xbox Game Pass - "+a)}}(window.wdgtagging,window.wdgtagging.util);
});</script><script>_satellite["_runScript18"](function(event, target, Promise) {
null!=window.wdgtagging&&function(e,a){var t=window.location.pathname;a.isTargetedPages=function(){try{return t.match(/xbox-game-pass?$/i)||t.match(/xbox-game-pass((pc-game-pass|ultimate))?$/i)?"inPageNavAndPurchase":t.match(/xbox-game-passgames?$/i)?"goToXgpJoinOnNavAndHero":t.match(/promotionslanding-pagegame-passpc-offer?$/i)?"promotions":t.match(/cloud-gaming?$/i)?"purchase":t.match(/gamesall-games?$/i)?"goToXgpJoinOnNavAndHero":!!t.match(/games.+/i)&&"inPageNavAndPurchaseAndGoToXgp"}catch(e){a.debugLog("UET isTargetedPages error: "+e)}},a.isMyPage=a.isTargetedPages(),a.isMyPage&&(a.UETMediaPixel=function(){try{if(o=window,r=document,n="script",s="//bat.bing.com/bat.js",o[i="uetq"]=o[i]||[],g=function(){var e={ti:"137017350"};e.q=o[i],o[i]=new UET(e),o[i].push("pageLoad")},(c=r.createElement(n)).src=s,c.async=1,c.onload=c.onreadystatechange=function(){var e=this.readyState;e&&"loaded"!==e&&"complete"!==e||(g(),c.onload=c.onreadystatechange=null)},(d=r.getElementsByTagName(n)[0]).parentNode.insertBefore(c,d),window.uetq=window.uetq||[],window.uetq.push("consent","default",{ad_storage:"granted"}),a.fireUetEvent=function(e,t){try{window.uetq=window.uetq||[],"none"===t?window.uetq.push("event",e,{}):window.uetq.push("event",e,{event_label:t})}catch(e){a.debugLog("UET mousedown error: "+e)}},a.GamePassDictionary={normalJoinEventLabel:"none",xboxGamePass:{idRegex:/cfq7ttc0k6l8|cfq7ttc0kgq8|cfq7ttc0khs0/i},gamePassIdToEventLabel:{cfq7ttc0k6l8:"none",cfq7ttc0kgq8:"pcgp",cfq7ttc0khs0:"ultimate"},targetGameSelectors:{purchaseLinksOrButtons:"a[onclick*=productId], a[data-xbbigid], a[href*=xbox-game-pass][href*='/p/'], a[href*='game/store']",promotionsPcOffer:"button[data-cta-href*='ms-windows-store://mylibrary'], a[href*='ms-windows-store://mylibrary']",inPageNav:"button[data-cta-href*='#join'], a[href*='#join']",goToXgpJoinPage:"button[data-cta-href*='/xbox-game-pass'][data-cta-href*='xbox.com'], a[href*='/xbox-game-pass'][href*='xbox.com'], [data-js-href*='/xbox-game-pass'][data-js-href*='xbox.com']"},pageTargetSelectorsArray:{inBody:["#PageContent "],promotionsPcOffer:["button[data-cta-href*='ms-windows-store://mylibrary']","a[href*='ms-windows-store://mylibrary']"],inPageNav:["button[data-cta-href*='#join']","a[href*='#join']"],goToXgpJoinPage:["button[data-cta-href*='/xbox-game-pass']","a[href*='/xbox-game-pass'][href*='xbox.com']"],goToXgpJoinOnNavAndHero:["button[data-cta-href*='/xbox-game-pass']",".m-hero-item a[href*='/xbox-game-pass']"],purchase:["a[onclick*=productId], a[data-xbbigid]","a[href*=xbox-game-pass][href*='/p/']","a[href*='game/store']"],dataJsHref:["[data-js-href*='/xbox-game-pass'][data-js-href*='xbox.com']"]}},a.getProductIdFromElem=function(e){try{var t=null;return $(e).attr("href")&&!$(e).attr("href").match(/javascript/i)?t=$(e).attr("href").match(a.GamePassDictionary.xboxGamePass.idRegex):$(e).attr("onclick")&&(t=$(e).attr("onclick").match(a.GamePassDictionary.xboxGamePass.idRegex)),null!==t&&t[0]}catch(e){a.debugLog("UET setup getProductIdFromElem error: "+e)}},a.isUetTargetLinkOrButtton=function(e){try{if($(e).is(a.GamePassDictionary.targetGameSelectors.purchaseLinksOrButtons))return a.getProductIdFromElem(e);if($(e).is(a.GamePassDictionary.targetGameSelectors.promotionsPcOffer))return!0;if($(e).is(a.GamePassDictionary.targetGameSelectors.inPageNav)&&!window.location.pathname.match(/cloud-gaming/))return!0;if($(e).is(a.GamePassDictionary.targetGameSelectors.goToXgpJoinPage)){var t=$(e).attr("data-cta-href")||$(e).attr("href")||$(e).attr("data-js-href");if(t||(t=$(e).attr("href")),t&&t.match(/xbox-game-pass?$/i))return!0}return!1}catch(e){a.debugLog("UET setup isUetTargetLinkOrButton error: "+e)}},a.getMySelectors=function(e){try{var t="",o={inPageNavAndPurchase:["inPageNav","purchase"],goToXgpJoinOnNavAndHero:["goToXgpJoinOnNavAndHero","dataJsHref"],promotions:["promotionsPcOffer"],purchase:["purchase"],inPageNavAndPurchaseAndGoToXgp:["inPageNav","purchase","goToXgpJoinPage","dataJsHref"]}[e],r=a.GamePassDictionary.pageTargetSelectorsArray;for(let e=0;e<o.length;e++){var n=r[o[e]];for(let a=0;a<n.length;a++)t=t+r.inBody+n[a],e===o.length-1&&a===n.length-1||(t+=", ")}return t}catch(e){a.debugLog("UET setup getMySelectors error: "+e)}},a.uetSelectors=a.getMySelectors(a.isMyPage),$(document).on("mousedown",a.uetSelectors,(function(e){try{if($(this).is("[data-js-href]")&&$(e.target).closest("a").length>0)return;var t=a.isUetTargetLinkOrButtton(this);if(!t)return;"boolean"==typeof t&&t?a.fireUetEvent("join_now",a.GamePassDictionary.normalJoinEventLabel):"string"==typeof t&&(t=t.toLowerCase(),a.fireUetEvent("join_now",a.GamePassDictionary.gamePassIdToEventLabel[t]))}catch(e){a.debugLog("UET tag error: "+e)}})),window.addEventListener("message",(function(e){try{if(e.origin&&"https://www.microsoft.com"!==e.origin)return;if(e.data&&e.data.message&&e.data.status&&e.data.orderInfo&&e.data.orderInfo.orderState&&"done"==e.data.message&&"success"==e.data.status&&"Purchased"==e.data.orderInfo.orderState){var t="";e.data.orderInfo&&e.data.orderInfo.lineItems.length&&e.data.orderInfo.lineItems[0].productId&&(t=e.data.orderInfo.lineItems[0].productId),"string"==typeof t&&(t=t.toLowerCase());var o=a.GamePassDictionary.gamePassIdToEventLabel[t];o&&o.length&&a.fireUetEvent("purchase",o)}}catch(e){a.debugLog("Error Tagging UET Purchase event: "+e)}}),!1),t.match(/gamescandy-crush-games?$/i)){var e="a[href*='/apps.microsoft.com/'], a[href*='/apps.apple.com/'], a[href*='/play.google.com/'], section[data-js-href]";$(document).on("mousedown",e,(function(e){try{if($(e.target).closest("[href]").length&&$(this).is("[data-js-href]"))return;a.fireUetEvent("click","download")}catch(e){a.debugLog("Error Tagging UET on Download event: "+e)}}))}}catch(e){a.debugLog("UET setup error: "+e)}var o,r,n,s,i,g,c,d},e.catCheckAllExecuteOrPush(a.UETMediaPixel))}(window.wdgtagging,window.wdgtagging.util);
});</script><script>_satellite["_runScript19"](function(event, target, Promise) {
null!=window.wdgtagging&&function(e,t){var a=window.location.pathname;t.isTargetedGamePages=function(){try{return!!a.match(/games(nba-2k24|call-of-duty-modern-warfare-iii)?$/i)}catch(e){t.debugLog("UET isTargetedPages error: "+e)}},t.isMyGamePage=t.isTargetedGamePages(),t.isMyGamePage&&(t.gameUETMediaPixel=function(){try{t.fireGameUetEvent=function(e,a,r,n){try{if(!(e&&a&&r&&n))return;window.uetq=window.uetq||[],window.uetq.push("event",e,{event_label:a,event_value:r,currency:n})}catch(e){t.debugLog("UET mousedown error: "+e)}},t.excludedGameProductIdArray=["cfq7ttc0k6l8","cfq7ttc0kgq8","cfq7ttc0khs0"],t.cleanUpString=function(e){try{return"string"==typeof e&&e.toLowerCase().trim()}catch(e){t.debugLog("cleanUpString function error: "+e)}},t.isGamePassId=function(e){try{var a=t.cleanUpString(e);if(!a)return!1;var r=t.excludedGameProductIdArray.indexOf(a),n=!1;return r>=0&&(n=!0),n}catch(e){t.debugLog("isGamePassId function error: "+e)}},window.addEventListener("message",(function(e){try{if(e.origin&&"https://www.microsoft.com"!==e.origin)return;if(e.data&&e.data.message&&e.data.status&&e.data.orderInfo&&e.data.orderInfo.orderState&&"done"==e.data.message&&"success"==e.data.status&&"Purchased"==e.data.orderInfo.orderState){var a="";if(e.data.orderInfo&&e.data.orderInfo.lineItems.length&&e.data.orderInfo.lineItems[0].productId&&(a=e.data.orderInfo.lineItems[0].productId),t.isGamePassId(a))return;a=t.cleanUpString(a);var r="purchase",n=a,d=e.data.orderInfo.lineItems[0].listPrice,o=e.data.orderInfo.currencyCode;t.fireGameUetEvent(r,n,d,o)}}catch(e){t.debugLog("Error Tagging Game UET Purchase event: "+e)}}),!1)}catch(e){t.debugLog("Game UET setup error: "+e)}},e.catCheckAllExecuteOrPush(t.gameUETMediaPixel))}(window.wdgtagging,window.wdgtagging.util);
});</script><script>_satellite["_runScript20"](function(event, target, Promise) {
null!==window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,i,e){if(window.location.pathname.match(/promotionsvisit-xboxpostcard?/i)){var n,s;(a=a||{}).sdata={};var d=a.sdata;i.scn="Xbox-Postcard-Campaign";var o={q1:"",q2:"",q3:"",q4:"",q5:"",q6:""};t.isxboxpostcardend=t.isxboxpostcardstart=!1,i.initializeQuestions=function(){localStorage.getItem("updateqalist")?(d.questions=JSON.parse(localStorage.getItem("updateqalist")),o=d.questions):((o={}).q1="",o.q2="",o.q3="",o.q4="",o.q5="",o.q6="",d.questions=o)},i.initializeQuestions(),i.xbox_pc_start=function(){try{if(localStorage.clear("stepnumber"),localStorage.clear("updateqalist"),i.initializeQuestions(),d.qalist="",i.updateqalist(),!t.isxboxpostcardstart){var a={behavior:"STARTPROCESS",actionType:"CL",contentTags:{contentName:"postcard-campaign-start",scn:i.scn,scnstp:"postcard-campaign-start",areaName:"body",field2:d.qalist}};window.owap.capturePageAction(this,a),t.isxboxpostcardstart=!0}}catch(t){i.debugLog("Error checking/retrieving the step url param for OneDS. Inside tu.checkIfResultsPage function. Inside windows_element_tagging_help-me-choose script. Error: "+t)}},i.updateqalist=function(){for(var t in d.qalist="",o)d.qalist+=t+":"+o[t]+";";d.qalist=d.qalist.slice(0,-1)},e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"0"===a){i.initializeQuestions(),i.xbox_pc_start(),indx=parseInt(e(".dlist .location-selector .selected").parent("li").index())+1,o.q1="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question1","data-bi-stpnum":1,"data-bi-field1":"q1:"+o.q1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".dlist .location-selector .selected").find("img").attr("alt"))})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"1"==a){indx=e(".mlist .thumbnail.selected").parent("li").index()+1,o.q2="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question2","data-bi-stpnum":2,"data-bi-field1":"q2:"+o.q2,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".mlist .thumbnail.selected").children("p").text())})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"2"==a){indx=parseInt(e(".glist .thumbnail.selected").parent("li").index())+1,o.q3="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question3","data-bi-stpnum":3,"data-bi-field1":"q3:"+o.q3,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".glist .thumbnail.selected").find("img").attr("alt"))})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"3"==a){indx=parseInt(e(".qlist .thumbnail.selected").parent("li").index())+1,o.q4="a"+indx,i.updateqalist();var n="q4:"+o.q4,s=e.trim(e(".m-area-heading:visible").find("h2").text()),l=i.tlcStr(e(".qlist .thumbnail.selected").find("img").attr("alt"));e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question4","data-bi-stpnum":4,"data-bi-field1":n,"data-bi-field2":d.qalist,"data-bi-field3":s,"data-bi-field4":l})}localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.oneds.sdata.questions)),localStorage.setItem("stepnumber","alreadysignedin")})),e(document).on("mousedown","button#signinbtn",(function(){var t=e(".signinsection:visible").find("h2").text();n=null!==t?e.trim(t):"",o.q5="a1",field1="q5:"+o.q5,i.updateqalist(),s=e(this).attr("data-bi-name")||i.tlcStr(e(this).text()),e(this).attr({"data-bi-bhvr":"SIGNIN","data-bi-scn":i.scn,"data-bi-stpnum":5,"data-bi-scnstp":"question5","data-bi-field1":field1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":s}),localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.oneds.sdata.questions)),localStorage.setItem("stepnumber","signinstep")})),e(document).on("mousedown","#skipbtn",(function(){o.q5="a2",i.updateqalist();var t=e(".signinsection:visible").find("h2").text();n=null!==t?e.trim(t):"",field1="q5:"+o.q5,s=e(this).attr("data-bi-name")||i.tlcStr(e(this).text()),e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-stpnum":5,"data-bi-scnstp":"question5","data-bi-field1":field1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":s}),localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.oneds.sdata.questions))})),e(document).on("mouseenter",".finalsection:not([data-wdg*='end'])",(function(){e(this).attr("data-wdg","end");var t=6,a={behavior:"COMPLETEPROCESS",uri:location.href,actionType:"O",contentTags:{contentName:"postcard-campaign-result",scn:i.scn,stpnum:t,scnstp:"postcard-campaign-result",areaName:"body",field2:d.qalist,field3:"Download",field4:"Visit Xbox"}};window.owap.capturePageAction(this,a)})),e(document).on("mousedown","#downloadbtn,#btnVisitXbox",(function(){var t=6,a="downloadbtn"==e(this).attr("id")?"fc:primary":"fc:secondary";o.q6=a,i.updateqalist(),e(this).attr({"data-bi-bhvr":"CLICK","data-bi-stpnum":t,"data-bi-scn":i.scn,"data-bi-scnstp":"postcard-campaign-result","data-bi-field1":a,"data-bi-field2":d.qalist}),localStorage.clear("updateqalist"),localStorage.clear("stepnumber")})),e(document).on("mousedown","#gobackbtn2",(function(){var t=parseInt(e(".parsed:visible").attr("data-index"))+1,a=e.trim(e(".m-area-heading:visible").find("h2").text()),n=e(".thumbnail.selected:visible").children("p").text()||e(".thumbnail.selected:visible").find("img").attr("alt");e(this).attr({"data-bi-scn":i.scn,"data-bi-scnstp":"question"+[t].toString(),"data-bi-stpnum":t,"data-bi-field3":a,"data-bi-field4":i.tlcStr(n)})})),e(document).on("mousedown",".thumbnail",(function(){var t=e(this).attr("alt")?e(this).attr("alt"):e(this).find("img").attr("alt");t||(t=e(this).find("p").text());var a={behavior:"CLICK",actionType:"CL",contentTags:{contentName:i.tlcStr(t),scn:i.scn,areaName:"body"}};window.owap.capturePageAction(this,a)}))}}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript21"](function(event, target, Promise) {
window.location.pathname.match(/help-me-choose/i)&&null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(t,a,e,n){jQuery("META[name='awa-pageType']").length<1&&e.setMetaTag("awa-pageType","HMC-page"),(a=a||{}).sdata={};var i=a.sdata;i.questions={};var o=i.questions;n("[data-scn-stepnum]").each((function(){var t="q"+n(this).attr("data-scn-stepnum");o[t]=""})),i.f2="",n(document).on("mousedown",".questioncontent .startquestions",(function(){n(this).attr({"data-bi-bhvr":"STARTPROCESS","data-bi-scn":"hmc"})})),n(document).on("mousedown","button.qoption",(function(){try{0==n(this).attr("aria-pressed")?n(this).attr("data-mld-sorder",null):n(this).attr("data-mld-sorder",Date.now());let t=n(this).attr("name");t&&n(this).attr("data-bi-ecn",t);let a=n(this).attr("aria-pressed");n(this).attr("data-select-button-multiselect")?"false"===a?n(this).attr("data-bi-bhvr","APPLY"):n(this).attr("data-bi-bhvr","REMOVE"):"false"===a&&n(this).attr("data-bi-bhvr","APPLY")}catch(t){e.debugLog("Error in Tagging options : ",+t)}})),n(document).on("mousedown",".buyBoxPurchases a:not([data-bi-compnm]), .crossGalaxy a:not([data-bi-compnm]), .crossModules a:not([data-bi-compnm]), .recredo a:not([data-bi-compnm])",(function(){try{n(this).is(".buyBoxPurchases a")?n(this).attr("data-bi-compnm","Recommendations"):n(this).is(".crossGalaxy a")?n(this).attr("data-bi-compnm","crossGalaxy"):n(this).is(".crossModules a")?n(this).attr("data-bi-compnm","crossModules"):n(this).is(".recredo a")&&n(this).attr("data-bi-compnm","re_take_quiz")}catch(t){e.debugLog("Error in adding component name : ",+t)}})),n(document).on("mousedown","a.qbackbutton, a.qcontinue",(function(t){try{if(n(this).hasClass("f-disabled")||3===t.which||2===t.which||2===t.button||1===t.button)return void n(this).attr("data-bi-dnt","");n(this).removeAttr("data-bi-dnt");var a=n("[id*=question]:visible"),s=a.attr("id"),r=a.attr("data-scn-stepnum"),d="q"+r,c="",h="",u=[],g={},l=a.find("h2:visible").text().trim();n("[id*=question]:visible").find("button.qoption").each((function(t){var a=this,e=t+1;if("true"==n(a).attr("aria-pressed")){c+="a"+e+",";var i=n(a).attr("name")?n(a).attr("name").trim():n(a).text().trim();h+=i+",";var o=n(a).attr("data-mld-sorder");o&&(u.push(parseInt(o)),g[o]=i)}})),c.lastIndexOf(",")&&h.lastIndexOf(",")&&(c=c.slice(0,-1),h=h.slice(0,-1)),o[d]=c;var m="";for(var b in o)m+=b+":"+o[b]+";";m.slice(0,-1);var p=n(".question:visible span[data-question-name]:visible").attr("data-question-name").trim(),w="";n(".qoption:visible[aria-pressed='true']").each((function(t,a){t>0&&(w+=","),w+=n(a).attr("name")}));var f=d+":"+c;i.f2=m;var v,C,E,y=l;u.sort((function(t,a){return t-a})),v=g[u[0]]||null,C=g[u[1]]||null,E=g[u[2]]||null;var q=p+": "+w,P="";"1"==a.attr("data-scn-stepnum")&&n(this).hasClass("qbackbutton")?P="SCENARIOCANCEL":"6"==a.attr("data-scn-stepnum")&&n(this).hasClass("qcontinue")?(i.listenForHashChangeEvent(),P="PROCESSCHECKPOINT",i.attachedCompleteProcess||i.listenForHashChange(),i.attachedCompleteProcess=!0):P="PROCESSCHECKPOINT",n(this).attr({"data-bi-scn":"hmc","data-bi-bhvr":P,"data-bi-scnstp":s,"data-bi-stpnum":r,"data-bi-field1":f,"data-bi-field2":i.f2,"data-bi-field3":y,"data-bi-field4":v,"data-bi-field5":C,"data-bi-field6":E,"data-bi-field7":q})}catch(t){e.debugLog("Error in the scenario checkpoint tagging : ",+t)}})),i.listenForHashChangeEvent=function(){try{i.attachedCompleteProcess||n(window).one("sHashChange",(function(){i.pageName=t.getData("gpn")||"help-me-choose/home";var a=window.location.href.split("#")[1],e={pageName:i.pageName,pageType:"hmc-result-xbox-series-"+a};window.owap.getWebAnalyticsExtension().updateCoreDataConfig(e);var n={behavior:"COMPLETEPROCESS",uri:location.href,pageName:i.pageName,actionType:"O",contentTags:{contentName:"hmc-result",scn:"hmc",stpnum:8,areaName:"body",field1:a}};window.owap.capturePageAction(null,n)}))}catch(t){e.debugLog("Error in scenario complete tagging :",+t)}},i.listenForHashChange=function(){i.tid=setInterval((function(){window.location.href.split("#")[1]&&(n(window).trigger("sHashChange"),clearInterval(i.tid))}),500)},n(document).on("click",".recredo a",(function(){try{for(var t in i.f2="",i.attachedCompleteProcess=!1,o)o[t]="";window.owap.getWebAnalyticsExtension().updateCoreDataConfig({pageType:"HMC-page"})}catch(t){e.debugLog("Error in Re take quiz tagging : ",+t)}})),n(document).on("mousedown",".recs.buyBox a",(function(){try{var t="hmc",a="hmc-result",o="9",s="fc:";s+=n(this).attr("data-bi-name")||n(this).text().trim();var r=i.f2+";"+s;n(this).attr({"data-bi-scn":t,"data-bi-scnstp":a,"data-bi-stpnum":o,"data-bi-field2":r,"data-bi-field1":s})}catch(t){e.debugLog("Error in Result page tagging : ",+t)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript22"](function(event, target, Promise) {
null!=window.wdgtagging&&(window.wdgtagging.oneds=window.wdgtagging.oneds||{},function(e,t,a){if(window.location.pathname.match(/xbox-game-passinvite-your-friends/i)){t.hasFiredStartProcessBp=!1,t.setOneDsPageType=function(e){try{myPageType=t.pTValue,"string"==typeof e&&(myPageType=e),window.owap.getWebAnalyticsExtension().updateCoreDataConfig({pageType:myPageType})}catch(e){t.debugLog("setOneDsPageType error: "+e)}},t.fireStartProcessEvent=function(){try{var e={behavior:"STARTPROCESS",actionType:"CL",contentTags:{contentName:t.pTValue,scn:"buddyPassUserStatus",scnstp:"visit-start",areaName:"body"}};window.owap.capturePageAction(null,e),t.hasFiredStartProcessBp=!0}catch(e){t.debugLog("fireStartProcessEvent error: "+e)}},t.setOneDsPageTypeAndFireStartProcessEvent=function(){try{t.setOneDsPageType(),t.fireStartProcessEvent()}catch(e){t.debugLog("setOneDsPageTypeAndFireStartProcessEvent error:"+e)}},t.userStateVisit=function(){try{var e="buddyPass-undefined";if(a(".m-banner").attr("data-bp-user-type")&&(e=a(".m-banner").attr("data-bp-user-type")),a(".m-banner h2").attr("data-bp-user-type")&&(e=a(".m-banner h2").attr("data-bp-user-type")),a(".m-banner .c-group").attr("data-bp-user-type")&&(e=a(".m-banner .c-group").attr("data-bp-user-type")),"buddyPass-undefined"===e||t.hasFiredStartProcessBp)return;t.pTValue=e,t.setOneDsPageTypeAndFireStartProcessEvent()}catch(e){t.debugLog("userStateVisit error: "+e)}},t.userStateVisit();try{if(!t.hasFiredStartProcessBp){t.checkBuddyPassUserStateCounter=0;var r=setInterval((function(){t.checkBuddyPassUserStateCounter++,t.checkBuddyPassUserStateCounter>200||t.hasFiredStartProcessBp?clearInterval(r):t.userStateVisit()}),50)}}catch(e){t.debugLog("checkBuddyPassUserState timing loop error: "+e)}}}(window.wdgtagging,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript23"](function(event, target, Promise) {
null!==window.wdgtagging&&(window.wdgtagging.jsll=window.wdgtagging.jsll||{},function(t,a,i,e){if(window.location.pathname.match(/promotionsvisit-xboxpostcard?/i)){var n,s;(a=a||{}).sdata={};var d=a.sdata;i.scn="Xbox-Postcard-Campaign";var l={q1:"",q2:"",q3:"",q4:"",q5:"",q6:""};t.isxboxpostcardend=t.isxboxpostcardstart=!1,i.initializeQuestions=function(){localStorage.getItem("updateqalist")?(d.questions=JSON.parse(localStorage.getItem("updateqalist")),l=d.questions):((l={}).q1="",l.q2="",l.q3="",l.q4="",l.q5="",l.q6="",d.questions=l)},i.initializeQuestions(),i.xbox_pc_start=function(){try{if(localStorage.clear("stepnumber"),localStorage.clear("updateqalist"),i.initializeQuestions(),d.qalist="",i.updateqalist(),!t.isxboxpostcardstart){var a={behavior:awa.behavior.STARTPROCESS,actionType:awa.actionType.CLICKLEFT,contentTags:{contentName:"postcard-campaign-start",scn:i.scn,scnstp:"postcard-campaign-start",areaName:"body",field2:d.qalist}};awa.ct.captureContentPageAction(a),t.isxboxpostcardstart=!0}}catch(t){i.debugLog("Error checking/retrieving the step url param for jsll. Inside tu.checkIfResultsPage function. Inside windows_element_tagging_help-me-choose script. Error: "+t)}},i.updateqalist=function(){for(var t in d.qalist="",l)d.qalist+=t+":"+l[t]+";";d.qalist=d.qalist.slice(0,-1)},e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"0"===a){i.initializeQuestions(),i.xbox_pc_start(),indx=parseInt(e(".dlist .location-selector .selected").parent("li").index())+1,l.q1="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question1","data-bi-stpnum":1,"data-bi-field1":"q1:"+l.q1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".dlist .location-selector .selected").find("img").attr("alt"))})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"1"==a){indx=e(".mlist .thumbnail.selected").parent("li").index()+1,l.q2="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question2","data-bi-stpnum":2,"data-bi-field1":"q2:"+l.q2,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".mlist .thumbnail.selected").children("p").text())})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"2"==a){indx=parseInt(e(".glist .thumbnail.selected").parent("li").index())+1,l.q3="a"+indx,i.updateqalist();var n=e.trim(e(".m-area-heading:visible").find("h2").text());e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question3","data-bi-stpnum":3,"data-bi-field1":"q3:"+l.q3,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":i.tlcStr(e(".glist .thumbnail.selected").find("img").attr("alt"))})}})),e(document).on("mousedown","#gotonextPage",(function(t){var a=e(".parsed:visible").attr("data-index");if(1===t.which&&"3"==a){indx=parseInt(e(".qlist .thumbnail.selected").parent("li").index())+1,l.q4="a"+indx,i.updateqalist();var n="q4:"+l.q4,s=e.trim(e(".m-area-heading:visible").find("h2").text()),o=i.tlcStr(e(".qlist .thumbnail.selected").find("img").attr("alt"));e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-scnstp":"question4","data-bi-stpnum":4,"data-bi-field1":n,"data-bi-field2":d.qalist,"data-bi-field3":s,"data-bi-field4":o})}localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.jsll.sdata.questions)),localStorage.setItem("stepnumber","alreadysignedin")})),e(document).on("mousedown","button#signinbtn",(function(){var t=e(".signinsection:visible").find("h2").text();n=null!==t?e.trim(t):"",l.q5="a1",field1="q5:"+l.q5,i.updateqalist(),s=e(this).attr("data-bi-name")||i.tlcStr(e(this).text()),e(this).attr({"data-bi-bhvr":"SIGNIN","data-bi-scn":i.scn,"data-bi-stpnum":5,"data-bi-scnstp":"question5","data-bi-field1":field1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":s}),localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.jsll.sdata.questions)),localStorage.setItem("stepnumber","signinstep")})),e(document).on("mousedown","#skipbtn",(function(){l.q5="a2",i.updateqalist();var t=e(".signinsection:visible").find("h2").text();n=null!==t?e.trim(t):"",field1="q5:"+l.q5,s=e(this).attr("data-bi-name")||i.tlcStr(e(this).text()),e(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-scn":i.scn,"data-bi-stpnum":5,"data-bi-scnstp":"question5","data-bi-field1":field1,"data-bi-field2":d.qalist,"data-bi-field3":n,"data-bi-field4":s}),localStorage.setItem("updateqalist",JSON.stringify(wdgtagging.jsll.sdata.questions))})),e(document).on("mouseenter",".finalsection:not([data-wdg*='end'])",(function(){e(this).attr("data-wdg","end");var t=6,a={behavior:awa.behavior.COMPLETEPROCESS,uri:location.href,actionType:"O",contentTags:{contentName:"postcard-campaign-result",scn:i.scn,stpnum:t,scnstp:"postcard-campaign-result",areaName:"body",field2:d.qalist,field3:"Download",field4:"Visit Xbox"}};awa.ct.captureContentPageAction(a)})),e(document).on("mousedown","#downloadbtn,#btnVisitXbox",(function(){var t=6,a="downloadbtn"==e(this).attr("id")?"fc:primary":"fc:secondary";l.q6=a,i.updateqalist(),e(this).attr({"data-bi-bhvr":awa.behavior.CLICK,"data-bi-stpnum":t,"data-bi-scn":i.scn,"data-bi-scnstp":"postcard-campaign-result","data-bi-field1":a,"data-bi-field2":d.qalist}),localStorage.clear("updateqalist"),localStorage.clear("stepnumber")})),e(document).on("mousedown","#gobackbtn2",(function(){var t=parseInt(e(".parsed:visible").attr("data-index"))+1,a=e.trim(e(".m-area-heading:visible").find("h2").text()),n=e(".thumbnail.selected:visible").children("p").text()||e(".thumbnail.selected:visible").find("img").attr("alt");e(this).attr({"data-bi-scn":i.scn,"data-bi-scnstp":"question"+[t].toString(),"data-bi-stpnum":t,"data-bi-field3":a,"data-bi-field4":i.tlcStr(n)})})),e(document).on("mousedown",".thumbnail",(function(){var t=e(this).attr("alt")?e(this).attr("alt"):e(this).find("img").attr("alt");t||(t=e(this).find("p").text());var a={behavior:awa.behavior.CLICK,actionType:"CL",contentTags:{contentName:i.tlcStr(t),scn:i.scn,areaName:"body"}};awa.ct.captureContentPageAction(a)}))}}(window.wdgtagging,window.wdgtagging.jsll,window.wdgtagging.util,window.jQuery));
});</script><script>_satellite["_runScript24"](function(event, target, Promise) {
null!=window.wdgtagging&&null!=window.wdgtagging.facebook&&function(t,a,e,n){try{e.globalpixelId="1770559986549030",a.fbAddToCart=function(n,o){try{var g=a.getProductInfo(n),i={content_name:t.getData("gpn")||"",content_id:g.id||n.attr("data-bi-prodid")||n.attr("data-bi-product")||"",content_type:"product",lang_locale:t.getData("langLoc")||"",partner:g.retailer||n.attr("data-bi-prtnm"),cta:g.cta||n.text().trim()||n.attr("data-bi-name")||""};e.trackEvent("trackSingle",o,"AddToCart",i)}catch(t){a.debugLog("Error tagging xbox facebook games tag - "+t)}};var o=function(){e.init(e.globalpixelId);var o={content_name:t.getData("gpn")||"",market_name:t.getData("loc")||"",lang_locale:t.getData("langLoc")||""};e.trackEvent("trackSingle",e.globalpixelId,"PageView"),e.trackEvent("trackSingle",e.globalpixelId,"ViewContent",o),n(document).on("click","button[data-bi-bhvr], a[data-bi-bhvr], [data-js-href][data-bi-bhvr]:not(.f-precise-click)",(function(t){if("PARTNERREFERRAL"==n(this).attr("data-bi-bhvr")||"220"==n(this).attr("data-bi-bhvr")){if(n(t.target).closest("[href]").length&&n(this).is("[data-js-href]"))return;a.fbAddToCart(n(this),e.globalpixelId)}})),n(document).on("mousedown","li[data-seller]",(function(){a.fbAddToCart(n(this),e.globalpixelId)}))};t.catCheckAllExecuteOrPush(o)}catch(t){a.debugLog("Error tagging xbox facebook games tag - "+t)}}(window.wdgtagging,window.wdgtagging.util,window.wdgtagging.facebook,window.jQuery);
});</script><script>_satellite["_runScript25"](function(event, target, Promise) {
null!=window.wdgtagging&&null!=window.wdgtagging.dcm&&function(e,t,a,r){var o=function(){var e=window.location.pathname,o=window.location.hostname;try{if(a.addToCartSelectors=["button[data-bi-bhvr='PARTNERREFERRAL']","a[data-bi-bhvr='PARTNERREFERRAL']","[data-js-href][data-bi-bhvr='PARTNERREFERRAL']:not(.f-precise-click)","a[href*='microsoftstore']:not(#headerArea a):not([data-bi-bhvr='PARTNERREFERRAL'])","a[href*='microsoft.com'][href*='/store/']:not(#headerArea a, [data-bi-bhvr='PARTNERREFERRAL'])","a[data-retailer][data-retailer!='']:not([data-bi-bhvr='PARTNERREFERRAL'])",".sku-chooser__panel [data-xbbigid][onclick*='OpenWithExp']:not([data-bi-bhvr='PARTNERREFERRAL'])",".sku-chooser__panel [onclick*='OpenWithExp'].xbstorebuy:not([data-bi-bhvr='PARTNERREFERRAL'])","a[onclick*=xboxContextualStore]:not([data-bi-bhvr='PARTNERREFERRAL'])",".sku-chooser__panel .xbstorebuy:not([data-bi-bhvr='PARTNERREFERRAL'])"],a.addToCartSelectors=a.addToCartSelectors.join(),(e.match(/..-..promotionssalessales-and-specials?/gi)||e.match(/..-..consoles(xbox-one-x|xbox-one-s|xbox-one)(((?!backward-compatibility).)*|)/gi)||e.match(/..-..promotionssales.*?/gi)||e.match(/..-..e3($|.*)/gi)||e.match(/..-..gear?$/gi)||o.match(/gear.xbox.com/gi))&&(t.genericSrc="8391491",t.genericType="xbxp",t.catPageLoad="lp_std",t.catPurchaseNow="pchn_std",t.catPurchaseOptions="pcho_std",t.trackView(t.genericSrc,t.genericType,t.catPageLoad),r(document).on("mousedown",a.addToCartSelectors,(function(e){r(e.target).closest("[href]").length&&r(this).is("[data-js-href]")||t.trackEvent(t.genericSrc,t.genericType,t.catPurchaseNow,null,this)})),r(document).on("mousedown",".ps-widget.ps-enabled",(function(){t.trackEvent(t.genericSrc,t.genericType,t.catPurchaseOptions,null,this)})),r(document).on("mousedown","li[data-seller]",(function(e){r(e.target).closest("a").is("a")||r(e.target).is("a")||r(e.target).closest("button").is("button")||r(e.target).is("button")?e.preventDefault():t.trackEvent(t.genericSrc,t.genericType,t.catPurchaseNow,null,this)}))),e.match(/(..-.*)xbox-game-pass?/gi))try{t.xgpGenericSrc="8406391",t.xgpGenericType="xgpg",t.xgpCatPageLoad="gplp_std",t.xgpCatPurchaseNow="pchn_std",t.trackView(t.xgpGenericSrc,t.xgpGenericType,t.xgpCatPageLoad),r(document).on("mousedown",a.addToCartSelectors,(function(e){try{if(r(e.target).closest("[href]").length&&r(this).is("[data-js-href]"))return;var o=null;r(this).is(".sku-wrapper .xbstorebuy")&&(o={u26:r(this).parents("li").attr("id")}),t.trackEvent(t.xgpGenericSrc,t.xgpGenericType,t.xgpCatPurchaseNow,o,this)}catch(e){a.debugLog("Error in Global DCM xbox-game-pass mousedown js. Error: "+e)}}))}catch(e){a.debugLog("Error in Global DCM xbox-game-pass js. Error: "+e)}(e.match(/..-..gamesbackward-compatibility?/gi)||e.match(/..-..games(?!xbox-game-pass)/gi))&&(t.gamesGenericSrc="8406391",t.gamesGenericType="xbxgms",t.gamesCatPageLoad="lp_std",t.gamesCatPurchaseNow="pchn_std",t.trackView(t.gamesGenericSrc,t.gamesGenericType,t.gamesCatPageLoad),r(document).on("mousedown",a.addToCartSelectors,(function(e){r(e.target).closest("[href]").length&&r(this).is("[data-js-href]")||t.trackEvent(t.gamesGenericSrc,t.gamesGenericType,t.gamesCatPurchaseNow,null,this)})),r(document).on("mousedown","li[data-seller]",(function(e){r(e.target).closest("a").is("a")||r(e.target).is("a")||r(e.target).closest("button").is("button")||r(e.target).is("button")?e.preventDefault():t.trackEvent(t.gamesGenericSrc,t.gamesGenericType,t.gamesCatPurchaseNow,null,this)}))),e.match(/(..-..|..-.*)live(?|.*)/gi)&&(t.genericLiveSrc="8391497",t.genericLiveType="xlg",t.liveCatPagePLoad="lp_std",t.liveCatPlatPurchaseNow="pchn_std",t.trackView(t.genericLiveSrc,t.genericLiveType,t.liveCatPagePLoad),r(document).on("mousedown",a.addToCartSelectors,(function(e){r(e.target).closest("[href]").length&&r(this).is("[data-js-href]")||t.trackEvent(t.genericLiveSrc,t.genericLiveType,t.liveCatPlatPurchaseNow,null,this)})))}catch(e){a.debugLog("Error in Global Xbox js. Error: "+e)}};e.catCheckAllExecuteOrPush(o)}(window.wdgtagging,window.wdgtagging.dcm,window.wdgtagging.util,window.jQuery);
});</script><script>_satellite["_runScript26"](function(event, target, Promise) {
window.location.pathname.match(/promotionswhat-are-you-playing?/i)&&null!=window.wdgtagging&&function(t,a,n,i){var e="what are you playing Game";i(document).on("mousedown","button#play-now",(function(){try{i(this).attr({"data-bi-bhvr":"STARTPROCESS","data-bi-scn":e,"data-bi-scnstp":"what-are-you-playing-Game-Start"})}catch(t){n.debugLog("Error tagging on what are you playing scenario starting process by clicking on play now CTA. Error: "+t)}})),i(document).on("mousedown","button#submit-answer",(function(){try{var t=i(this).closest("#questions-section").find("#questions-button").attr("data-bi-name");i(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-field1":n.etlcStr(t),"data-bi-scn":e,"data-bi-scnstp":"what-are-you-playing-Game-Question-Selection"})}catch(t){n.debugLog("Error tagging on what are you playing scenario on click of Submit CTA. Error: "+t)}})),i(document).on("mousedown","button#make-guess",(function(){try{var t=i(this).closest("section#questions-section").find("ul#questions-list li.disabled").text().trim().split("?").join(":");i(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-field1":n.etlcStr(t),"data-bi-scn":e,"data-bi-scnstp":"what-are-you-playing-Game-Make-Guess"})}catch(t){n.debugLog("Error tagging on what are you playing scenario on click of Make a Guess CTA. Error: "+t)}})),i(document).on("mousedown","button#submit-guess-button",(function(){try{var t=i("div#game-container div.games-container div.selected").attr("data-bi-name");i(this).attr({"data-bi-bhvr":"PROCESSCHECKPOINT","data-bi-field2":n.etlcStr(t),"data-bi-scn":e,"data-bi-scnstp":"what-are-you-playing-Game-Final-Guess"})}catch(t){n.debugLog("Error tagging on what are you playing scenario on click of Submit Final Guess CTA. Error: "+t)}n.resultRetrive()})),n.resultRetrive=function(){try{if(i("section#end-game-container:visible").length>0==!0){var t=window.wdgtagging.getData("gpn")||"promotions/what are you playing",a={behavior:"COMPLETEPROCESS",uri:location.href,pageName:t,actionType:"O"},o={contentName:"what-are-you-playing-Game-Result",scn:e,scnstp:"what-are-you-playing-Game-Results-Page",areaName:"body",field3:i("section#game-title-container h2.c-heading-3").text()+":"+i("section#game-title-container p.c-subheading span.highlight-txt").text()};a.contentTags=o,window.owap.capturePageAction(null,a)}else window.setTimeout((function(){n.resultRetrive()}),500)}catch(t){n.debugLog("Error tagging on what are you playing scenario Final Step. Error: "+t)}},i(document).on("mousedown","button#tryAgainButton",(function(){try{var t=i("section#end-game-container div#end-game-content h2.c-heading").text();i(this).attr({"data-bi-bhvr":"SCENARIOCANCEL","data-bi-field3":n.etlcStr(t),"data-bi-scn":e,"data-bi-scnstp":"what-are-you-playing-Play-Again-CTA-Click"})}catch(t){n.debugLog("Error tagging on what are you playing scenario on click of play again button. Error: "+t)}}))}(window.wdgtagging,window.wdgtagging.oneds,window.wdgtagging.util,window.jQuery);
});</script><iframe id="mecontrol-iframe-0" sandbox="allow-forms allow-scripts allow-same-origin" src="https://login.live.com/me.srf?wa=wsignin1.0&amp;wreply=https%3A%2F%2Fwww.xbox.com&amp;uaid=eb499668-ef40-4285-b2ed-c59c0556ab78&amp;partnerId=xboxcomuhf" style="display: none;"></iframe><div id="batBeacon269253655538" style="width: 0px; height: 0px; display: none; visibility: hidden;"><img id="batBeacon696932435713" width="0" height="0" alt="" src="https://bat.bing.com/action/0?ti=137017350&amp;Ver=2&amp;mid=2634ce19-de69-485f-b020-b5ffd8490c4a&amp;bo=2&amp;sid=9df22090adc711f0821c4bc5fe6293d1&amp;vid=9df25f80adc711f0a513997892e19ae2&amp;vids=0&amp;msclkid=N&amp;uach=pv%3D19.0.0&amp;pi=918639831&amp;lg=en-US&amp;sw=1920&amp;sh=1080&amp;sc=24&amp;tl=Ver%20os%20jogos%20do%20Xbox%20Game%20Pass%20%7C%20Xbox&amp;kw=jogos%20game%20pass,%20cat%C3%A1logo%20do%20xbox%20game%20pass,%20biblioteca%20game%20pass&amp;p=https%3A%2F%2Fwww.xbox.com%2Fpt-BR%2Fxbox-game-pass%2Fgames&amp;r=https%3A%2F%2Fwww.google.com%2F&amp;lt=6457&amp;evt=pageLoad&amp;sv=2&amp;asc=G&amp;cdb=AQAQ&amp;rn=717827" style="width: 0px; height: 0px; display: none; visibility: hidden;"></div></body>
'''
print(sha(html))
# minha_string = "Olá, mundo!"
# minha_string_bytes = minha_string.encode('utf-8')

# print(int(minha_string_bytes))