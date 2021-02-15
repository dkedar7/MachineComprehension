cd Machine\ Comprehension/
gcloud builds submit --tag gcr.io/web-apps-273916/machinecomprehension
gcloud run deploy machine-comprehension --image gcr.io/web-apps-273916/machinecomprehension --platform managed --allow-unauthenticated --region us-central1 --memory 2Gi