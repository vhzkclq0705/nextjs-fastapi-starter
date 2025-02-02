
'use client'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useState } from "react";

export default function Home() {
  const [birthday, setBirthday] = useState("");
  const [age, setAge] = useState<number | null>(null);
  const [kage, setKage] = useState<number | null>(null);
  const [zodiac, setZodiac] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [student, setStudent] = useState<string | null>(null);

  const handleCalculateAge = async () => {
    setError(null);
    setAge(null);
    setKage(null);
    setZodiac(null);

    if (!birthday) {
      setError("Please enter your birthday.");
      return;
    }

    try {
      const response = await fetch(`/api/py/ageCalculator/${birthday}`);
      const data = await response.json();

      if (response.ok) {
        setAge(data.age);
        setKage(data.kage);
        setZodiac(data.zodiac);
      } else {
        setError(data.error || "Failed to calculate age.");
      }
    } catch (err) {
      setError("An error occurred while fetching the API.");
    }
  };

  // 랜덤 학생 뽑기
  const getRandomStudent = async () => {
    setError(null);
    setStudent(null);

    try {
      const response = await fetch(`/api/py/randomStudent`);
      const data = await response.json();

      if (response.ok) {
	setStudent(data.student);
      } else {
	setError(data.error || "Failed to get a student.");
      }
    } catch (err) {
      setError("An error occurred while fetching the API.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-green-600 p-4">
      <div className="max-w-md w-full bg-white shadow-md rounded p-6 space-y-4">
        <h1 className="text-3xl font-bold text-center">나이 계산기(만, 연, 띠)</h1>
        <h1 className="text-xl font-bold text-center text-green-600">WHY NOT?</h1>

        <div>
          <label htmlFor="birthday" className="block text-sm font-medium text-gray-700">
            Enter your birthday
          </label>
          <Input
            type="date"
            id="birthday"
            value={birthday}
            onChange={(e) => setBirthday(e.target.value)}
          />
        </div>

        <Button onClick={handleCalculateAge} className="w-full">
          Calculate Age
        </Button>

	<Button onClick={getRandomStudent} className="w-full">
	  Get a random student
	</Button>

        {age !== null && (
          <div className="mt-4 text-center text-green-600 font-semibold">
            Your age: {age}
          </div>
        )}

	{kage != null && (
	  <div className="mt-4 text-center text-red-600 font-semibold">
	    Your korean_age: {kage}
	  </div>
	)}

        {zodiac && (
          <div className="mt-4 text-center text-blue-600 font-semibold">
            Your zodiac: {zodiac}
          </div>
        )}

	{student && (
	  <div className="mt-4 text-center text-orange-600 font-semibold">
	    Student: {student}
	  </div>
	)}
         
        {error && (
          <div className="mt-4 text-center text-red-600 font-semibold">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
