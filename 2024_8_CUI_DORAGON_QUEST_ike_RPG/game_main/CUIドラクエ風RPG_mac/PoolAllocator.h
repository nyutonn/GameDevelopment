#pragma once

#include <cstddef> // size_t

// class Tを最大MAXSIZE個確保可能なPoolAllocatorを実装してください
template<class T, size_t MAXSIZE> class PoolAllocator
{
public:
    // コンストラクタ
    PoolAllocator() : m_freeListPtr(nullptr) {
        // 初期化時に全てのブロックを解放する
        for (size_t i = 0; i < MAXSIZE; i++) {
            Free(reinterpret_cast<T*>(&m_blocks[i])); // i個目のブロックを解放
        }
    }

    // デストラクタ
    ~PoolAllocator() {
    }

    // 確保できない場合はnullptrを返す事。
    T* Alloc() {
        // 確保できない場合
        if (m_freeListPtr == nullptr) // 現在空いているポインタがない
            return nullptr;
        // 確保可能な場合
        else{
            Block* blockPtr = m_freeListPtr; // フリーリストの先頭からブロックを取得
            m_freeListPtr = blockPtr->nextPtr; // フリーリストには次の空きブロックを設定
            return reinterpret_cast<T*>(blockPtr); // T型のポインタに変換して今回確保したブロックのアドレス返す
        }
    }

    // Free(nullptr)で誤動作しないようにする事。
    void Free(T* addr) {
        // nullptrのときの処理：何もしない
        if (addr == nullptr) return;

        // ブロックをフリーリストの先頭に追加
        Block* blockPtr = reinterpret_cast<Block*>(addr); // T型のポインタaddrをBlock型のポインタに変換
        blockPtr->nextPtr = m_freeListPtr; // 次の空きブロックのポインタは1つ前のBlackのアドレスを設定
        m_freeListPtr = blockPtr; // 今回解放したブロックのアドレスをフリーリストにする
    }

private:
    // メモリプールの各ブロック
    // メモリ解放中：nextPtrのみ使用
    // メモリ確保中：dataのみ使用
    // このように構造体内でメンバ変数が同時に使われない（排他的）場合は，共用体unionのほうがメモリの節約になる
    struct Block {
    // union Block{ // 共用体のほうがメモリの節約につながる
        T data; // ブロックにいれるT型のデータ
        Block* nextPtr; // 次の空きブロックへのポインタ
    };
    // 確保したい全てのブロック
    Block m_blocks[MAXSIZE];
    // m_freeListPtr:空いているブロックの先頭を指すポインタ
    // Block 分のメモリを確保した後は Block.nextPtr に変更する
    Block* m_freeListPtr;
};
