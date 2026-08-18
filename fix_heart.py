import os

missing_css = """
/* ==================================
   HEART DISEASE SPECIFIC
=================================== */
.snapshot {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  margin-top: 16px;
}

.snapshot-item {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 16px 24px;
  flex: 1;
  min-width: 150px;
  text-align: center;
}

.snapshot-item .number {
  display: block;
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  color: #60a5fa;
  font-weight: 700;
  margin-bottom: 4px;
}

.snapshot-item .label {
  color: #94a3b8;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}

.question-list {
  list-style: none;
  padding-left: 0 !important;
}

.question-list li {
  position: relative;
  padding-left: 24px;
  margin-bottom: 12px;
  color: #cbd5e1;
}

.question-list li::before {
  content: '❓';
  position: absolute;
  left: 0;
  top: 0;
}

.analysis-item {
  margin-bottom: 16px;
  padding-left: 16px;
  border-left: 3px solid #3b82f6;
}

.finding-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.finding {
  background: rgba(15, 23, 42, 0.4);
  padding: 16px;
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.finding strong {
  display: block;
  color: #38bdf8;
  margin-bottom: 8px;
  font-size: 15px;
}

.finding span {
  color: #cbd5e1;
  font-size: 14px;
  line-height: 1.6;
}

.highlight-metric {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin: 24px 0;
}

.metric {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  transition: all 0.3s ease;
}

.metric:hover {
  background: rgba(30, 41, 59, 0.8);
  border-color: rgba(96, 165, 250, 0.3);
  transform: translateY(-3px);
}

.metric strong {
  display: block;
  font-family: 'Outfit', sans-serif;
  font-size: 28px;
  color: #60a5fa;
  margin-bottom: 4px;
}

.metric span {
  color: #94a3b8;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.result-image {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 12px;
  margin: 30px auto;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: block;
}

.result-table-wrapper {
  overflow-x: auto;
  margin-bottom: 24px;
}

.result-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.result-table th, .result-table td {
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.result-table th {
  background: rgba(15, 23, 42, 0.8);
  color: #f1f5f9;
  font-weight: 600;
  font-size: 14px;
}

.result-table td {
  color: #cbd5e1;
  font-size: 14px;
}

.result-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}

.result-note {
  background: rgba(59, 130, 246, 0.1);
  border-left: 4px solid #3b82f6;
  padding: 16px 20px;
  border-radius: 0 8px 8px 0;
  color: #cbd5e1;
  font-size: 14px;
  line-height: 1.6;
}

.result-note strong {
  color: #60a5fa;
}

@media (max-width: 760px) {
  .highlight-metric {
    grid-template-columns: repeat(2, 1fr);
  }
  .finding-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open(r"c:\bismillah kerja sukse\porto\style.css", "a", encoding="utf-8") as f:
    f.write(missing_css)

print("Appended Heart Disease CSS to style.css")
