#include "JPTest.hpp"
#include "Letter.hpp"

using std::cout;
using std::cin;
using std::endl;

namespace jp50{
    JPTest::JPTest(){

    }

    JPTest::~JPTest(){
    }

    void JPTest::init_letters(){

        // a
        letters[0] = new Letter("あ","ｱ","a");
        letters[1] = new Letter("い","イ","i");
        letters[2] = new Letter("う","ウ","u");
        letters[3] = new Letter("え","エ","e");
        letters[4] = new Letter("お","オ","o");

        //ka
        letters[5] = new Letter("か","カ","ka");
        letters[6] = new Letter("き","キ","ki");
        letters[7] = new Letter("く","ク","ku");
        letters[8] = new Letter("け","ケ","ke");
        letters[9] = new Letter("こ","コ","ko");

        //sa
        letters[10] = new Letter("さ","サ","sa");
        letters[11] = new Letter("し","シ","shi");
        letters[12] = new Letter("す","ス","su");
        letters[13] = new Letter("せ","セ","se");
        letters[14] = new Letter("そ","ソ","so");

        //ta
        letters[15] = new Letter("た","タ","ta");
        letters[16] = new Letter("ち","チ","chi");
        letters[17] = new Letter("つ","ツ","tu");
        letters[18] = new Letter("て","テ","te");
        letters[19] = new Letter("と","ト","to");

        //na
        letters[20] = new Letter("な","ナ","na");
        letters[21] = new Letter("に","ニ","ni");
        letters[22] = new Letter("ぬ","ヌ","nu");
        letters[23] = new Letter("ね","ネ","ne");
        letters[24] = new Letter("の","ノ","no");

        //ha
        letters[25] = new Letter("は","ハ","ha");
        letters[26] = new Letter("ひ","ヒ","hi");
        letters[27] = new Letter("ふ","フ","hu");
        letters[28] = new Letter("へ","ヘ","he");
        letters[29] = new Letter("ほ","ホ","ho");

        //ma
        letters[30] = new Letter("ま","マ","ma");
        letters[31] = new Letter("み","ミ","mi");
        letters[32] = new Letter("む","ム","mu");
        letters[33] = new Letter("め","メ","me");
        letters[34] = new Letter("も","モ","mo");

        //ya
        letters[35] = new Letter("や","ヤ","ya");
        letters[36] = new Letter("い","イ","i");
        letters[37] = new Letter("ゆ","ユ","yu");
        letters[38] = new Letter("え","エ","e");
        letters[39] = new Letter("よ","ヨ","yo");

        //ra
        letters[40] = new Letter("ら","ラ","ra");
        letters[41] = new Letter("り","リ","ri");
        letters[42] = new Letter("る","ル","ru");
        letters[43] = new Letter("れ","レ","re");
        letters[44] = new Letter("ろ","ロ","ro");

        //wa
        letters[45] = new Letter("わ","ワ","wa");
        letters[46] = new Letter("い","イ","i");
        letters[47] = new Letter("う","ウ","u");
        letters[48] = new Letter("え","エ","e");
        letters[49] = new Letter("を","ヲ","wo");


    }




    void JPTest::test_letters(){


        int random;

        random = rand() % 50;

        Letter *p = letters[random];

        random = rand() % 3;

        switch(random){
        case 0:
            p->test_first();
            break;
        case 1:
            p->test_second();
            break;
        case 2:
            p->test_roman();
            break;
        default:
            break;
        }
    }



    void JPTest::test_rows(){

        Letter *p;
        int random;
        int index;

        random = rand() % 50;


        if (random >=0 && random < 5) {
            index = 0;
        } else if(random >=5 && random < 10){
            index = 5;
        } else if(random >=10 && random < 15){
            index = 10;
        } else if(random >= 15 && random < 20){
            index = 15;
        } else if(random >= 20 && random < 25){
            index = 20;
        } else if(random >= 25 && random < 30){
            index = 25;
        } else if(random >= 30 && random < 35){
            index = 30;
        } else if(random >= 35 && random < 40){
            index = 35;
        } else if(random >= 40 && random < 45){
            index = 40;
        } else if(random >= 45 && random < 50){
            index = 45;
        }


        cout << "\n\n===>默写出 " << letters[index]->get_roman() << " 行: " << endl;

        for(int i = 0; i <= 4; i++){
            p = letters[index+i];
            p->test_roman();
        }

    }



    void JPTest::test_columns(){

        Letter *p;
        int random;

        random = rand() % 5;

        cout << "\n\n===>默写出 " << letters[random]->get_roman() << " 段: " << endl;

        for(int i=0;i<=9;i++){
            p = letters[random+i*5];
            p->test_roman();
        }


    }

    void JPTest::result(){
        Letter *p;

        cout << "\n\n检验结果: " << endl;

        for (int i=0; i<50;i++){
            if(i%5 ==0){
                cout << endl;
            }

            p = letters[i];
            p->display();

        }
    }
}
