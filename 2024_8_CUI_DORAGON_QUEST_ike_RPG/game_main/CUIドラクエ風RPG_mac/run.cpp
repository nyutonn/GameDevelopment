#include <iostream>
// Windows OS の場合は以下のコメントアウトを解除すること
// Mac OS の場合はコメントアウトをすること
// #define WIN
#ifdef WIN
#include <conio.h>
#else
#include <termios.h>
#include <unistd.h>
#endif
#include <cstdlib>
#include <string>
#include <vector>
#include <typeinfo>
#include <chrono>
#include <thread>
#include "PoolAllocator.h" // 自分が作成した Poolアロケータが使われていること(必須)
#include <random>

// 状態の列挙
enum State{
    State_Start, // スタート
    State_Field, // フィールド：歩く
    State_Battle, // 戦闘
    State_Result, // 結果
    State_LevelUp, // レベルアップ
    State_GameOver, // ゲームオーバー
    State_GameClear, // ゲームクリア
    State_End, // ゲーム終了画面
};
// 現在の状態
State current_state = State_Start;



// 関数
// カーソルの表示/非表示を制御する関数
void setCursorVisibility(bool visible) {
    if (visible) {
        std::cout << "\x1b[?25h"; // カーソルを表示
    } else {
        std::cout << "\x1b[?25l"; // カーソルを非表示
    }
}

// カーソル位置を指定する関数
void setCursorPosition(int y, int x) {
    std::cout << "\x1b[" << y << ";" << x << "H";
}

// キー入力を非ブロッキングで取得するための関数
char getKey() {
#ifndef WIN
    struct termios oldt, newt;
    char ch;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO); // 非ブロッキングに設定
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return ch;
#else
    char ch = 0;
    //if (_kbhit()) {
        ch = (char)_getch();
    //}
    return ch;
#endif
}

// プログラムを停止する
void timeSleep(int seconds) {
    std::this_thread::sleep_for(std::chrono::seconds(seconds));
}

// 全画面クリア
void ScreenAllClear(){
    std::cout << "\x1b[2J" << std::flush;
}

// 画面描画
// 同じ行に続けて入力したい場合に備えて，入力文字数を返す
int ScreenWrite(int y, int x, std::string s){
    std::cout << "\x1b[" << y << ";" << x << "H" << s;
    return s.length();
}

// プレイヤーと敵の表示
void ScreenPointDraw(int new_x, int new_y, char c){
    std::cout << "\x1b[" << new_y << ";" << new_x << "H" << c; // 今の座標に c と表示
}

// 四角の範囲を消す
void ScreenSquareClear(int y, int x, int height, int width){
    for(int j=1; j<=height; j++){
        for(int i=1; i<=width; i++){
            std::cout << "\x1b[" << y + j << ";" << x + i << "H" << " "; // 消去
        }
    }
}

// 戦闘画面の描画
void ButtleScreenDraw(std::string m1, std::string m2, std::string m3, std::string m4){
    ScreenSquareClear(8, 1, 4, 50); // 戦闘画面の初期化
    int y_window = 9; // 戦闘画面の左上の座標
    int x_window = 3; // 戦闘画面の左上の座標
    ScreenWrite(y_window, x_window, m1);
    ScreenWrite(y_window + 1, x_window, m2);
    ScreenWrite(y_window + 2, x_window, m3);
    ScreenWrite(y_window + 3, x_window, m4);
}

// // 四角で枠線を囲む
void ScreenSquareDraw(int y, int x, int height, int width){
    // 横線 ------
    for(int i=0; i<=width + 1; i++){
        std::cout << "\x1b[" << y << ";" << x + i << "H" << "-"; // - と表示
    }
    // 縦線 |
    for(int j=1; j<=height; j++){
        std::cout << "\x1b[" << y + j << ";" << x << "H" << "|"; // | と表示
        std::cout << "\x1b[" << y + j << ";" << x + width + 1 << "H" << "|"; // - と表示
    }
    // 横線
    for(int i=0; i<=width + 1; i++){
        std::cout << "\x1b[" << y + height + 1 << ";" << x + i << "H" << "-"; // - と表示
    }
}



// ステータス画面表示
template<typename T>
std::string Status2String(T* player_ptr){
    return {
        "名前: " + player_ptr->name + 
        " Lv." + std::to_string(player_ptr->level) + 
        ", HP: " + std::to_string(player_ptr->hp) + "/" + std::to_string(player_ptr->maxhp) + 
        ", MP: " + std::to_string(player_ptr->mp) + "/" + std::to_string(player_ptr->maxmp) +
        ", 攻撃力: " + std::to_string(player_ptr->power) +
        ", 防御力: " + std::to_string(player_ptr->block) +
        ", X: " + std::to_string(player_ptr->x) +
        ", Y: " + std::to_string(player_ptr->y) +
        ", EXP: " + std::to_string(player_ptr->exp)
    };
}




// クラスの多態性を用いたオブジェクト管理が入っていること(任意)
// 基本ステータス
class StatusBase {
public:
    StatusBase(const std::string& name)
        : name(name), maxhp(10), maxmp(10), hp(10), mp(10), power(1), block(0), exp(0) {}

    // 攻撃するメソッド
    virtual int attack(StatusBase* other) {
        int damage = std::max(power - other->block, 1);
        other->hp = std::max(0, other->hp - damage);
        return damage;
    }

    // MPを使って回復するメソッド
    virtual int heal() {
        // std::cout << "回復魔法を使用" << std::endl;
        if (mp >= 3) {
            int healAmount = (maxhp / 2) + level;
            mp -= 3;
            hp = std::min(maxhp, hp + healAmount);
            // std::cout << name << "のHPは" << healAmount << "回復した!" << std::endl;
            // std::cout << name << "の残りMPは" << mp << std::endl;
            // 運が良いと攻撃力が上昇
            // if (rand() % 3 == 0) {
            //     power += 30;
            //     std::cout << "攻撃力が30上昇！" << std::endl;
            // }
            return healAmount;
        } else {
            // std::cout << "MPが足りない..." << std::endl;
            return -1;
        }
    }

public:
    std::string name;
    int maxhp;
    int maxmp;
    int hp;
    int mp;
    int power;
    int block;
    int exp; // 経験値
    int level; // レベル
    std::vector<int> exp_level_list; // レベルアップに要する経験値

    int x; // x座標
    int y; // y座標
};

// 主人公クラス
class Hero : public StatusBase {
public:
    Hero() : StatusBase("") {} // デフォルトコンストラクタを追加
    Hero(const std::string& name) : StatusBase(name) {}

    ~Hero() {
        std::cout << "ゲーム終了" << std::endl;
    }

};

// ザコ敵クラス
class Enemy : public StatusBase {
public:
    Enemy() : StatusBase("") {} // デフォルトコンストラクタを追加
    Enemy(const std::string& name, int level, int x, int y)
        : StatusBase(name) {
        hp = 5 + level;
        maxhp = hp;
        mp = 0;
        maxmp = 0;
        power = 1 + level;
        block = 0 + level;
        this->exp = 1 + level;
        this->x = x;
        this->y = y;
        // std::cout << "ザコ敵の" << name << "が現れた！" << std::endl;
    }
};

// 中堅敵クラス
class Enemy2 : public StatusBase {
public:
    Enemy2() : StatusBase("") {} // デフォルトコンストラクタを追加
    Enemy2(const std::string& name, int level, int x, int y)
        : StatusBase(name) {
        hp = 10 + level;
        power = 3 + level;
        block = 1 + level;
        this->exp = 5 + level * 3;
        this->x = x;
        this->y = y;
        // std::cout << "中ボスの" << name << "が現れた！" << std::endl;
    }
};

// ボス敵クラス
class Boss : public StatusBase {
public:
    Boss() : StatusBase("") {} // デフォルトコンストラクタを追加
    Boss(const std::string& name, int level, int x, int y)
        : StatusBase(name) {
        hp = 20 + level;
        maxhp = hp;
        mp = 0;
        maxmp = 0;
        power = 10 + level;
        block = 3 + level;
        this->exp = 10 + level * 5;
        this->x = x;
        this->y = y;
        // std::cout << "ボスの" << name << "が現れた！" << std::endl;
    }
};


PoolAllocator<Hero, 1> hero_allocator;
const int enemy_cnt = 2; // 敵の数
PoolAllocator<Enemy, enemy_cnt> enemy_allocator;
const int enemy2_cnt = 1; // 中ボスの数
PoolAllocator<Enemy2, enemy2_cnt> enemy2_allocator;
const int boss_cnt = 1; // ボスの数
PoolAllocator<Boss, boss_cnt> boss_allocator;


// 残っている敵の数を取得
template<typename T>
int cnt_enemy_remain(std::vector<T*>& enemy_ptr_list){
    int cnt = 0;
    for(int i=0; i<enemy_ptr_list.size(); i++){
        if(enemy_ptr_list[i] == nullptr) continue;
        else cnt++;
    }
    return cnt;
}



// ステートマシンによってコントロールされていること（任意)
// スタート画面 0
void Start(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "スタート画面");
    ScreenSquareDraw(3, 1, 3, 37); // 枠
    ScreenWrite(4, 3, "なまえ を にゅうりょく してください");
    ScreenWrite(5, 3, "エンター で けってい します");
    ScreenWrite(6, 3, "");

    setCursorVisibility(true); // 入力時だけカーソルをオンにする
    setCursorPosition(6, 3);

    // プレイヤー名の入力受取
    std::string player_name;
    std::getline(std::cin, player_name);
    if(player_name == "") player_name = "ゆうしゃ";
    setCursorVisibility(false); // カーソルをオフに

    // プレイヤーのメモリ確保
    player_ptr = hero_allocator.Alloc();
    // プレイヤーのインスタンス生成
    new (player_ptr) Hero(player_name);
    // プレイヤーのステータスを作成
    player_ptr->name = player_name;
    player_ptr->x = 3;
    player_ptr->y = 9;
    player_ptr->exp_level_list = {0, 2, 7, 17, 30};
    player_ptr->level = 1;

    // 敵のメモリ確保
    enemy_ptr_list = {};
    enemy_ptr_list.push_back(enemy_allocator.Alloc());
    enemy_ptr_list.push_back(enemy_allocator.Alloc());
    // 中ボスのメモリ確保
    enemy2_ptr_list = {};
    enemy2_ptr_list.push_back(enemy2_allocator.Alloc());
    // ボスのメモリ確保
    boss_ptr_list = {};
    boss_ptr_list.push_back(boss_allocator.Alloc());

    // 敵のインスタンス生成
    new (enemy_ptr_list[0]) Enemy("スライムA", 0, 15, 10);
    new (enemy_ptr_list[1]) Enemy("スライムB", 0, 20, 13);
    // 中ボスのインスタンス生成
    new (enemy2_ptr_list[0]) Enemy2("ドラゴン", 0, 30, 11);
    // ボスのインスタンスを生成
    new (boss_ptr_list[0]) Boss("まおう", 0, 50, 12);

    current_state = State_Field; // スタート画面が終了したらフィールド画面へ
}

// フィールド画面：歩かせたい 1
void Field(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "フィールド画面");
    ScreenWrite(4, 1, "WASD: 上下左右, Q: ゲームをやめる");
    ScreenWrite(6, 1, Status2String(player_ptr));
    ScreenSquareDraw(7, 1, 10, 100); // フィールドの枠

    // テンキー or wasdで@マークが移動するだけのサンプル
    int x = 3; // X座標
    int y = 9; // Y座標


    // 敵の座標を描画
    // for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){
    //     Enemy* e_ptr = enemy_ptr_list[ei];
    //     ScreenPointDraw(e_ptr->x, e_ptr->y, '.'); // 敵プレイヤーの描画
    // }
    for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){

        Enemy* e_ptr = enemy_ptr_list[ei];

        
        ScreenPointDraw(e_ptr->x, e_ptr->y, '.'); // 敵プレイヤーの描画
    }


    // 中ボスの描画
    for(int ei = 0; ei < cnt_enemy_remain(enemy2_ptr_list); ei++){
        Enemy2* e_ptr = enemy2_ptr_list[ei];
        ScreenPointDraw(e_ptr->x, e_ptr->y, '*'); // 敵プレイヤーの描画
    }

    // ボスの描画
    for(int bi = 0; bi < cnt_enemy_remain(boss_ptr_list); bi++){
        Boss* b_ptr = boss_ptr_list[bi];
        ScreenPointDraw(b_ptr->x, b_ptr->y, 'B'); // 敵プレイヤーの描画
    }

    char input_key; // キー入力
    do{
        ScreenWrite(6, 1, Status2String(player_ptr)); // ステータスの描画
        ScreenPointDraw(player_ptr->x, player_ptr->y, '@'); // 現在のプレイヤーの描画
        input_key = getKey(); // キー入力待ち
        ScreenPointDraw(player_ptr->x, player_ptr->y, ' '); // 過去のプレイヤーの消去

        // キー入力でプレイヤーの座標更新
        switch (input_key) {
            case 's':
                if(player_ptr->y >= 17) break;
                else{
                    ++player_ptr->y;
                    break;
                }
            case 'a':
                if(player_ptr->x <= 2) break;
                else{
                    --player_ptr->x;
                    break;
                }
            case 'd':
                if(player_ptr->x >= 101) break;
                else{
                    ++player_ptr->x;
                    break;
                }
            case 'w':
                if(player_ptr->y <= 8) break;
                else{
                    --player_ptr->y;
                    break;
                }
        }

        // 敵の座標をまとめて表示
        for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){
            Enemy* e_ptr = enemy_ptr_list[ei];
            // 敵の座標をランダムに変更させる
            // ランダムデバイスとエンジンを設定
            std::random_device rd;  // 非決定的なランダム数生成器
            std::mt19937 gen(rd()); // メルセンヌ・ツイスタエンジン（シードに `rd` を使用）
            // 範囲を指定するための分布を設定
            std::uniform_int_distribution<> dis(1, 15); // 1 から 5 までの一様整数分布
            // ランダムな整数を生成
            int random_number = dis(gen);
            
            ScreenPointDraw(e_ptr->x, e_ptr->y, ' '); // 前の座標を消す

            switch (random_number){
                case 1:
                    if(e_ptr->y >= 17) break;
                    else{
                        ++e_ptr->y;
                        break;
                    }
                case 2:
                    if(e_ptr->x <= 2) break;
                    else{
                        --e_ptr->x;
                        break;
                    }
                case 3:
                    if(e_ptr->x >= 101) break;
                    else{
                        ++e_ptr->x;
                        break;
                    }
                case 4:
                    if(e_ptr->y <= 8) break;
                    else{
                        --e_ptr->y;
                        break;
                }
            }

            ScreenPointDraw(e_ptr->x, e_ptr->y, '.'); // 敵プレイヤーの描画
        }

        // 敵の座標と重なっているかどうか確認
        for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){
            Enemy* e_ptr = enemy_ptr_list[ei];
            // プレイヤーと敵の座標が重なっていたら戦闘画面へ遷移
            if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
                current_state = State_Battle;
                return;
            }
        }

        // 中ボスの座標をまとめて表示
        for(int ei = 0; ei < cnt_enemy_remain(enemy2_ptr_list); ei++){
            Enemy2* e_ptr = enemy2_ptr_list[ei];
            // ScreenWrite(5 + i, 1, Status2String(*e_ptr)); // 敵ステータスの表示
            ScreenPointDraw(e_ptr->x, e_ptr->y, '*'); // 敵プレイヤーの描画
        }

        // 中ボスの座標と重なっているかどうか確認
        for(int ei = 0; ei < cnt_enemy_remain(enemy2_ptr_list); ei++){
            Enemy2* e_ptr = enemy2_ptr_list[ei];
            // プレイヤーと敵の座標が重なっていたら戦闘画面へ遷移
            if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
                current_state = State_Battle;
                return;
            }
        }

        // ボスの座標をまとめて表示
        for(int bi = 0; bi < cnt_enemy_remain(boss_ptr_list); bi++){
            Boss* b_ptr = boss_ptr_list[bi];
            // ScreenWrite(5 + i, 1, Status2String(*b_ptr)); // 敵ステータスの表示
            ScreenPointDraw(b_ptr->x, b_ptr->y, 'B'); // 敵プレイヤーの描画
        }

        // ボスの座標と重なっているかどうか確認
        for(int bi = 0; bi < cnt_enemy_remain(boss_ptr_list); bi++){
            Boss* b_ptr = boss_ptr_list[bi];
            // プレイヤーと敵の座標が重なっていたら戦闘画面へ遷移
            if(player_ptr->x == b_ptr->x && player_ptr->y == b_ptr->y){
                current_state = State_Battle;
                return;
            }
        }

    }while(input_key != 'q');
    current_state = State_End; // q：終了
}

// 戦闘画面 2
void Battle(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "戦闘画面");
    ScreenWrite(4, 1, "1: たたかう, 2: かいふく, 3: にげる, Q: ゲームをやめる");
    // 敵の取得
    int index = 0;
    bool is_enemy = false; // 敵 or ボス
    // 敵を探す
    for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){
        Enemy* e_ptr = enemy_ptr_list[ei];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
            is_enemy = true;
            break;
        }
        index++;
    }
    Enemy enemy;
    if(is_enemy) enemy = *enemy_ptr_list[index]; // 敵のインスタンス

    // 中ボスを探す
    bool is_enemy2 = false; // 敵 or ボス
    index = 0;
    for(int ei = 0; ei < cnt_enemy_remain(enemy2_ptr_list); ei++){
        Enemy2* e_ptr = enemy2_ptr_list[ei];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
            is_enemy2 = true;
            break;
        }
        index++;
    }
    Enemy2 enemy2;
    if(is_enemy2) enemy2 = *enemy2_ptr_list[index]; // 敵のインスタンス

    // ボスを探す
    bool is_boss = false; // 敵 or ボス
    index = 0;
    for(int bi = 0; bi < cnt_enemy_remain(boss_ptr_list); bi++){
        Boss* b_ptr = boss_ptr_list[bi];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == b_ptr->x && player_ptr->y == b_ptr->y){
            is_boss = true;
            break;
        }
        index++;
    }
    Boss boss;
    if(is_boss) boss = *boss_ptr_list[index]; // ボスのインスタンス

    ScreenWrite(6, 1, Status2String(player_ptr)); // プレイヤーのステータスの表示
    if(is_enemy) ScreenWrite(7, 1, Status2String(&enemy)); // 敵ステータスの表示
    else if(is_enemy2) ScreenWrite(7, 1, Status2String(&enemy2));
    else if(is_boss) ScreenWrite(7, 1, Status2String(&boss));

    ScreenSquareDraw(8, 1, 4, 50); // 戦闘画面の枠
    std::string message1;
    if(is_enemy) message1 = enemy.name + " が あらわれた！"; // 現在のメッセージ
    else if(is_enemy2) message1 = enemy2.name + " が あらわれた！";
    else if(is_boss) message1 = boss.name + " が あらわれた！";
    std::string message2 = "コマンド を せんたく してください："; // 1つ前のメッセージ
    std::string message3 = ""; // 2つ前のメッセージ
    std::string message4 = ""; // 3つ前のメッセージ
    ButtleScreenDraw(message1, message2, message3, message4); // 戦闘画面の描画

    char input_key; 
    int damage_point;
    int heal_point;

    do{
        input_key = getKey(); // キー入力待ち

        // キー入力でプレイヤーの行動選択
        switch(input_key){
            case 'q':
                current_state = State_End; // qキーが押されたら終了    
                return;
            case '1': // たたかう
                if(is_enemy) damage_point = player_ptr->attack(&enemy);
                else if(is_enemy2) damage_point = player_ptr->attack(&enemy2);
                else if(is_boss) damage_point = player_ptr->attack(&boss);
                message1 = player_ptr->name + " の こうげき！";
                if(is_enemy) message2 = enemy.name + " に " + std::to_string(damage_point) + " の ダメージ！";
                else if(is_enemy2) message2 = enemy2.name + " に " + std::to_string(damage_point) + " の ダメージ！";
                else if(is_boss) message2 = boss.name + " に " + std::to_string(damage_point) + " の ダメージ！";
                if(is_enemy) message3 = enemy.name + " の のこりHP は " + std::to_string(enemy.hp);
                else if(is_enemy2) message3 = enemy2.name + " の のこりHP は " + std::to_string(enemy2.hp);
                else if(is_boss) message3 = boss.name + " の のこりHP は " + std::to_string(boss.hp);
                message4 = "なにか キー を おしてください";
                ButtleScreenDraw(message1, message2, message3, message4);
                break;
            case '2': // かいふく
                heal_point = player_ptr->heal();
                message1 = player_ptr->name + " は かいふくまほう を となえた！";
                if(heal_point == -1){
                    message2 = "しかし MP が たりなかった！";
                    message3 = "";
                }
                else{
                    message2 = player_ptr->name + " は  " + std::to_string(heal_point) + " かいふく した！";
                    message3 = player_ptr->name + " の のこりHP は " + std::to_string(player_ptr->hp);
                }
                message4 = "なにか キー を おしてください";
                ButtleScreenDraw(message1, message2, message3, message4);
                break;
            // case '3': // アイテム
            //     break;
            case '3': // にげる
                message1 = player_ptr->name + " は にげだした！";
                message2 = "";
                message3 = "";
                message4 = "なにか キー を おしてください";
                ButtleScreenDraw(message1, message2, message3, message4);
               
                player_ptr->x -= 1;  // プレイヤーの座標を戻す
                current_state = State_Field; // 逃げたらフィールド画面へ戻す
                getKey(); // キー入力待ち
                return;
        }

        // 変動したステータスを表示
        ScreenWrite(6, 1, "                                                                                        ");
        ScreenWrite(6, 1, Status2String(player_ptr)); // プレイヤーのステータスの表示
        ScreenWrite(7, 1, "                                                                                        ");
        if(is_enemy) ScreenWrite(7, 1, Status2String(&enemy)); // 敵ステータスの表示
        else if(is_enemy2) ScreenWrite(7, 1, Status2String(&enemy2));
        else if(is_boss) ScreenWrite(7, 1, Status2String(&boss));

        getKey(); // キー入力待ち

        // 敵のHPが0になってたらリザルト画面へ遷移
        if((is_enemy && enemy.hp <= 0) || (is_enemy2 && enemy2.hp <= 0) || (is_boss && boss.hp <= 0)){
            current_state = State_Result;
            return;
        }

        // 敵の攻撃
        if(is_enemy) damage_point = enemy.attack(player_ptr);
        else if(is_enemy2) damage_point = enemy2.attack(player_ptr);
        else if(is_boss) damage_point = boss.attack(player_ptr);
        if(is_enemy) message1 = enemy.name + " の こうげき！";
        else if(is_enemy2) message1 = enemy2.name + " の こうげき！";
        else if(is_boss) message1 = boss.name + " の こうげき！";
        message2 = player_ptr->name + " に " + std::to_string(damage_point) + " の ダメージ！";
        message3 = player_ptr->name + " の のこりHP は " + std::to_string(player_ptr->hp);
        message4 = "コマンド を せんたく してください";
        ButtleScreenDraw(message1, message2, message3, message4);

        // 変動したステータスを表示
        ScreenWrite(6, 1, "                                                                                        ");
        ScreenWrite(6, 1, Status2String(player_ptr)); // プレイヤーのステータスの表示
        ScreenWrite(7, 1, "                                                                                        ");
        if(is_enemy) ScreenWrite(7, 1, Status2String(&enemy)); // 敵ステータスの表示
        else if(is_enemy2) ScreenWrite(7, 1, Status2String(&enemy2));
        else if(is_boss) ScreenWrite(7, 1, Status2String(&boss));

        // 自分のHPが0になってたらゲームオーバー画面へ遷移
        if(player_ptr->hp <= 0){
            // 画面の描画
            ScreenWrite(6, 1, Status2String(player_ptr)); // 経験値取得後のプレイヤーのステータスの表示
            message4 = "なにか キー を おしてください";
            ButtleScreenDraw(message1, message2, message3, message4);   
            getKey(); // キー入力待ち
            current_state = State_GameOver;
            return;
        }
        current_state = State_Result; // 戦闘が終了したらリザルト画面へ
    }while(input_key != 'q');

}

// リザルト画面 3
void Ressult(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "結果画面");
    // 倒した敵のステータス
    std::string name;
    int exp;

    // 敵の取得
    int index_enemy = 0;
    bool is_enemy = false;
    for(int ei = 0; ei < cnt_enemy_remain(enemy_ptr_list); ei++){
        Enemy* e_ptr = enemy_ptr_list[ei];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
            name = e_ptr->name;
            exp = e_ptr->exp;
            is_enemy = true;
            break;
        }
        index_enemy++;
    }
    Enemy& enemy = *enemy_ptr_list[index_enemy]; // 敵のインスタンス

    // 中ボスの取得
    int index_enemy2 = 0;
    int is_enemy2 = false;
    for(int ei = 0; ei < cnt_enemy_remain(enemy2_ptr_list); ei++){
        Enemy2* e_ptr = enemy2_ptr_list[ei];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
            name = e_ptr->name;
            exp = e_ptr->exp;
            is_enemy2 = true;
            break;
        }
        index_enemy2++;
    }
    Enemy2& enemy2 = *enemy2_ptr_list[index_enemy2]; // 敵のインスタンス

    // ボスの取得
    int index_boss = 0;
    int is_boss = false;
    for(int ei = 0; ei < cnt_enemy_remain(boss_ptr_list); ei++){
        Boss* e_ptr = boss_ptr_list[ei];
        // プレイヤーと敵の座標が重なっているところを探す
        if(player_ptr->x == e_ptr->x && player_ptr->y == e_ptr->y){
            name = e_ptr->name;
            exp = e_ptr->exp;
            is_boss = true;
            break;
        }
        index_boss++;
    }
    Boss& boss = *boss_ptr_list[index_boss]; // 敵のインスタンス

    // 経験値を獲得
    player_ptr->exp += exp;

    ScreenWrite(6, 1, "                                                                                        ");
    ScreenWrite(6, 1, Status2String(player_ptr)); // プレイヤーのステータスの表示
    // ScreenWrite(7, 1, "                                                                                        ");
    // ScreenWrite(7, 1, Status2String(&enemy)); // 敵ステータスの表示
    ScreenSquareDraw(8, 1, 4, 50); // 戦闘画面の枠

    std::string message1 = name + " を たおした！";
    std::string message2 = player_ptr->name + " は EXP を " + std::to_string(exp) + " かくとく した";
    std::string message3 = "";
    std::string message4 = "なにか キー を おしてください";
    ButtleScreenDraw(message1, message2, message3, message4);

    // メモリの解放
    if(is_enemy){
        enemy_allocator.Free(enemy_ptr_list[index_enemy]);
        // 要素を左にシフトして、指定のインデックスを除外
        for (int i = index_enemy; i < cnt_enemy_remain(enemy_ptr_list) - 1; ++i) {
            enemy_ptr_list[i] = enemy_ptr_list[i + 1];
        }
        // 最後の要素は不要なので nullptr を設定（オプション）
        enemy_ptr_list[cnt_enemy_remain(enemy_ptr_list) - 1] = nullptr;
    }
    else if(is_enemy2){
        enemy2_allocator.Free(enemy2_ptr_list[index_enemy2]);
        // 要素を左にシフトして、指定のインデックスを除外
        for (int i = index_enemy2; i < cnt_enemy_remain(enemy2_ptr_list) - 1; ++i) {
            enemy2_ptr_list[i] = enemy2_ptr_list[i + 1];
        }
        // 最後の要素は不要なので nullptr を設定（オプション）
        enemy2_ptr_list[cnt_enemy_remain(enemy2_ptr_list) - 1] = nullptr;
    }
    else if(is_boss){
        boss_allocator.Free(boss_ptr_list[index_boss]);
        // 要素を左にシフトして、指定のインデックスを除外
        for (int i = index_boss; i < cnt_enemy_remain(boss_ptr_list) - 1; ++i) {
            boss_ptr_list[i] = boss_ptr_list[i + 1];
        }
        // 最後の要素は不要なので nullptr を設定（オプション）
        boss_ptr_list[cnt_enemy_remain(boss_ptr_list) - 1] = nullptr;
    }

    ScreenWrite(6, 1, Status2String(player_ptr)); // 経験値取得後のプレイヤーのステータスの表示
    char input_key = getKey(); // キー入力待ち

    // ボスを倒したらクリア画面へ
    if(is_boss){
        current_state = State_GameClear;
    }
    // 経験値が溜まっていない場合はフィールド画面へ
    else if(player_ptr->exp < player_ptr->exp_level_list[player_ptr->level]){
        current_state = State_Field; // フィールド画面へ
    }
    // 経験値が溜まっている場合はレベルアップ
    else{
        current_state = State_LevelUp; // レベルアップ
    }
}

// レベルアップ画面 4
void LevelUP(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "レベルアップ画面");
    ScreenWrite(4, 1, "1: HP, 2: MP, 3: 攻撃力, 4: 防御力");
    ScreenWrite(6, 1, Status2String(player_ptr)); // 経験値取得後のプレイヤーのステータスの表示
    std::string message1;
    std::string message2;
    std::string message3;
    std::string message4;

    for(int i=0; i<3; i++){
        ScreenWrite(6, 1, Status2String(player_ptr)); // 経験値取得後のプレイヤーのステータスの表示
        message1 = player_ptr->name + " は レベル が あがった！";
        message2 = "あげたい ステータス を " + std::to_string(3 - i) + " つ えらんで ください！";
        if(i == 0) message3 = "";
        message4 = "1: HP, 2: MP, 3: 攻撃力, 4: 防御力";
        ButtleScreenDraw(message1, message2, message3, message4);
        char input_key = getKey(); // キー入力待ち
        switch (input_key){
            case '1':
                player_ptr->maxhp += 5;
                player_ptr->hp = player_ptr->maxhp;
                message3 = player_ptr->name + " の HPが 5 あがった！";
                break;
            case '2':
                player_ptr->maxmp += 5;
                player_ptr->mp = player_ptr->maxmp;
                message3 = player_ptr->name + " の MPが 5 あがった！";
                break;
            case '3':
                player_ptr->power += 2;
                message3 = player_ptr->name + " の 攻撃力が 2 あがった！";
                break;
            case '4':
                player_ptr->block += 2;
                message3 = player_ptr->name + " の 防御力が 2 あがった！";
                break;
        }

    }
    ScreenWrite(6, 1, Status2String(player_ptr)); // 経験値取得後のプレイヤーのステータスの表示
    message2 = "";
    message4 = "なにか キー を おしてください";
    ButtleScreenDraw(message1, message2, message3, message4);   
    
    char input_key = getKey(); // キー入力待ち

    current_state = State_Field; // レベルアップが終わったら再度フィールド画面へ
}

// ゲームオーバー画面 5
void GameOver(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "ゲームオーバー画面");
    ScreenWrite(4, 1, "R: リトライ, 他: ゲームを終了                                        ");

    std::string message1 = player_ptr->name + "は しんでしまった．．．";
    std::string message2 = "";
    std::string message3 = "リトライ: R";
    std::string message4 = "ゲームをやめる: 他のキー";
    ButtleScreenDraw(message1, message2, message3, message4);   
    
    char input_key = getKey(); // キー入力待ち
    
    switch (input_key){
        case 'r':
            current_state = State_Start; // rボタンが押されたらスタート画面へ戻す
            // 残っている全てのメモリを解放
            hero_allocator.Free(player_ptr);
            for(int i=0; i<enemy_ptr_list.size(); i++){
                enemy_allocator.Free(enemy_ptr_list[i]);
            }
            for(int i=0; i<enemy2_ptr_list.size(); i++){
                enemy2_allocator.Free(enemy2_ptr_list[i]);
            }
            for(int i=0; i<boss_ptr_list.size(); i++){
                boss_allocator.Free(boss_ptr_list[i]);
            }
            break;
        default:
            current_state = State_End; // 終了
            break;
    }
}

// ゲームクリア画面
void GameClear(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){
    ScreenWrite(2, 1, "ゲームクリア画面");
    ScreenWrite(4, 1, "なにかキーをおしてください");
    ScreenSquareDraw(5, 1, 5, 63);
    ScreenWrite(6, 3, player_ptr->name + " は まおう を たおした！");
    getKey();
    ScreenWrite(8, 3, "まばゆい ばかり の ひかり が あたり に あふれだす......");
    getKey();
    ScreenWrite(10, 3, player_ptr->name + " の かつやく により せかい に へいわ が もどったのだ！");
    getKey();
    ScreenSquareClear(5, 1, 5, 63);
    ScreenWrite(8, 3, player_ptr->name + " の あたらな たびが はじまる．");
    getKey();
    ScreenSquareClear(5, 1, 5, 63);
    ScreenWrite(6, 3,  "    ######  ##   ##  #####        #####  ##   ##  ####  ");
    ScreenWrite(7, 3,  "      ##    ##   ##  ##           ##     ###  ##  ##  ## ");
    ScreenWrite(8, 3,  "      ##    #######  #####        #####  ## # ##  ##   ##");
    ScreenWrite(9, 3,  "      ##    ##   ##  ##           ##     ##  ###  ##  ## ");
    ScreenWrite(10, 3, "      ##    ##   ##  #####        #####  ##   ##  ####  ");
    getKey();

    // 残っている全てのメモリを解放
    hero_allocator.Free(player_ptr);
    for(int i=0; i<enemy_ptr_list.size(); i++){
        enemy_allocator.Free(enemy_ptr_list[i]);
    }
    for(int i=0; i<enemy2_ptr_list.size(); i++){
        enemy2_allocator.Free(enemy2_ptr_list[i]);
    }
    for(int i=0; i<boss_ptr_list.size(); i++){
        boss_allocator.Free(boss_ptr_list[i]);
    }

    current_state = State_Start;
}

// ゲーム終了画面
void End(Hero*& player_ptr, std::vector<Enemy*>& enemy_ptr_list, std::vector<Enemy2*>& enemy2_ptr_list, std::vector<Boss*>& boss_ptr_list){

}


int main() {
    // 自分が作成した Poolアロケータが使われていること(必須)
    // プレイヤーのポインタ
    Hero* player_ptr;
    // 敵のポインタ
    std::vector<Enemy*> enemy_ptr_list;
    // 中ボスのポインタ
    std::vector<Enemy2*> enemy2_ptr_list;
    // ボスのポインタ
    std::vector<Boss*> boss_ptr_list;

    // エスケープシーケンスを有効に
    std::cout << "\x1b[?1049h" << std::flush; // カーソルの動きを有効に

    // 画面クリア
    ScreenAllClear();

    // カーソルを消す
    setCursorVisibility(false);

    {
        do {
            // デバッグ表示
            ScreenWrite(1, 1, "current_state: " + std::to_string(current_state));

            // ゲーム状態管理
            switch (current_state) {
                case State_Start:
                    ScreenAllClear();
                    Start(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;
                case State_Field:
                    ScreenAllClear();
                    Field(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;
                case State_Battle:
                    Battle(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    break;
                case State_Result:
                    Ressult(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    break;          
                case State_LevelUp:
                    LevelUP(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;   
                case State_GameOver:
                    GameOver(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;
                case State_GameClear:
                    ScreenAllClear();
                    GameClear(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;
                case State_End:
                    ScreenAllClear();
                    End(player_ptr, enemy_ptr_list, enemy2_ptr_list, boss_ptr_list);
                    ScreenAllClear();
                    break;   
            }
        } while (current_state != State_End); // 終了
    }

    // カーソルを表示
    setCursorVisibility(true);

    // 元の画面モードに戻す
    std::cout << "\x1b[?1049l" << std::flush;

    return EXIT_SUCCESS;
}


// スライム
//    ##  
//  ###### 
// ## ## ##
//  ######   