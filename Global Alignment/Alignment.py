import numpy as np
import Blosum62
def BestAlignment(a, b):
    b62 = Blosum62.b62()
    n = len(a)
    m = len(b)
    matrix = np.zeros((m+1, n+1), dtype=int)
    miss = 5
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i == 0 and j == 0:
                continue
            if i == 0:
                matrix[i][j] = matrix[i][j-1] -5
                continue
            if j == 0:
                matrix[i][j] = matrix[i-1][j] - 5
                continue
            if a[j-1] =='-' or b[i-1]=='-':
                match = miss
            else:
                pair = (a[j-1], b[i-1])
                if pair in b62:
                    match = b62[pair]
                else:
                    match = b62[(b[i-1], a[j-1])]


            match = match + matrix[i-1][j-1]
            up = matrix[i - 1][j] - miss
            left = matrix[i][j - 1] - miss
            matrix[i][j] = max(left, up, match)

    s1 = ''
    s2 = ''
    i = m
    j = n
    gaps = []
    while(True):
        if i == 0 and j==0:
            break
        elif i == 0:
            s1 = a[j-1] + s1
            s2 = '-' +s2
            j -= 1
        elif j == 0:
            s1 = '-' + s1
            s2 = b[i-1] + s2
            i -= 1
        else:
            if a[j-1] =='-' or b[i-1]=='-':
                match = miss
            else:
                pair = (a[j - 1], b[i - 1])
                if pair in b62:
                    match = b62[pair]
                else:
                    match = b62[(b[i - 1], a[j - 1])]

            up = matrix[i - 1][j] -5
            left = matrix[i][j-1] -5
            diag = matrix[i - 1][j-1] + match
            mx = max(left,up,diag)

            if mx == left:
                s1 = a[j - 1] + s1
                s2 = '-' + s2
                j -= 1


            elif mx == up:
                s1 = '-' + s1
                s2 = b[i - 1] + s2
                gaps.append(i-1)
                i -= 1



            else:
                s1 = a[j - 1] + s1
                s2 = b[i - 1] + s2
                j -= 1
                i -= 1


    #print(matrix[m][n])
    print(matrix)
    print(s1)
    print(s2)
    return(s1, s2, gaps)




def MSA(sequences):
    allignments = []
    SC = sequences[0]
    for i, S in enumerate(sequences):
        if i == 0:
            continue
        SC, S, gaps = BestAlignment(S, SC)
        if len(allignments)!= 0:
            g = 0
            for j, a in enumerate(allignments):
                st = ''
                for c in range(len(a)):
                    if g < len(gaps):
                        if gaps[g] == c:
                            st = st + '-'
                            g+=1
                            c-=1
                            continue
                    st = st + a[c]
                allignments[j] = st
        allignments.append(S)
    allignments.append(SC)

    for a in allignments:
        print(len(a))
        print(str(a))
    s = 0
    for i in range(len(allignments[0])):
        if allignments[0][i] == allignments[1][i] == allignments[2][i]:
            s+=1
    print(s)






#sequences=['YAFDLGYTCMFPVLLGGGELHIVQKETYTAPDEIAHYIKEHGITYIKLTPSLFHTIVNTASFAFDANFESLRLIVLGGEKIIPIDVIAFRKMYGHTEFINHYGPTEATIGA',
#           'AFDVSAGDFARALLTGGQLIVCPNEVKMDPASLYAIIKKYDITIFEATPALVIPLMEYIYEQKLDISQLQILIVGSDSCSMEDFKTLVSRFGSTIRIVNSYGVTEACIDS',
#           'IAFDASSWEIYAPLLNGGTVVCIDYYTTIDIKALEAVFKQHHIRGAMLPPALLKQCLVSAPTMISSLEILFAAGDRLSSQDAILARRAVGSGVYNAYGPTENTVLS',]

BestAlignment('GGYYYGGMN','YYGGMNG')
#MSA(sequences)


#BestAlignment('KGYNNDGYKADGFAWEQVIRRRTCQRRATYKKQRYWPWRRHNRPWQEHFAVCYYGWHMTEKGLGPYMNGYMETTWCYIEQTWRKDTCIMLCRKRGRKGRMVFRQSWPKIMRCRQHFDFIEHYVQPMKLRIMQYFFAIWCPHKMKLGMRPWCMISPHNQHWILNIYYNYNVFTANISTYIDWDLCNVDFYKVERNYGCIMYLMALYFRNGQGNQMDFTEGVSTCFTMPIQTFEPPHRPDLIILGSLMVAMEERYLLDGTAGPILERPNDPDIRSDSHAGGDREGDKYNYNEFSRYKTQNWRGDNKDKQFMAKHWCYCYDSKMMYDTNTIAYNGIYALDGCSRTIMTDRKTKIFWHFKDAHCKACTWFNMTRFAPSSRSRMSGGHTMWDTLNRSGSICYCKTFDELSTIFCDQFLISNWKNEWWTINCSRKNPTMWVLWCMYMPDPCIQLCEFQFMLVSRCGLICHSNRCGLRANTGDAFGNCAFVVDELKGNIIEEDWGKSASGKLFQHKQEVLTKCCKDTIPAPEKRDRHSNDLFHVKYYTNHNNGFSAPMPRCYGADGHGDWWDMKIMLSANMGKCPMHIEVGIQPVFHWHMEHSACHPVAKGRCLGCMWMTIYTGLFPYCFGFTVKNIDGKGWTVYDWPDYNPPPATELMAYCDFRFTQYAQDWQTEPGIGVKDLYTMIVQWACCYLYFKILCWLLLMGQTYEMHERMMNSLHDWSLYHKTHKYVWDELARPWYMWVYETMAYVSQLTWLGVPYNHLTNPKYEQTHIRQLPIMYHFIGQFFIYFANDPQFIEIMEDSCDKSAQGTGCWWSKPPENLFAMCKQIQRMAQWAPGPMQVWCIGGMMNPTIAIPTEHFMVDVVWSVHHFSYCMPGHDNSGKLHIKADVEMDKDKMHWEGMWGCWVVWALCRWVEASNRHEYPHNLHGICGVGIDNSEKPVRVTWPPDEGKKDTFCPNWIWMSYYFGMTARWRMQVLESHYAGYTISRLILRAGPFCYKDGNVRRGRGPDNDTEQAVVRKIRSTSSYNLLKPKQVFPHFMKIRHMGCSRRQVCWPKCVESLTKPCPIFVRTKLDPCIFLKRCMLACDSLDPYTLGCFCGNLMNRSMAKQMSNVHCKSRDNGAAFWWQSCFMKKGANYGQNCSQYPRNHPRHMRWCTQFIYRNWKAMAICFTYVKDQVTWCDQYARDARYICMITGMKPGLGISGESLQAKKHCHFLKKHQKAGVNHMVTTRSLCPVLHAVNEQYWCIYLSAPKYCTVCMCQEIPNCLCHTWVQCVERDKLCMQNWRRCLMVTTGSFDVPWQREDICQHKSQHYDVWGQTFEGCRLHGGTHTWFWFEGGSSWFFCSNMDHAWFFWNPKSDTGLHFLFGIMIMLIHTMFEMVLCSSAHQLFTAAWWHEENNQLMKTGMVMVMHCLAFTFEGPWHYQTILIYYLMKQIPMICQPGKFNFCLQDQFTIKSGDHRHHSLVSRQYESDEMLNWEDASVNPPHSSKCCLRNAPWKKWWWEANEYCYFVDVGSGSQVPTGCESQSPIKRQNWCAVPFFLHNAGHERCQDQGDAGVSTIYWLNTIWFYGIEPSVNINGMNYYFEDVMYGWQLWKRTPPYGMPNDWYRFKVALDITFAWWYSYALYQQDHWMWSDPHNRVANNGVPQHQNRNSDLDICRDTHFYLTMHMENLTNKRCWLSPNACHVIIFFYRCRSYGCFNYAMMICHLYQEYATQHWQTSKDGRTRNMYRMQTYTSTCMFYKSYGYEACFSAQFVHPLLGAQEYKDFWIIVIMLFCLRELRMFYQLIRPLKFPHLAPETQCVYTEGDWVHWAIRHVHLLDPICFASNQSGMRWDPAFQMGQRWCNAHFCLFWWWCFDHTDMMTATTYKRKCTKCGWHQQLVGLYMGYWFNHGYWVKRPWGQGAGNGIWLACVMINEHSIAVCCKIDVDHTYTWHHLSEMDTHWELDTYSRYYIVHERIQLCYHPIPSCRMCMKPTAPWLGHEWNERCLDMVEKVENFHWANCHQWLALRGKDNNKHPCGGAHGRMFFFMSGCAVGSYYPQGVKTHHPYYENERKDWWWFKLQSSHIYFPFMHMPWTTMVYMADMWRVEKVETRATGGGKSPMEACICCAGNLADNAIYIQRNSLRLLSNWYLGESKQEFMWAPLIGLDWMRCALKYCDGDFIFPGYQKRWAYEMACTEWQGDSVMWVKQIIYFMIHFPQWQQNIHKDHVPTAFEFKRPHPPQWLDREYRINYYTCYLESTLSFACNPQKSWNKVHVMYGGELVHIGAAVVCIEDPGLNDDSQQISIMACTIGHENMSTMHTEPWNVYGGFSMSPWSIMQPIQCCTPTDIWTSNRYPLMWNMTVYRYQKITMDSGQCQNDGAIGHCTMMRMGERDGWASLDVWKCCSKLKSNAYIIKWADWGRNMHILPITKWSHTMKQGMYEGPVYTPKFCQPGQLPGYTGVEHITMGIKCPGDETHQRVGGGYWMHAEQTCGRYIEKLSYPVSATFPWVFDGEQSGRVNMALYLMMVDDILVIDRSPELVWFHQNRGSLHHMGIYQGKSWQSSRCMLEGFDMAFNWDCQMFVDAEVMEYRQVNIPCIVRVDEVWEGSEGNYKSYVESYCQHNQHDQLKTKKLCGCFQRQQQILMVAEPRLITEKEHGDLPQQTEIIMYGWAGLGEKQGQPIWNAGSGDCHLFYKAEGSSQETRRWMMLEKVPAASSITLWCCPGMGYFYFDILDLGGSNKDCGKFTAANAPMDSGIAQNRCKWDHAMWHVHALEQSFHANNALSLRQYYTGHGTPTMNTGSHFMGNSDATLRSIINPPNWWYLFDLACSHTNDNMEMYISESRDSNRSVHGNDDCNMRCKGHVAVPNCPPIPQIETILAKEHCELCGCYMWMILDIVHYAPIYMGTMYHEPTHPLHNAGMTDEWFQFMQVYPGNQHDACLHHCRKIRGWYCWMWPNMGCTSYDKLPKNRWLETHQHTMNVIDDQLIPYNVPHDQVVQGMQKVGGWWAPQAGVEFWAEKHTFRDPRQECASPYHWDVRSWFTKRNEAFMMDDWGNCKHVGHAYQDYWPGSLSDPLMSTKRGLDQQKTTMCQWRSSTKQHMWLENADFRTCPLADNRWDGHIFGFNWKGRTEDYRSYDRKVQRKVIVRLEVDMDHKSPHLDPLPMLNSSPEMEVPTHYIVCFDLWEVLEDIHHHWFVICHKMPSMYNAYHCADDKLEITCRCKMRLSACATQSNGQTARMQCQEPMSLTKCPMFSGFRHIACDQYENDKACGTFHSSMVPKQGNMQHGVISHELLFHHAEGISHTPMESFNYKCIHAKKKCWDELFALHTCIHDWRMHSVTIKIWCRYSEWFALYTNLLSAGQWTALCVHRFKKSAFPPWSFCYESMESPFEIVWMPNRPELCQEEETATWQCYNFCVHMACSWIPCRGTKKGLWNVINYSNKVEVWMAVNQSIMFEYDEECLKDYQPHEWIQMQFMKYAVWYWSESRMNMCKTGKTLWPEFGCSLYMEGNEFMMMACDDVDAYHRCAIHVIMNAKQHLVVFKLRTSLIMERWDFLRHWMFNEECAIHYIHPPTGDNNTSTATMDAAIKVPASYCSCFVKDRMRRLSRIQHYRLAWHHIGLYWGWICICSAFQIALPHMCCWDHWNNMYCYKWEMAHILWDNLKVWCEEQFFFNRTCHCGEFEKACNFGSFIYIGNHQWPWDQETLSGGTEFWTFESYSCYLHMKSHMFGQMIRSGQIRPQRHMHAMQKPLKASGQGDEQFKYEWDKIITDILYKRQNIDCMPIRHTYGNVRVICRQKYVEHWTSIKCMFEHQDDTEDVKCVPMWKQGFSHHGDEVADWLCVIMHCYAMVHENWEFKHVMLCSQLGHVSPTQFKSNILGQTNSPPTEATCCYFLWDVKPFCPHQLAICLHFPELFWDTSHMIRWLPVSWAMCPVERMAARRDYQMWCDWELLLCIPEQIQFGAPQEHQQFRMLEFPHPYNCHCNKNSFCVDKKSGCFFAYFPCHDDWTIHLTDRTWDSHTNHPSPIRFEQPCGWQYILMWCTYDKKQQGW', 'KGYNNDRYKADGFAWEAEIIFVQRRATYKKQRYYFMNDPWRRHNRPWQEHFAVCYYGWRMTEYSPDGLGPTFEQSVHDPLVFCYIYQTRQHCFDYKQRKDTGSGIAWCIMLCRDTRMWDATLHFNFGRKGRMVFRQRQHFDFIEHYEVNWVQPMKLRIMQYCKFFSFAIWCPWTVHRMKLGMRPWCMYSNQHILNIYYNYNVFTANISTYFDWDLCWYKVERNYGPQEVGQGNEMDFTESTCLCFDVTMPNCTFMPPHRPDLIVLSLMVAMEERYLLDGTAGPNDPDIAGGWIREGDKYNYNEHSRYKTQNWRIKIYPIDHWKYCYDSKMQYDTNTYAYNGIYALDGCSRIFWHFKDAHCKAYTWFPKTMTRFAPSIENCNWRRGRMSGGHTMWIYNYCKTFDELSTIFPSQFFLGEWWTIWCSRKNPTMWVLWWWMYMPDPCIQLCEFQFMLVSAHGMQCGNRCGLRANTGDAYSPDIMGNCPTVWMAFVADEDKGNIIPEDWGKSAFGKLFQHEQEVCTKCCFDTIPANKTGIGWLHHGFSAPMGHGDPQTRGSWDMKIMLKANMGKCPMHGGEVGIQPMQDCTGFHRELHMEHSACHPTATISVIKCCYMWMTCNTSELFCTLLGCYCFGFTAKNIDNKGWTVYDWEHEVFMVREKNPTELMAYCDFRFTQYAQDWQTESGIGVKDLSCMRRVQWACCYLYFKILCWLFLMGQTAFVIAQFAPRMMNSLHDWSCQYYHKTGSNAGQPWYMWVYERWLVQWPVMAYVSQLTWLGVHCWVYNFIGQFFITFANDPWPYYEGMFHTNGGSKHIEIMEDSCDKSAPVSKPPENLFAMCKQIQRMAQWAPGPMQNWCIGGMMNVTEGAIPTEHFHFGHGEMDKFWPNLLRGCWVVWALCRWWEAVHKHVRHESITYPHNLSHTYCEGICGVGIHPSLSFHECNMKPVRVTWKKDTFCPNQIWMSYYHYGMTARWRMAHRLREITHVYAGYIDDKKISRLILRAGPFCYKDGNVRNGRGLRCQHNVTEQARKIRSTSSYNLHKPKQVFHFDKIRHLENKAIGCSRRQVCWPKKPCPIVRPKLDPCISRKLACDSLDPYTLGCFCGNLNDPHGHSRDNGADWIVDFWPMCYCNPQQSCFMKKGANYGQNCSQYPRNHPWHMFWCTQFIDRNWKAMSICFTYVKAKVTSCDDARYICKQAIDGQGISFESLQAKKHCRFLKKHQVGVNHMVTTRSLCPVTCAHAVNEQYWCIDLSAPKYCTVCMCQEEPNALCHTWVQCVENARFKVDARGKLDMQYWENWRRCLMVTPWQSMQHGTRLHGGTTNHIFTMNWFWSEGGSSWFFCSNMDHAWFFWNPKSDTGLLIHTVHPWFPTMRVQDRCAMTAAWWHEENNQLMKVMVMHCLSFTFEQTILLYYLHKRYTRPKQIPMILQPGKFNFCLTDQFTIDSGDHRHSDEMLNMEDASVHSSKCFLRNALEWKKWWWEANEYCLGSGSQGMESQSPIKRQNWCAWMFTCASGSEVVHNATHEESTTNWQRCQDQGDAGVSTIYDLHTIWFYGFEPSVNINNMNQRLYFEDVMYGWCLWKRTEPYFMPNDWYRFKVALDITFAYMRWLHAAWYSYALYQQDHWMWYDVPQHQNRWVCIPPTWVHFYLTMSPVGWLSIFFYRMRSYGCFNYAMMIEHLYWEYATQRTRNANWETGDSGYRMQTYTFTCMFYKSSGYEACFSAKFRKINTSRHPLLGAQEYKDFWIIVIMLFCLKGNKCTELRMFYQLIRPLKWPHNRVKSFACEPETQCVYEGDWVHWAIRHVHDSLSGMRWDPAFMAAARGQQNAHFCLFWWWCFDHNFSVMTDMQNDDTATTYKRKMGLHFFVGLYMGYWRLYDNHGYQVKRPWGHKKQNNDGAGNGIWLACVMHSIWQCCKIDVDHTYTWHELSEMDTHWSLDTYVRYYIVHEKIQLPHNKPTAPWLGGEWERCVDQDITHIEIGNSFPEKSYPAENFHWANCHDWLALRGKDNNKHSNYMFAKSGCAVGSYYPQGAPTHHPYYENERKDWWWMVPPQKLQSDAGCVFMVRPWMHMPWTTWKSIVKANVYMADMWRVEKVETRSEYKNLLITGGGKSTMEACHCCAGNLADNAIHIQRNSLRKDSRRWLSYMQMYLFQKWYLGENYLDKECRAWRCPHIVGFMWAKYIGLDWYQKPESSGFHVWPSDCDFIFEIQFTVKQFEHKDYDEIVPTAFEFDYYQKRPHCPQWLDREEMYFYINYYTCYLEQTLSFAHYGGEIAWMWIPGLNDDLLHHLGMSQQISIMADTSGHENMSTIHVQGGFSMSPWSIMQPIQCCTPTDIWTSNRYPLMWNMTVYRYQKEVGVAPQTIDSGYKCQIDASWDCIKHADWGRNMHILPITKWSMMVHMQVAFMKVGMYAGPVYVPKFCQPGQLPMYTGVEHPTSVGGGYWFQPVWATFPWVSDGEYQGALACGRKKDLMMVDTILVIDFFCYKCKSMWFHQNRHHFGIYHGKSWQNSRCMLEGFDMAFNWDCQMVLATVMEYRNIPCIVRVDTVVSCKMSPGNYFSYVESYPRNQHNQHDQLKVQIFLCFKKPLMHTCGCFQRQQQIWRTMSQAEPRLITEKEHGYLGHAGLEKQEQPIWNARVHHYGSAASGDCHLFYKAKGSSQETREWMMLEKVPAASSITLWCCPGMGYFDFDHLDLGGSKQNQPYPVYKYGCGKFTVTANAPMDSQFHSIHQDCYAVIILRCNWMTAMWQMMSQKCVHHPYCLEQSFHAIPALSLRHGQPTMFTGSSLATLRSFDSIPWINPPNWHQNWEMSYLFDLACSHRSFIRRNDNMEMYISESRDSNRSHQQKPHGNDDCKYSMTGHDETILAKEHCSVWELCGCVMWMILDIVHYAPIYMDTMYDVAIMHNLGMRDEWFQIMQVYPKNTHDKPNFPLSLQDISWYCVMWPNMGCSSYDKLPDAIGQNRWLETQHHPMCFPENGMNYMRVIPAMQIPYNVPHDQVVQGNYYALLQKLIIGDGGWKGVEFNAEKHTFGCPPYPALMDPDDWQTMDWGNCKHVGQDASGFYRLRMDPAMSTKRGLDQQMTSSTDQHMWLENADFITCPLADNCWSEYWKHHIFGFNWKGRTEDYRSYDRKWQRKLEVDMDHKSPHLDYTRNRDKMLISSPGMEVPGHYIVCFDLWEVLEDTDSMMTHHPWFVICHKMPSMYNAYHCADDKLEIKCRCKFRLSACATQSNDQRWFCHNDARMQLTKQPMFSGFYHDACMQYFCDKALNDKVPKGGNVISHELLFEEGISHTPMESFNYKCIHAKKKCWDTLFADMHGLCTIHDWRMHSHTIKIWCRYSEWFAKYDDPSLHEYTNLLSAGQWTWLCVHRFPFWLYIKVKSFPYEPRLSHWMPNMTWSYFVVMPELRQEEETATWQCYNFCVHMALSWIPCRGTKKGLWNVINYSNKVEVPANQDDPMLRLQHDKPVAITVNDAIRLLMWKDYQPHIIIQMQFMKYAVWYWSESRMNMKCMAKKTGKTLWPEFGCSLYMEGNEFMMMACDDVDVYARCDIHVIMLWAKVVFKLRTMERWQRHKSEIVFNEEEAIANYIHPPTGDNNTSMACGWLCIVPASDLLHEKDKATSYELANTKYKEHHIWLYWGFICICSYILWEFQIALPHRCCWDMWNNMYGLLILEIDCEEQFFFNRTCCCGEFEKDHPIGLTVGTEFWTFESYSCYLHGQPPRSGQIEPHMHWFQKGLKASGQGDEQFHYEWDKIHQGILYKRQNIDCPIRHTYGNVRVICAADVSHVEPQNYEKWARAHWSSIKDDTGDVKCVPMWKQGFKQHHGDEAAVWLCVIMQSWGMHRWRFSQLGHVSPTVIWIRISWPCQCGQTNSPPTEATCCYFYWDSKPFCPHQLAICLHFIELAWWALYHWEFLSNCKYQLCPVERMAARRDYMWRLCIPEQIQFGAPQEHQQSLEFPHPNCHLGCFFAYFPCHDIETPDIDATMTDSHTSEGGPNTRIKFEQFFGGCWELHWPWQYILMWCFEDKDDKKRQGAPKQG')