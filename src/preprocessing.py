import pandas as pd
import os
import traceback
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def load_and_preprocess(path):
    """
    Đọc và tiền xử lý dữ liệu penguins từ đường dẫn chỉ định
    
    Xử lý:
    - Kiểm tra tồn tại file
    - Impute giá trị thiếu trong numeric columns
    - Fill giá trị thiếu trong categorical columns
    - One-hot encoding cho categorical features
    - Tách feature và label
    
    Args:
        path: Đường dẫn đến file dữ liệu
        
    Returns:
        X: DataFrame các đặc trưng
        y: Series chứa nhãn
    """
    # Kiểm tra file tồn tại
    if not os.path.exists(path):
        raise FileNotFoundError(f"File không tồn tại: {path}")
        
    try:
        # Đọc dữ liệu
        df = pd.read_csv(path)
        print(f"Đã đọc được file với {df.shape[0]} dòng và {df.shape[1]} cột.")
        
        # Impute numeric columns
        numeric_cols = df.select_dtypes(include='number').columns
        print(f"Các cột số: {list(numeric_cols)}")
        imputer = IterativeImputer(max_iter=10, random_state=42)
        df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
        
        # Fill missing categorical values
        print("Xử lý categorical columns...")
        if 'sex' in df.columns:
            print(f"Giá trị null trong cột sex trước khi điền: {df['sex'].isnull().sum()}")
            df['sex'].fillna(df['sex'].mode()[0], inplace=True)
            print(f"Giá trị null trong cột sex sau khi điền: {df['sex'].isnull().sum()}")
        
        # One-hot encoding
        print("Thực hiện one-hot encoding...")
        categorical_cols = ['sex', 'island']
        # Chỉ encode các cột có trong DataFrame
        cols_to_encode = [col for col in categorical_cols if col in df.columns]
        df = pd.get_dummies(df, columns=cols_to_encode, drop_first=True)
        
        # Tách feature và label
        if 'species' not in df.columns:
            raise ValueError("Không tìm thấy cột 'species' trong dataset!")
            
        X = df.drop('species', axis=1)
        y = df['species']
        
        print("Tiền xử lý hoàn tất.")
        print(f"Các đặc trưng sau khi xử lý: {list(X.columns)}")
        print(f"Unique values trong target: {y.unique()}")
        
        return X, y
        
    except Exception as e:
        print(f"Lỗi trong quá trình xử lý dữ liệu: {str(e)}")
        traceback.print_exc()
        raise