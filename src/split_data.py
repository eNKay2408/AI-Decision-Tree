from sklearn.model_selection import train_test_split

def create_splits(X, y, ratios=[(0.4,0.6),(0.6,0.4),(0.8,0.2),(0.9,0.1)]):
    """
    Chia dữ liệu thành nhiều tập train/test với các tỷ lệ khác nhau
    
    Args:
        X: Features DataFrame
        y: Target Series
        ratios: List of tuples (train_size, test_size)
        
    Returns:
        List of tuples: (X_train, X_test, y_train, y_test) cho mỗi tỷ lệ
    """
    try:
        splits = []
        for i, (tsize, _) in enumerate(ratios):
            print(f"Tạo split với tỷ lệ train/test = {tsize}/{1-tsize}")
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, train_size=tsize, stratify=y, random_state=42
            )
            print(f"  - Train set: {X_train.shape[0]} mẫu, {X_train.shape[1]} đặc trưng")
            print(f"  - Test set: {X_test.shape[0]} mẫu, {X_test.shape[1]} đặc trưng")
            
            # Check class distribution
            train_dist = y_train.value_counts().to_dict()
            test_dist = y_test.value_counts().to_dict()
            print(f"  - Train class distribution: {train_dist}")
            print(f"  - Test class distribution: {test_dist}")
            
            splits.append((X_train, X_test, y_train, y_test))
        
        return splits
        
    except Exception as e:
        print(f"Lỗi khi tạo splits: {e}")
        import traceback
        traceback.print_exc()
        raise