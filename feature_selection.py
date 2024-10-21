
def SHAP_fs(self, model, X, thresh_perc=1):
        explainer = shap.Explainer(model)
        shap_values = explainer.shap_values(X)

        # For LightGBM binary classification, select the SHAP values for the positive class
        if isinstance(shap_values, list):
            shap_values = shap_values[1]  # assuming you're interested in the positive class

        shap_sum = np.abs(shap_values).sum(axis=0)
        sorted_indices = np.argsort(shap_sum)[::-1]
        cumulative_sum = np.cumsum(shap_sum[sorted_indices])
        total_shap_sum = cumulative_sum[-1]  # Total sum of SHAP values
        threshold = thresh_perc * total_shap_sum
        num_features = np.argmax(cumulative_sum >= threshold) + 1  # Number of features needed
        selected_features = X.columns[sorted_indices[:num_features]]
        cols = selected_features.tolist()

        # Sort the SHAP values and feature names
        sorted_indices = np.argsort(shap_sum)[::-1]
        sorted_shap_values = shap_sum[sorted_indices]
        sorted_feature_names = X.columns[sorted_indices]

        # Increase the figure size to make the y-axis longer
        plt.figure(figsize=(10, 8))
        # Plot the bar chart
        plt.bar(sorted_feature_names[:25], sorted_shap_values[:25])
        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=90)
        plt.xlabel("Features")
        plt.ylabel("SHAP Value")
        plt.title("SHAP Feature Importance")
        # Adjust the placement of y-axis labels for better readability
        plt.subplots_adjust(bottom=0.4)  # You can adjust the value as needed
        plt.show()

        return cols